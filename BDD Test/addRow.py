#! /usr/bin/python3

import pymysql
import datetime
import functions_addRow as f

# Initialize users parameters and connection to DB
user_name, date = f.parameters()
db, cursor = f.connectionToDb(user_name)


# Ask about what will be added
usedTable = f.chooseTable()
columns, type_column, sizeTable = f.getTableStructure(usedTable)
raw_row_input = f.getRowInformation(usedTable, date, user_name, sizeTable, columns)


# Re-modelling to have the right information
row_input = f.verifyRowSyntaxes(raw_row_input, sizeTable, columns)
answer = f.userConfirmation(usedTable)

if answer == 'O':
    sql_command = f.prepareSQLRequest(sizeTable)

else:
    print("mauvaise entrée")
    # TODO Mettre en place le retour sans avoir à tout retaper


# Add the row in the db
f.addingRowInDb(usedTable, sql_command, row_input)


db.close()