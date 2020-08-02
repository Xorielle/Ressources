#! /usr/bin/python3
# -*- coding: utf-8 -*-


import pymysql
import Functions.search as fct
import Functions.connectionDb as conn
import Functions.scroll as scr


# Initialize users parameters and connection to DB
user_name, date = conn.parametersWithoutPass()
db, cursor = conn.connectionToDb(user_name)
authorized = conn.getAuthorizedTerms(cursor)

answer_abort = "O"

while answer_abort == "O":
    
    #Ask about the type of research and get the structure of the table
    search = fct.typeOfSearch()
    usedTable = fct.chooseTable()
    namesColumns, controlled, units, categories = conn.getNamesOfColumns(usedTable, cursor)
    columns, type_columns, sizeTable = fct.getTableStructure(usedTable, cursor)

    if search == "S":

        # Ask about what is being searched
        nameColumn, column, type_column, unit = fct.getColumnToSearch(namesColumns, units, columns, type_columns)
        searched_one, searched_two = fct.getSearchCriteria(usedTable, column, type_column, cursor)
        
        # Re-modelling to have the right sql request
        selected_columns, selected_names, selected_units = fct.selectColumnsToPrint(usedTable, sizeTable, namesColumns, units, columns)
        sql, sizeRequest = fct.prepareSQLRequestSimple(searched_one, searched_two, usedTable, selected_columns, column, type_column)

    elif search == "A":

        # Ask about what is being searched
        s_names, s_columns, s_type_columns, s_units, sizeRequest = fct.getColumnsToSearch(namesColumns, units, columns, type_columns, sizeTable)
        searched = fct.getSearchCriterias(usedTable, s_names, s_columns, s_type_columns, s_units, sizeRequest, cursor)

        # Finalizing the sql request
        selected_columns, selected_names, selected_units = fct.selectColumnsToPrint(usedTable, sizeTable, namesColumns, units, columns)
        sql, sizeRequest = fct.prepareSQLRequestAdvanced(usedTable, selected_columns, searched)


    # Print data
    try:
        results, description, request = fct.searchDb(sql, selected_columns, cursor)
        print("La recherche a abouti.")
        #truncated, titleHead, titleUnit = fct.printResults(results, description, selected_names, selected_units, sizeRequest, request)
        truncated, titleHead, titleUnit = scr.printResultsWindow(sizeRequest, selected_names, selected_units, description, results, request)

        if truncated != []:
            answer = fct.wantToPrintTruncated()
            while answer != "N":
                if answer == "O":
                    scr.printTruncated(truncated, titleHead, titleUnit, results, description, sizeRequest)
                    answer = "N"

                else:
                    answer = fct.wantToPrintTruncated()
    except:
        print("Votre requête n'a pas pu aboutir.")
        
    answer_abort = input("\nSouhaitez-vous continuer à consulter la base de données ? [O] pour continuer, toute autre touche pour quitter ")
    
print("Sortie de la BDD")

db.close()