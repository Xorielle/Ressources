#! /usr/bin/python3

# TODO codage utf8 (python + mysql)


import pymysql
import datetime


def parameters():
    """Fetch the username and the date
    Return (user_name, date)"""
    user_name = input('Qui utilise la BDD ? ')
    full_date = datetime.datetime.now()
    date = "%s-%s-%s" % (full_date.strftime("%Y"), full_date.strftime("%m"), full_date.strftime("%d"))
    print("Date du jour : ", date)
    
    return(user_name, date)


def connectionToDb(username, host = "localhost", db_name = "TestDB", password = ""):
    """Connect to the DB and get the access
    Return (db, db.cursor())"""
    db = pymysql.connect(host,username,password,db_name)
    return(db, db.cursor())


def chooseTable():
    """Choose if we are working with Pieces or with Materiaux
    Return usedTable as Materiaux or Pieces"""
    usedTable = input('Ajouter à la table Matériaux [M] ou à la table Pièces [P] ? ')
    assert usedTable=='M' or usedTable=='P', 'Erreur de saisie, entrer M ou P en majuscule'
    
    if (usedTable == 'M'):
        usedTable = 'Materiaux'
        print('Ajoutons une ligne à la table des Matériaux')
    
    elif (usedTable == 'P'):
        usedTable = 'Pieces'
        print('Ajoutons une ligne à la table des Pièces')
    
    return(usedTable)


def getTableStructure(usedTable, cursor):
    """Return the title of the columns, the type of data and the number of columns"""
    cursor.execute('DESCRIBE %s;' % usedTable)
    description = cursor.fetchall()
    columns = []
    type_column = []

    for row in description:
        columns.append(row[0])
        type_column.append(row[1])
    sizeTable = len(columns)

    return(columns, type_column, sizeTable)


def getRowInformation(usedTable, date, user_name, sizeTable, columns, cursor):
    """Get the information about the row we want to add in the table
    Return raw_row_input"""
    cursor.execute("""SELECT MAX(id) FROM %s;""" % usedTable)
    last_id = cursor.fetchone()
    raw_row_input = [last_id[0]+1, date, user_name] # Those have to be the same beginning in Materiaux as in Pieces

    for column in range(3, sizeTable):
        raw_row_input.append(input(columns[column] + " "))
    
    return(raw_row_input)


def verifyRowSyntaxes(raw_row_input, sizeTable, columns):
    """Check the syntax of the row is able to be understood by sql, and make the changes if needed
    Return row_input as needed by MySQL"""
    row_input = []
    
    for column in range (0, sizeTable):
        column_data = raw_row_input[column]
        print("\n", columns[column], column_data)
        if column_data == "":
            row_input.append(None)
        else:
            row_input.append(column_data)
    
    return(row_input)


def userConfirmation(usedTable):
    """Ask the user if the data he wrote are correct
    Return O or N"""
    print('\nEst-ce que les données ci-dessus à ajouter à la table ' + usedTable + ' sont correctes ?')
    answer = input ('Oui [O] ou Non [N] ? ')
    assert answer == 'O' or answer == 'N', 'Entrer O ou N en majuscule'
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
    
    return()
