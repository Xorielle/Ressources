#! /usr/bin/python3
# -*- coding: utf-8 -*-


import pymysql
import Functions.connectionDb as conn
import Functions.modifyRow as fct


# Initialize users parameters and connection to DB
user_name, date = conn.parameters()
db, cursor = conn.connectionToDb(user_name)

usedTable = fct.chooseTable()

modify_id, answer = fct.haveID(usedTable, cursor)

if answer == "O":
    columns, type_columns, sizeTable = fct.getTableStructure(usedTable, cursor)
    row_initial, description = fct.returnRowToModify(modify_id, usedTable, cursor)
    fct.printRowToModify(row_initial, columns, sizeTable)


else:
    print("Revenez avec un ID !")

db.close()