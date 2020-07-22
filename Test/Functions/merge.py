#! /usr/bin/python3
# -*- coding: utf-8 -*-

import pymysql

def chooseTable():
    """Choose wether we are merging in Materiaux or Pieces.
    Return usedTable"""
    table = input("Voulez-vous fusionner deux lignes qui sont dans les matériaux [M] ou dans les pièces [P] ? ")
    
    if table == "M": 
        return("Materiaux")
    
    if (table == "P"):
        return("Pieces")
    
    else:
        return(chooseTable())


def haveIDs(usedTable, cursor):
    """Verifying the user knows the ids of the row he wants to merge.
    Return the tuple (id1, id2, "O") or (None, None, "N")"""
    print("\nAttention : pour fusionner deux lignes, vous devez connaître leurs IDs exacts.") 
    print("Si ce n'est pas le cas, quittez ce programme et allez chercher les IDs grâce au programme de recherche.")
    answer = input("Connaissez-vous les IDs des lignes à fusionner ? [O/N] ")

    if answer == "O":
        
        try:
            id1 = int(input("Tapez l'ID de la première ligne : "))
            id2 = int(input("Tapez l'ID de la deuxième ligne : "))
            cursor.execute("SELECT MAX(id) FROM %s;" % usedTable)
            max_id = cursor.fetchone()[0]

            if (id1 > 0) and (id1 <= max_id) and (id2 > 0) and (id2 <= max_id) and (id1 != id2):
                return(id1, id2, answer)

            else:
                print("Les IDs saisis sont en-dehors des plages de valeur acceptées ou bien sont identiques, sortie du programme.")
                return(None, None, "N")

        except:
            print("Les IDs saisis sont incorrects, sortie du programme.")
            return(None, None, "N")
    
    else:
        print("Sortie du programme.")
        return(None, None, "N")


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


def getNewValues(row1, row2, namesColumns, sizeTable):
    """Print the rows to merge. 
    Simultaneously returns the inputs to change (new_values, old_values, entered_values)"""
    print("\nVoici une proposition de fusion. Si celle-ci vous convient, tapez entrée.")
    print("A titre indicatif, le contenu de la deuxième ligne est affiché entre parenthèses, mais n'apparaîtra pas dans le tableau.")
    print("Sinon, si vous souhaitez changer la valeur par défaut, entrez simplement la nouvelle valeur.")
    new_values = []
    old_values = []
    entered_values = []
    
    for nb in range(3, sizeTable):
        actual_value1 = row1[nb]
        actual_value2 = row2[nb]

        if actual_value1 == None:
            
            if actual_value2 == None:
                new_value = ""
                old_value = ""
                print(namesColumns[nb] + " : ")

            else:
                new_value = str(actual_value2)
                old_value = ""
                print(namesColumns[nb] + " : " + new_value)
        
        else:
            
            if actual_value2 == None:
                new_value = str(actual_value1)
                old_value = ""
                print(namesColumns[nb] + " : " + new_value)
            elif actual_value2 == actual_value1:
                new_value = str(actual_value1)
                old_value = str(actual_value2)
                print(namesColumns[nb] + " : " + new_value)
            else:
                new_value = str(actual_value1)
                old_value = str(actual_value2)
                print(namesColumns[nb] + " : " + new_value + "       (" + old_value + ")")


        entered_values.append(input("? "))
        new_values.append(new_value)
        old_values.append(old_value)

    return(new_values, old_values, entered_values)


def buildValues(new_values, entered_values, sizeTable):
    """Return the final list of values (each value can be either a string or None)."""
    values = []
    
    for nb in range(sizeTable-3):
        entered_value = entered_values[nb]
        
        if entered_value == "":
            new_value = new_values[nb]
            if new_value == "":
                value = None
            else:
                value = new_value
        
        else:
            value = entered_value
    
        values.append(value)
    
    return(values)


def buildSQLrequest(values, columns, sizeTable, usedTable, id1, date, user_name):
    """Build the SQL request to merge the rows.
    Deals now with Null values.
    Return SQL request as a string"""
    sql = []
    sql.append("UPDATE %s SET %s = '%s', %s = '%s'" % (usedTable, columns[1], date, columns[2], user_name) ) 
    
    for nb in range(sizeTable-3):
        value = values[nb]
        
        if value == None:
            sql.append(", %s = NULL" % columns[nb+3])

        else:
            sql.append(", %s = '%s'" % (columns[nb+3], value))

    sql.append(" WHERE id = %d;" % id1)
    request = "".join(sql)
    return(request)
