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
        selected_columns, selected_names, selected_units = fct.selectColumnsToPrint(usedTable, sizeTable, namesColumns, units, categories, columns)
        sql, sizeRequest = fct.prepareSQLRequestSimple(searched_one, searched_two, usedTable, selected_columns, column, type_column)

    elif search == "A":

        # Ask about what is being searched
        if usedTable == "Pieces": # Ask if jointure or not if the selected table is Pieces.
            jointure = fct.useJointure()
            if jointure == "O":
                print("\nCommençons par les critères de recherche sur la table des pièces.")
                s_names_p, s_columns_p, s_type_columns_p, s_units_p, sizeRequest_p = fct.getColumnsToSearch(namesColumns, units, columns, type_columns, sizeTable)
                searched = fct.getSearchCriterias(usedTable, s_names_p, s_columns_p, s_type_columns_p, s_units_p, sizeRequest_p, cursor)
                print("\nAjoutons maintenant les criètere de recherche que le matériau dont est composé la pièce doit remplir.")
                namesColumns_m, controlled_m, units_m, categories_m = conn.getNamesOfColumns("Materiaux", cursor)
                columns_m, type_columns_m, sizeTable_m = fct.getTableStructure("Materiaux", cursor)
                s_names_m, s_columns_m, s_type_columns_m, s_units_m, sizeRequest_m = fct.getColumnsToSearch(namesColumns_m, units_m, columns_m, type_columns_m, sizeTable_m)
                searched_m = fct.getSearchCriterias("Materiaux", s_names_m, s_columns_m, s_type_columns_m, s_units_m, sizeRequest_m, cursor)

            elif jointure == "N":
                s_names, s_columns, s_type_columns, s_units, sizeRequest = fct.getColumnsToSearch(namesColumns, units, columns, type_columns, sizeTable)
                searched = fct.getSearchCriterias(usedTable, s_names, s_columns, s_type_columns, s_units, sizeRequest, cursor)
        
        elif usedTable == "Materiaux":
            jointure = "N"
            s_names, s_columns, s_type_columns, s_units, sizeRequest = fct.getColumnsToSearch(namesColumns, units, columns, type_columns, sizeTable)
            searched = fct.getSearchCriterias(usedTable, s_names, s_columns, s_type_columns, s_units, sizeRequest, cursor)

        # Finalizing the sql request
        selected_columns, selected_names, selected_units = fct.selectColumnsToPrint(usedTable, sizeTable, namesColumns, units, categories, columns)
        if jointure == "N":
            sql, sizeRequest = fct.prepareSQLRequestAdvanced(usedTable, selected_columns, searched)
        elif jointure == "O":
            selected_columns = fct.renameId(selected_columns)
            sql, sizeRequest = fct.prepareSQLRequestAdvancedWithJointure(selected_columns, searched, searched_m)

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