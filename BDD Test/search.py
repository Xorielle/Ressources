#! /usr/bin/python3
# -*- coding: utf-8 -*-


import pymysql
import Functions.search as fct
import Functions.connectionDb as conn


# Initialize users parameters and connection to DB
user_name, date = conn.parameters()
db, cursor = conn.connectionToDb(user_name)


answer_abort = "O"

# TODO only simple search for the moment

while answer_abort == "O":
    # Ask about what is being searched
    usedTable = fct.chooseTable()
    columns, type_columns = fct.getColumns(usedTable, cursor)
    column, type_column = fct.getColumnToSearch(columns, type_columns)
    fct.getSearchRequest(usedTable, column, type_column)
    # Re-modelling to have a displayable information
    # Print data
    answer_abort = input("Souhaitez-vous continuer à consulter la base de données ? [O] pour continuer, toute autre touche pour quitter ")
    
print("Sortie de la BDD")

db.close()