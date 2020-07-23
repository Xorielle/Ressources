#! /usr/bin/python3
# -*- coding: utf-8 -*-


import pymysql
import datetime


def chooseTable():
    """Choose if we are working with Pieces or with Materiaux
    Return usedTable as Materiaux or Pieces"""
    usedTable = input('Ajouter à la table Matériaux [M] ou à la table Pièces [P] ? ')
    
    if (usedTable == 'M'):
        usedTable = 'Materiaux'
        print('Ajoutons une ligne à la table des Matériaux')
    
    elif (usedTable == 'P'):
        usedTable = 'Pieces'
        print('Ajoutons une ligne à la table des Pièces')

    else:
        print("Erreur de saisie, entrer M ou P en majuscule.")
        return(chooseTable())
    
    return(usedTable)


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


def getRowInformation(usedTable, date, user_name, sizeTable, namesColumns, controlled, authorized, cursor):
    """Get the information about the row we want to add in the table
    Return raw_row_input"""
    cursor.execute("""SELECT MAX(id) FROM %s;""" % usedTable)
    last_id = cursor.fetchone()

    if last_id[0] == None:
        last_id[0] = 0

    raw_row_input = [last_id[0]+1, date, user_name] # Those have to be the same beginning in Materiaux as in Pieces

    column = 3
    while column < sizeTable:
        toAdd = input(namesColumns[column] + " ")
        if controlled[column] == "True":
            if toAdd in authorized:
                raw_row_input.append(toAdd)
                column += 1
            else:
                print("\nCette valeur n'est pas autorisée. Vérifiez l'orthographe et la casse.")
                print("Si l'orthographe et la casse sont corrects, le terme que vous souhaitez entrer n'est pas dans le tableau des termes autorisés.")
                print("Quittez ce programme, ajoutez-le puis revenez.")
                print("Sinon, vous avez la possibilité de le modifier ci-dessous pour l'écrire correctement.\n")

        else:
            raw_row_input.append(toAdd)
            column += 1
    
    return(raw_row_input)


def modifyRowInformation(row_input, sizeTable, nameColumns, controlled, authorized):
    """Modify the information of the row we want to add without having to retype all from the beginning
    Return raw_row_input"""
    print("Pour modifier une ligne, taper les valeurs voulues. Pour laisser la ligne inchangée, taper Entrée")
    
    column = 3
    while column < sizeTable:
        column_data = row_input[column]
        replacing_data = input("\n%s : %s " % (nameColumns[column], str(column_data)))
        
        if replacing_data != "": 
            if controlled[column] == "True":
                if replacing_data in authorized:
                    row_input[column] = replacing_data
                    column += 1
                else:
                    print("\nCette valeur n'est pas autorisée. Vérifiez l'orthographe et la casse.")
                    print("Si l'orthographe et la casse sont corrects, le terme que vous souhaitez entrer n'est pas dans le tableau des termes autorisés.")
                    print("Quittez ce programme, ajoutez-le puis revenez.")
                    print("Sinon, vous avez la possibilité de le modifier ci-dessous pour l'écrire correctement.\n")

            else:
                row_input[column] = replacing_data
                column += 1
    
    return(row_input)


def verifyRowSyntaxes(raw_row_input, sizeTable, nameColumns, default_column):
    """Check the syntax of the row is able to be understood by sql, and make the changes if needed
    Return row_input as needed by MySQL"""
    row_input = []
    
    for column in range (0, sizeTable):
        column_data = raw_row_input[column]
        print("\n", nameColumns[column], " : ", column_data)
        if column_data == "":
            default = default_column[column]
            if default != "":
                row_input.append(default)
            else: 
                row_input.append(None)
        else:
            row_input.append(column_data)
    
    return(row_input)


def userConfirmation(usedTable):
    """Ask the user if the data he wrote are correct
    Return O or N"""
    print('\nEst-ce que les données ci-dessus à ajouter à la table ' + usedTable + ' sont correctes ?')
    answer = input ('Oui [O] ou Non [N] ? ')
    return(answer)


def prepareSQLRequest(sizeTable):
    """Prepare the SQL request to add the row (but wasn't the name clear enough ?)
    Return SQL request"""
    sql_command = ["(%s"]
    
    for nb in range(1, sizeTable):
        sql_command.append(", %s")
    
    sql_command.append(");")
    return(sql_command)


def addingRowInDb(usedTable, sql_command, row_input, cursor, db):
    """Try to add the row in the DB if possible. If not, print the warning and rollback"""

    try:
        cursor.execute("INSERT INTO %s VALUES " % usedTable + "".join(sql_command), tuple(row_input))
        print("Ligne ajoutée")
        db.commit()
        print("BDD mise à jour avec succès")

    except:
        cursor.execute("SHOW WARNINGS;")
        warnings = cursor.fetchall()
        print("warnings : ", warnings)
        db.rollback()
        return("error")

    
    return()
