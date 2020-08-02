#! /usr/bin/python3
# -*- coding: utf-8 -*-


import pymysql


def introduction():
    print("\nAttention, vous entrez dans la matrice. Soyez sûrs de ce que vous faites, ou passez votre chemin. \
        \n Il vous est d'ailleurs conseillé d'effectuer une backup avant de continuer à arpenter les méandres \
de ces lieux, à trifouiller les tréfonds obscurs qui s'offrent à vous, à vous immerger dans ces sombres reco...\
Bref, venons-en aux faits.")
    answer = input("Etes-vous sûr de vouloir continuer ? [O/N] ")
    if answer == "O":
        return(True)
    elif answer == "N":
        return(False)
    else:
        return(introduction())

    
def chooseModificationType():
    print("Quel type de modification souhaitez-vous effectuer ?")
    modificationType = input("Ajouter une colonne [A], supprimer une colonne [S], modifier une colonne existante [M] ? ")
    if (modificationType != "A") and (modificationType != "S") and (modificationType != "M"):
        print("Concentrez-vous, vous allez faire des bêtises sinon !")
        return(chooseModificationType())
    return(modificationType)


def chooseTable():
    table = input("Souhaitez-vous effectuer cette modification parmi les Matériaux [M] ou les Pièces [P] ? ")
    if table == "M":
        usedTable = "Materiaux"
        supportTable = "NameMateriaux"
    elif table == "P":
        usedTable = "Pieces"
        supportTable = "NamePieces"
    else:
        print("Concentrez-vous, c'est sérieux !")
        return(chooseTable())
    return(usedTable, supportTable)


def getNamesOfColumns(usedTable, cursor):
    """Get four lists : namesColumns, controlled, units, categories."""
    namesColumns = []
    controlled = []
    units = []
    categories = []

    cursor.execute("SELECT * FROM Name%s;" % usedTable)
    
    names = cursor.fetchone()
    for name in names:
        namesColumns.append(name)

    constraints = cursor.fetchone()
    for constraint in constraints:
        controlled.append(constraint)

    units_table = cursor.fetchone()
    for unit in units_table:
        units.append(unit)

    categories_table = cursor.fetchone()
    for category in categories_table:
        categories.append(category)

    return(namesColumns, controlled, units, categories)


def getTableStructure(usedTable, cursor):
    """Return the title of the columns, the type of data and the number of columns"""
    cursor.execute('DESCRIBE %s;' % usedTable)
    description = cursor.fetchall()
    columns = []
    type_columns = []
    default_columns = []

    for row in description:
        columns.append(row[0])
        type_columns.append(row[1])
        default_columns.append(row[4])
    sizeTable = len(columns)

    return(columns, type_columns, sizeTable, default_columns)


def getColumnToDelete(namesColumns):
    print("Choisissez la colonne à supprimer. Pour cela, tapez entrée jusqu'à arriver à la colonne que vous souhaitez supprimer. \
Pour cette colonne, tapez n'importe quelle touche.")
    inp = ""
    i = 0
    while inp == "":
        name = namesColumns[i]
        inp = input(name + " ")
        i += 1
    return(sureToDelete(name, i-1, namesColumns))


def sureToDelete(name, name_id, namesColumns):
    answer = input("Vous vous apprêtez à supprimer la colonne %s. Êtes-vous sûr de votre choix ? [O/N] " % name)
    if answer == "O":
        return(name_id)
    elif answer == "N":
        return(getColumnToDelete(namesColumns))
    else:
        return(sureToDelete(name, name_id, namesColumns))


def buildSQLDelete(usedTable, supportTable, name_id, used_titles):
    """With this way of doing, id cannot be deleted because the column is named id and not n_id"""
    name = used_titles[name_id]
    request1 = "ALTER TABLE %s DROP COLUMN %s;" % (usedTable, name)
    request2 = "ALTER TABLE %s DROP COLUMN n_%s;" % (supportTable, name)
    return(request1, request2)


def buildList_categories(categories):
    list_categories = []
    for category in categories:
        if (category not in list_categories) and (category != None):
            list_categories.append(category)
    return(list_categories)


def getAddingData(usedTable, list_categories):
    print("Vous souhaitez donc ajouter une colonne à la table %s." % usedTable)
    print("Merci de répondre à ce petit questionnaire, temps estimé trois minutes.")
    print("Merci de respecter strictement la syntaxe imposée pour éviter tout problème ultérieur. \
En cas de besoin, référez-vous au paragraphe correspondant du manuel.")
    
    newName = input("Donnez un nom à votre colonne : ")
    newTitle = input("/!\\ Syntaxe /!\\ Donnez-lui son titre : ")
    newType = input("/!\\ Syntaxe /!\\ Donnez-lui son type : ")
    newUnit = input("Donnez-lui son unité, si elle en a une : ")
    newDefault = input("Donnez-lui sa valeur par défaut, si elle en a une : ")
    
    if newUnit == "":
        newUnit = None
    if newDefault == "":
        newDefault = None
    
    newControlled = input("Doit-elle accepter uniquement les termes autorisés ? [O/N] ")
    
    if newControlled == "O":
        newControlled = "True"
    elif newControlled == "N":
        newControlled = "False"
    else:
        print("Vous avez fait une erreur de saisie, merci de recommencer depuis le début.")
        return(getAddingData(usedTable, list_categories))
    
    print("Voici les catégories d'affichage déjà existantes : ")
    print(list_categories)
    newCategory = input("Dans quelle catégorie doit-elle s'afficher ? ")
    supportTitle = "n_" + newTitle
    return(newName, newTitle, supportTitle, newType, newUnit, newDefault, newControlled, newCategory)
    

def buildSQLAdd(usedTable, supportTable, newName, newTitle, supportTitle, newType, newUnit, newDefault, newControlled, newCategory):
    #Create the new column in main table
    if newDefault != None:
        request1 = """ALTER TABLE %s ADD %s %s DEFAULT="%s";""" % (usedTable, newTitle, newType, newDefault)
    else:
        request1 = "ALTER TABLE %s ADD %s %s;" % (usedTable, newTitle, newType)
    #Create the new column in NameTable for metadata
    request2 = "ALTER TABLE %s ADD %s VARCHAR(32);" % (supportTable, supportTitle)
    #Create the requests to fill the metadatas
    if supportTitle == "NameMateriaux":
        supportColumn = "n_m_date"
    elif supportTitle == "NamePieces":
        supportColumn = "n_p_date"
    request3 = """UPDATE %s SET %s = "%s" WHERE %s = 'Date de modification';""" %(supportTable, supportTitle, newName, supportColumn)
    request4 = "UPDATE %s SET %s = '%s' WHERE %s = 'False';" %(supportTable, supportTitle, newControlled, supportColumn)
    if newUnit != None:
        request5 = """UPDATE %s SET %s = "%s" WHERE %s = NULL;""" %(supportTable, supportTitle, newUnit, supportColumn)
    request6 = """UPDATE %s SET %s = '%s' WHERE %s = 'métadonnées';""" %(supportTable, supportTitle, newCategory, supportColumn)