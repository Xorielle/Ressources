#! /usr/bin/python3
# -*- coding: utf-8 -*-


import pymysql
import Functions.search as fct
import Functions.connectionDb as conn


# Initialize users parameters and connection to DB
user_name, date = conn.parameters()
db, cursor = conn.connectionToDb(user_name)

answer_abort = "O"

while answer_abort == "O":
    
    #Ask about the type of research and get the structure of the table
    search = fct.typeOfSearch()
    usedTable = fct.chooseTable()
    columns, type_columns, sizeTable = fct.getTableStructure(usedTable, cursor)

    if search == "S":

        # Ask about what is being searched
        column, type_column = fct.getColumnToSearch(columns, type_columns)
        searched_one, searched_two = fct.getSearchCriteria(usedTable, column, type_column, cursor)
        
        # Re-modelling to have the right sql request
        selected_columns = fct.selectColumnsToPrint(usedTable, sizeTable, columns)
        sql, sizeRequest = fct.prepareSQLRequestSimple(searched_one, searched_two, usedTable, selected_columns, column, type_column)

    elif search == "A":

        # Ask about what is being searched
        s_columns, s_type_columns, sizeRequest = fct.getColumnsToSearch(columns, type_columns, sizeTable)
        searched = fct.getSearchCriterias(usedTable, s_columns, s_type_columns, sizeRequest, cursor)

        # Finalizing the sql request
        selected_columns = fct.selectColumnsToPrint(usedTable, sizeTable, columns)
        sql, sizeRequest = fct.prepareSQLRequestAdvanced(usedTable, selected_columns, searched)


    # Print data
    try:
        results, description = fct.searchDb(sql, selected_columns, cursor)
        fct.printResults(results, description, sizeRequest)
    
    except:
        print("Votre requête n'a pas pu aboutir.")
        
    answer_abort = input("Souhaitez-vous continuer à consulter la base de données ? [O] pour continuer, toute autre touche pour quitter ")
    
print("Sortie de la BDD")

db.close()