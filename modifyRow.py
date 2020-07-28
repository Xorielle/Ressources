#! /usr/bin/python3
# -*- coding: utf-8 -*-


import pymysql
import Functions.connectionDb as conn
import Functions.modifyRow as fct


# Initialize users parameters and connection to DB
user_name, password, date = conn.parametersWithPass()
db, cursor = conn.connectionToDb(user_name, password=password)
authorized = conn.getAuthorizedTerms(cursor)

# Get the row we want to modify
usedTable = fct.chooseTable()
modify_id, answer = fct.haveID(usedTable, cursor)

if answer == "O":
    namesColumns, controlled, units = conn.getNamesOfColumns(usedTable, cursor)
    columns, type_columns, sizeTable = fct.getTableStructure(usedTable, cursor)
    row_initial, description = fct.returnRowToModify(modify_id, usedTable, cursor)
    new_values = fct.printRowToModify(row_initial, namesColumns, sizeTable, controlled, units, authorized)
    request = fct.buildSQLrequest(usedTable, modify_id, new_values, user_name, date, sizeTable, columns)
    fct.executeModification(request, cursor, db)

else:
    print("Revenez avec un ID !")

db.close()