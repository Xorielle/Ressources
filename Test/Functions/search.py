#! /usr/bin/python3
# -*- coding: utf-8 -*-


import pymysql
import datetime
import Functions.buildSQL as build


def typeOfSearch():
    """Choose if the search is simple (one criteria) or advanced (many criterias)"""
    search = input("Souhaitez-vous effectuer une recherche simple [S] ou avancée [A] ? ")
    if search != "S" and search != "A":
        return(typeOfSearch())
    
    else: 
        return(search)


def chooseTable():
    """Choose wether we are searching in Materiaux or Pieces.
    Return usedTable"""
    table = input("Voulez-vous effectuer une recherche parmi les matériaux [M] ou les pièces [P] ? ")
    
    if table == "M": 
        return("Materiaux")
    
    if (table == "P"):
        return("Pieces")
    
    else:
        return(chooseTable())


def getTableStructure(usedTable, cursor):
    """Create the list of all columns/criterias in the table.
    Return columns, type_columns, sizeTable"""
    columns = []
    type_columns = []
    cursor.execute("DESCRIBE %s;" % usedTable)
    description = cursor.fetchall()
    sizeTable = 0
    
    for row in description:
        columns.append(row[0])
        type_columns.append(row[1])
        sizeTable += 1
    
    return(columns, type_columns, sizeTable)


def getColumnToSearch(namesColumns, columns, type_columns):
    """Ask in which column (that means wich criteria) the user wants to search.
    Return searched_column, type_column"""
    print("Dans quelle colonne souhaitez-vous effectuer une recherche ? \
        Tapez Entrée jusqu'à arriver à la colonne souhaitée, puis tapez n'importe quelle touche pour cette colonne-ci.")
    answer = ""
    nb = 0

    while answer == "":
        answer = input(namesColumns[nb] + " ? ")
        nb += 1
    
    return(namesColumns[nb-1], columns[nb-1], type_columns[nb-1])


def getColumnsToSearch(namesColumns, columns, type_columns, sizeTable):
    """Ask in which columnS the user wants to search.
    Return two lists : s_columns, s_type_columns"""
    print("Dans quelles colonnes souhaitez-vous effectuer une recherche ? Tapez Entrée jusqu'à arriver aux colonnes souhaitées, puis tapez n'importe quelle touche pour ces colonnes-ci.")
    s_columns = []
    s_names = []
    s_type_columns = []
    nb = 0
    sizeRequest = 0

    for nb in range(sizeTable):
        nameColumn = namesColumns[nb]
        column = columns[nb]
        answer = input(nameColumn + " ? ")
        
        if answer != "":
            sizeRequest += 1
            s_names.append(nameColumn)
            s_columns.append(column)
            s_type_columns.append(type_columns[nb])

    return(s_names, s_columns, s_type_columns, sizeRequest)


def getSearchCriteria(usedTable, nameColumn, type_column, cursor):
    """Ask which criteria is searched in the column.
    Return the tuple (criteria, none) or (min, max) or (none, none) if error"""

    if ("char" or "text") in type_column:
        criteria = input("Quel terme souhaitez-vous chercher dans la colonne %s ? " % nameColumn)
        return(criteria, None)
    
    elif ("int" or "float") in type_column:
        searchMode = input("Effectuer une recherche numérique simple [S] ou bien une recherche sur un intervalle [I] ? ")    
        if searchMode == "S":
            return(numericSimple(type_column))
        elif searchMode == "I":
            return(numericInterval(usedTable, nameColumn, type_column, cursor))
        else:
            return(getSearchCriteria(usedTable, nameColumn, type_column, cursor))

    elif "date" in type_column:
        print("Entrer les dates sous la forme aaaa-mm-jj.")
        return(getDate())
    
    else:
        print("Il n'est pas possible d'effectuer de recherche sur cette colonne.")
        return(None, None)


def getDate():
    date_min = str(input("Date initiale ? "))
    date_max = input("Date de fin ? ")
    return(date_min, date_max)


