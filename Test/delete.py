#! /usr/bin/python3
# -*- coding: utf-8 -*-

import pymysql
import Functions.connectionDb as conn
import Functions.delete as fct


# Initialize users parameters and connection to DB
user_name, date = conn.parameters()
db, cursor = conn.connectionToDb(user_name)

# Get the row we want to modify
usedTable = fct.chooseTable()
suppressed_id, answer = fct.haveID(usedTable, cursor)

if answer == "O":
    fct.delete(suppressed_id, usedTable, cursor, db)

else:
    print("Revenez avec un ID !")

db.close()
