#! /usr/bin/python3
# -*- coding: utf-8 -*-

import pymysql
import Functions.connectionDb as conn
import Functions.delete as delete
import Functions.modifyRow as modify
import Functions.merge as fct


# Initialize users parameters and connection to DB
user_name, date = conn.parameters()
db, cursor = conn.connectionToDb(user_name)

# Get the rows to merge
usedTable = fct.chooseTable()
id1, id2, answer = fct.haveIDs(usedTable, cursor)

if answer == "O":
    columns, type_columns, sizeTable = fct.getTableStructure(usedTable, cursor)
    row1, description1 = modify.returnRowToModify(id1, usedTable, cursor)
    row2, description2 = modify.returnRowToModify(id2, usedTable, cursor)
    new_values, old_values, entered_values = fct.getNewValues(row1, row2, columns, sizeTable)
    values = fct.buildValues(new_values, entered_values, sizeTable)
    request = fct.buildSQLrequest(values, columns, sizeTable, usedTable, id1, date, user_name)
    modification = modify.executeModification(request, cursor, db)
    deletion = delete.delete(id2, usedTable, cursor, db)
    
    if modification and deletion:
        print("La fusion a été effectuée correctement.")
    else:
        print("Il y a eu une erreur au cours de la fusion") # db.commit is executed after both functions. This may cause LOSS OF DATA.

else:
    print("Revenez avec les IDs !")

db.close()