def getSearchCriterias(usedTable, s_names, s_columns, s_type_columns, sizeRequest, cursor):
    """Ask the criteria for each column. Multiple search in one column is possible.
    Return a list of strings containing pieces of SQL request."""
    searched = [] # List with strings (one per column) for the request in SQL 
    
    for nb in range(sizeRequest):
        name = s_names[nb]
        type_column = s_type_columns[nb]
        column = s_columns[nb]
        print("Critères de recherche pour la colonne " + name)

        if nb != 0:
            searched.append(" AND")

        if ("char" in type_column) or ("text" in type_column):
            criterias_and = [input("Quel mot ou expression exacte souhaitez-vous chercher ? ")]
            criterias_not = []
            criterias_or = []
            answer = input("Souhaitez-vous ajouter un terme supplémentaire pour cette colonne ? [O/N] ")
            
            while answer == "O":
                criteria, answer = getNewCriteriaText()

                if criteria[1] == "AND": # Here is criteria the tuple (term, modulator)
                    criterias_and.append(criteria[0]) 
                elif criteria[1] == "NOT":
                    criterias_not.append(criteria[0])
                elif criteria[1] == "OR":
                    criterias_or.append(criteria[0])

            # All functions are in buildSQL. Depending on if OR and NOT modulators are present or not, we are not using the same function.
            if criterias_or != []:
                if criterias_not == []:
                    searched.append(build.createRequestTextAo(column, criterias_and, criterias_or))
                else:
                    searched.append(build.createRequestTextAon(column, criterias_and, criterias_not, criterias_or))
            
            elif criterias_not != []:
                searched.append(build.createRequestTextAn(column, criterias_and, criterias_not))
            
            else:
                searched.append(build.createRequestTextA(column, criterias_and))

        elif ("int" in type_column) or ("float" in type_column):
            searchMode = input("Effectuer une recherche numérique simple [S] ou bien une recherche sur un intervalle [I] ? ")    
            
            if searchMode == "S":

                criteriaOK = 0

                while criteriaOK == 0: # Be sure the entry is a number.
                    searched_number, tolerancy = numericSimple(type_column)
                    
                    if (type(searched_number) == int) or (type(searched_number) == float):    
                        criteriaOK = 1
                        if tolerancy == None:
                            searched.append(build.createRequestNumericSimple(column, searched_number))
                        else:
                            searched.append(build.createRequestNumericTolerancy(column, searched_number, tolerancy))

            else: 
                searched_number_min, searched_number_max = numericInterval(usedTable, column, type_column, cursor)
                searched.append(build.createRequestNumericInterval(column, searched_number_min, searched_number_max))
        
        elif "date" in type_column:
            print("Entrer les dates sous la forme aaaa-mm-jj.")
            date_min, date_max = getDate()
            searched.append(build.createRequestDate(column, date_min, date_max))
        
        else:
            searched.pop()
            print("Il n'est pas possible d'effectuer de recherche sur cette colonne")
            print("Passage à la colonne suivante.")

    return(searched)


def getNewCriteriaText():
    """Ask a term to add to the search. Modulate is with NOT, AND, OR.
    Return ((term, modulator), answer)"""
    print("Vous pouvez entrer un nouveau terme à rechercher dans cette colonne. Ensuite, vous pourrez également le moduler (avec NOT, AND ou OR)")
    term = input("Quel terme souhaitez-vous ajouter à la recherche ? ")
    modulator = input("Souhaitez-vous le moduler ? Entrez OR, AND ou NOT. ")
    
    if modulator not in ["NOT", "AND", "OR"]:
        print("Mauvaise entrée, le terme recheché n'a pas été retenu.")
        return((None, None), "O")
    
    answer = input("Souhaitez-vous ajouter un terme supplémentaire à votre recherche sur cette colonne ? [O/N] ")
    return((term, modulator), answer)


def numericSimple(type_column):
    """Numeric search with the possibility of adding a tolerancy.
    Return (min, max) or (search, none)"""
    tolerancy = input("Souhaitez-vous donner une valeur simple [S] ou bien indiquer une tolérance [T] ? ")

    if tolerancy == "S":
        number = input("Quel est le nombre recherché ? ")
        if "int" in type_column:
            searched_number = int(number)
        elif "float" in type_column:
            searched_number = float(number)
        return(searched_number, None)
    
    elif tolerancy == "T":
        number = input("Autour de quelle valeur souhaitez-vous effectuer la recherche ? ")
        searched_tolerancy = input("Avec une tolérance de combien ? ")
        if "int" in type_column:
            number = int(number)
            searched_tolerancy = int(searched_tolerancy)
            searched_number_min = number-searched_tolerancy
            searched_number_max = number+searched_tolerancy
        elif "float" in type_column:
            number = float(number)
            searched_tolerancy = float(searched_tolerancy)
            searched_number_min = number-searched_tolerancy
            searched_number_max = number+searched_tolerancy
        return(searched_number_min, searched_number_max)
    
    else:
        return()


