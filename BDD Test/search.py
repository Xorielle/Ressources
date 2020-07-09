#! /usr/bin/python3
# -*- coding: utf-8 -*-


import pymysql
import Functions.search as fct
import Functions.connectionDb as conn


# Initialize users parameters and connection to DB
user_name, date = conn.parameters()
db, cursor = conn.connectionToDb(user_name)


answer_abort = "O"

# TODO only simple search for the moment, implement the advanced search

while answer_abort == "O":
    
    # Ask about what is being searched
    usedTable = fct.chooseTable()
    columns, type_columns, sizeTable = fct.getTableStructure(usedTable, cursor)
    column, type_column = fct.getColumnToSearch(columns, type_columns)
    searched_one, searched_two = fct.getSearchCriteria(usedTable, column, type_column)
    
    # Re-modelling to have the right sql request
    selected_columns = fct.selectColumnsToPrint(usedTable, sizeTable, columns)
    sql, sizeRequest = fct.prepareSQLRequest(searched_one, searched_two, usedTable, selected_columns, column, type_column)

    # Print data
    results, description = fct.searchDb(sql, selected_columns, cursor)
    fct.printResults(results, description, sizeRequest)
    
    answer_abort = input("Souhaitez-vous continuer à consulter la base de données ? [O] pour continuer, toute autre touche pour quitter ")
    
print("Sortie de la BDD")

db.close()