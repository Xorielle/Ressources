#! /usr/bin/python3
# -*- coding: utf-8 -*-


import pymysql


def chooseTable():
    """Choose wether we are modifying in Materiaux or Pieces.
    Return usedTable"""
    table = input("Voulez-vous modifier une ligne parmi les matériaux [M] ou les pièces [P] ? ")
    
    if table == "M": 
        return("Materiaux")
    
    if (table == "P"):
        return("Pieces")
    
    else:
        return(chooseTable())


def haveID(usedTable, cursor):
    """Verifying the user knows the id of the row he wants to modify
    Return the tuple (id, "O") or (None, "N")"""
    print("Attention : pour modifier une ligne, vous devez connaître son ID exact.") 
    print("Si ce n'est pas le cas, quittez ce programme et allez chercher l'ID grâce au programme de recherche.")
    answer = input("Connaissez-vous l'ID de la ligne à modifier ? [O/N] ")

    if answer == "O":
        
        try:
            modify_id = int(input("Tapez l'ID : "))
            cursor.execute("SELECT MAX(id) FROM %s;" % usedTable)
            max_id = cursor.fetchone()[0]

            if (modify_id > 0) and (modify_id <= max_id):
                return(modify_id, answer)

            else:
                print("L'ID saisi est en-dehors des plages de valeur acceptées, sortie du programme.")
                return(None, "N")

        except:
            print("L'ID saisi est incorrect, sortie du programme.")
            return(None, "N")
    
    else:
        print("Sortie du programme.")
        return(None, "N")


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


def returnRowToModify(modify_id, usedTable, cursor):
    """Gets the information the row with corresponding ID.
    Returns (row_initial, description)"""
    try:
        cursor.execute("SELECT * FROM %s WHERE id = %d;" % (usedTable, modify_id))
        row_initial = cursor.fetchone()
        description = cursor.description

    except:
        print("SELECT * FROM %s WHERE id = %d;" % (usedTable, modify_id))
        cursor.execute("SHOW WARNINGS;")
        warnings = cursor.fetchall()
        print("warnings : ", warnings)
    
    return(row_initial, description)


def printRowToModify(row_initial, namesColumns, sizeTable, controlled, authorized):
    """Print the row with corresponding ID. Simultaneously returns the inputs to change"""
    print("Si vous souhaitez changer la valeur indiquée, entrez simplement la nouvelle valeur.")
    print("Si vous souhaitez remplacer la valeur actuelle par une case vide, rentrez NULL.")
    new_values = []
    
    nb = 3
    while nb < sizeTable:
        actual_value = row_initial[nb]

        if actual_value == None:
            actual_value = ""
        
        print(namesColumns[nb] + " : " + str(actual_value))
        new_value = input("? ")

        if controlled[nb] == "True":
            if new_value.lower() in authorized:
                new_values.append(new_value)
                nb += 1
            else:
                print("\nCette valeur n'est pas autorisée. Vérifiez l'orthographe et les accents.")
                print("Si l'orthographe et l'accentuation sont corrects, le terme que vous souhaitez entrer n'est pas dans le tableau des termes autorisés.")
                print("Quittez ce programme, ajoutez-le puis revenez.")
                print("Sinon, vous avez la possibilité de le modifier ci-dessous pour l'écrire correctement.\n")

        else:
            new_values.append(new_value)
            nb += 1

    return(new_values)


def buildSQLrequest(usedTable, modify_id, new_values, user_name, date, sizeTable, columns):
    """Build the SQL request to update the DB.
    Return SQL request as a string"""
    sql = []
    sql.append("UPDATE %s SET %s = '%s', %s = '%s'" % (usedTable, columns[1], date, columns[2], user_name) ) 
    
    for nb in range(sizeTable-3):
        value = new_values[nb]
        
        if value == "NULL":
            sql.append(", %s = NULL" % columns[nb+3])
        
        elif value != "":
            sql.append(", %s = '%s'" % (columns[nb+3], value))

    sql.append(" WHERE id = %d;" % modify_id)
    request = "".join(sql)
    return(request)


def executeModification(request, cursor, db):
    """"""
    try:
        cursor.execute(request)
        db.commit()
        print("La modification de la ligne a bien été enregistrée.")
        return(True)

    except:
        print("Une erreur est survenue lors de la modification. Cette dernière n'a pas été enregistrée.")
        cursor.execute("SHOW WARNINGS;")
        warnings = cursor.fetchall()
        print("warnings : ", warnings)
        return(False)