def numericInterval(usedTable, column, type_column, cursor):
    """Giving the interval in which we are gonna search.
    Can handle between min and max of the searched column.
    Return (min, max)"""
    
    print("Vous avez la possibilité d'entrer 'min' (respectivement 'max') pour chercher toutes les données jusqu'à une certaine valeur (respectivement au-dessus d'une certaine valeur).")

    searched_min = input("Quelle est la valeur du minimun ? ")
    searched_max = input("Quelle est la valeur du maximum ? ")

    if "int" in type_column:
        if searched_min == "min":
            cursor.execute("SELECT MIN(%s) FROM %s;" % (column, usedTable))
            searched_min = cursor.fetchone()[0]
        
        else:
            try:
                searched_min = int(searched_min)
            except:
                print("Erreur de saisie, veuillez réessayer")
                return(numericInterval(usedTable, column, type_column, cursor))
        
        
        if searched_max == "max":
            cursor.execute("SELECT MAX(%s) FROM %s;" % (column, usedTable))
            searched_max = cursor.fetchone()[0]

        else:
            try:
                searched_max = int(searched_max)
            except:
                print("Erreur de saisie, veuillez réessayer")
                return(numericInterval(usedTable, column, type_column, cursor))
        
    
    elif "float" in type_column:
        if searched_min == "min":
            cursor.execute("SELECT MIN(%s) FROM %s;" % (column, usedTable))
            searched_min = cursor.fetchone()[0]
        
        else:
            try:
                searched_min = float(searched_min)
            except:
                print("Erreur de saisie, veuillez réessayer")
                return(numericInterval(usedTable, column, type_column, cursor))
        
        
        if searched_max == "max":
            cursor.execute("SELECT MAX(%s) FROM %s;" % (column, usedTable))
            searched_max = cursor.fetchone()[0]

        else:
            try:
                searched_max = float(searched_max)
            except:
                print("Erreur de saisie, veuillez réessayer")
                return(numericInterval(usedTable, column, type_column, cursor))

    return(searched_min, searched_max)


def selectColumnsToPrint(usedTable, sizeTable, namesColumns, columns):
    """Select the columns to print in the results of the query.
    Return the list of the selected columns"""
    selected_columns = []
    selected_names = []
    print("Choisissons les colonnes de résultat à afficher.")
    answer = input("Souhaitez-vous un affichage restreint [R], un affichage total [T] ou bien un affichage plus complexe [C] ? ")
    
    if answer == "R":
        for i in range (3, 6):
            selected_columns.append(columns[i])
            selected_names.append(namesColumns[i])
        return(selected_columns, selected_names)

    elif answer == "T":
        return(columns, namesColumns)

    elif answer == "C":
        print("Tapez Entrée pour afficher la colonne dans les résultats, n'importe quel autre caractère pour l'en exclure.")
        for nb in range(sizeTable):
            name = namesColumns[nb]
            if input(name + " ") == "":
                selected_columns.append(columns[nb])
                selected_names.append(name)
        return(selected_columns, selected_names)

    else:
        return(selectColumnsToPrint(usedTable, sizeTable, namesColumns, columns))


def prepareSQLRequestSimple(searched_one, searched_two, usedTable, selected_columns, column, type_column):
    """Write the SQL request with the values and the tuple of the columns we want to show.
    Return the SQL request as it has to be executed plus the number of columns to show"""

    if searched_two == None:
        
        if searched_one == None:
            return("error", 0)
        
        else:
            sizeRequest = len(selected_columns)
            sql = ["SELECT %s"]
            
            for i in range(sizeRequest-1):
                sql.append(", %s")
            
            if ("int" or "float") in type_column:
                sql.append(" FROM %s WHERE %s = '%s';" % (usedTable, column, searched_one))
            elif ("char" or "text" in type_column):
                # every "%" is needed in the line below because you have to escape two times (one in these request, and one when you execute it)
                # in order to execute correctly the sql request and to be able to search "searched_one" in the word, and not only as "searched_one"
                sql.append(" FROM %s WHERE %s LIKE '%%%%%s%%%%';" % (usedTable, column, searched_one))
            return(sql, sizeRequest)
    
    else:
        sizeRequest = len(selected_columns)
        sql = ["SELECT %s"]

        for i in range(sizeRequest-1):
            sql.append(", %s")
        
        if "date" in type_column:
            sql.append(" FROM %s WHERE %s BETWEEN '%s' AND '%s';" % (usedTable, column, searched_one, searched_two))
        else:
            sql.append(" FROM %s WHERE %s BETWEEN %d AND %d;" % (usedTable, column, searched_one, searched_two))
        
        return(sql, sizeRequest)


