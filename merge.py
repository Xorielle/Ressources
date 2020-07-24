#! /usr/bin/python3
# -*- coding: utf-8 -*-

import pymysql
import Functions.connectionDb as conn
import Functions.delete as delete
import Functions.modifyRow as modify
import Functions.merge as fct


# Initialize users parameters and connection to DB
user_name, password, date = conn.parametersWithPass()
db, cursor = conn.connectionToDb(user_name, password=password)
authorized = conn.getAuthorizedTerms(cursor)

# Get the rows to merge
usedTable = fct.chooseTable()
id1, id2, answer = fct.haveIDs(usedTable, cursor)

if answer == "O":
    namesColumns, controlled = conn.getNamesOfColumns(usedTable, cursor)
    columns, type_columns, sizeTable = fct.getTableStructure(usedTable, cursor)
    row1, description1 = modify.returnRowToModify(id1, usedTable, cursor)
    row2, description2 = modify.returnRowToModify(id2, usedTable, cursor)
    new_values, old_values, entered_values = fct.getNewValues(row1, row2, namesColumns, sizeTable, controlled, authorized)
    values = fct.buildValues(new_values, entered_values, sizeTable)
    request = fct.buildSQLrequest(values, columns, sizeTable, usedTable, id1, date, user_name)
    modification = modify.executeModification(request, cursor, db)

    if modification:
        deletion = delete.delete(id2, usedTable, cursor, db)
        if deletion:
            print("La fusion a été effectuée correctement.")
        else:
            print("La modification a bien été enregistrée, mais il y a eu une erreur pendant la suppression. Retentez avec le programme dédié.")
    
    else:
        print("Il y a eu une erreur au cours de la modification de la première ligne. Fusion abandonnée.") 

else:
    print("Revenez avec les IDs !")

db.close()