def prepareSQLRequestAdvanced(usedTable, selected_columns, searched):
    """Write the beginning and the full sql request with the selected columns and the end already written.
    Return (sql, sizeRequest)"""
    sizeRequest = len(selected_columns)
    sql = ["SELECT %s"]

    for i in range(sizeRequest-1):
        sql.append(", %s")

    sql.append(" FROM %s WHERE" % usedTable)

    for term in searched:
        sql.append(term)
    
    sql.append(";")
    return(sql, sizeRequest)


def searchDb(sql, selected_columns, cursor):
    """Try to execute the sql request.
    Return (results, description)"""
    
    try:
        request = cursor.execute("".join(sql) % tuple(selected_columns))
        print("\nNombre de résultats correspondant : %d" % request)
        results = cursor.fetchall()
        description = cursor.description

    except:
        print("".join(sql) % tuple(selected_columns))
        cursor.execute("SHOW WARNINGS;")
        warnings = cursor.fetchall()
        print("warnings : ", warnings)
    
    return(results, description, request)


def printResults(results, description, selected_names, sizeRequest, request):
    """Allow to print properly as a table the results"""
    # See doc PyMySQL for what is in description :
    # name    type_code    display_size    internal_size    precision    scale    null_ok
    lineHead = []
    titleHead = []
    length = []

    # Build the first row with the heads of the columns 
    for i in range (sizeRequest):
        head = selected_names[i]
        sizeDisplay = max(description[i][3], len(head))
        
        if sizeDisplay > 40:
            sizeDisplay = 40
        
        titleHead.append(head)
        lineHead.append(" {t[%d]:^%s} " % (i, sizeDisplay))
        length.append(sizeDisplay)
    
    lineHead = "".join(lineHead)
    print(lineHead.format(t=titleHead))

    # Build the table of results row after row
    for nb in range(request):
        line = []
        title = []
        truncated = []
        
        for i in range (sizeRequest):
            sizeDisplay = length[i]
            content = str(results[nb][i])
            sizeContent = len(content)

            if sizeContent >= sizeDisplay:
                title.append(content[0:sizeDisplay])
                truncated.append((results[nb], i, sizeContent))
            
            elif content == "None":
                content = ""
                title.append(content)
            
            else:
                title.append(content)
            
            line.append(" {t[%d]:^%s} " % (i, sizeDisplay))
        
        line = "".join(line)
        print(line.format(t=title))
    
    return(truncated, titleHead)


def wantToPrintTruncated():
    """Ask if the truncated lines have to be print or not.
    Return O or N."""
    return(input("Souhaitez-vous afficher en entier les lignes tronquées ? [O/N] "))


def printTruncated(truncated, titleHead, results, sizeRequest):
    """Print the truncated lines."""
    
    print("\nAffichage des lignes tronquées")
    # Print the title of each column
    
    lineHead = []
    length = []

    for i in range(sizeRequest):
        listForMax = []

        for row in truncated:
            if row[1] == i:
                listForMax.append(row[2])

        sizeMax = max(listForMax, default=0)
        sizeDisplay = max(len(titleHead[i]), sizeMax)
        
        if sizeDisplay < 12:
            sizeDisplay = 12
        
        lineHead.append(" {t[%d]:^%s} " % (i, sizeDisplay))
        length.append(sizeDisplay)
    
    lineHead = "".join(lineHead)
    print(lineHead.format(t=titleHead))

    # select the truncated lines
    toPrint = []
    for row in truncated:
        rowToPrint = row[0]
        
        if rowToPrint not in toPrint:
            toPrint.append(rowToPrint)

    # print the truncated lines
    for row in toPrint:
        line = []
        title = []
        
        for i in range (sizeRequest):
            sizeDisplay = length[i]
            content = str(row[i])

            if content == "None":
                content = ""
                title.append(content)
            
            else:
                title.append(content)
            
            line.append(" {t[%d]:^%s} " % (i, sizeDisplay))
        
        line = "".join(line)
        print("\n")
        print(line.format(t=title))

        return()   


