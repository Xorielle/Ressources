#! /usr/bin/python3
# -*- coding: utf-8 -*-


import pymysql


def chooseTable():
    """Choose wether we are searching in Materiaux or Pieces
    Return usedTable"""
    table = input("Voulez-vous effectuer une recherche parmi les matériaux [M] ou les pièces [P] ? ")
    
    if table == "M": 
        return("Materiaux")
    
    if (table == "P"):
        return("Pieces")
    
    else:
        return(chooseTable())


def getColumns(usedTable, cursor):
    """Create the list of all columns/criterias in the table
    Return columns, type_column"""
    columns = []
    type_columns = []
    cursor.execute("DESCRIBE %s;" % usedTable)
    description = cursor.fetchall()
    
    for row in description:
        columns.append(row[0])
        type_columns.append(row[1])
    
    return(columns, type_columns)


def getColumnToSearch(columns, type_columns):
    """Ask in which column (that means wich criteria) the user wants to search
    Return searched_column, type_column"""
    print("Dans quelle colonne souhaitez-vous effectuer une recherche ? Tapez Entrée jusqu'à arriver à la colonne souhaitée, puis tapez n'importe quelle touche pour cette colonne-ci.")
    answer = ""
    nb = 0

    while answer == "":
        answer = input(columns[nb] + " ? ")
        nb += 1
    
    return(columns[nb-1], type_columns[nb-1])



def getSearchRequest(usedTable, column, type_column):
    """Ask which criteria is searched in the column
    Return the tuple (criteria, none) or (min, max) or (none, none) if error"""

    if ("char" or "text") in type_column:
        criteria = input("Quel terme souhaitez-vous chercher dans la colonne %s ? " % column)
        return(criteria, None)
    
    elif ("int" or "float") in type_column:
        searchMode = input("Effectuer une recherche numérique simple [S] ou bien une recherche sur un intervalle [I] ? ")    
        if searchMode == "S":
            return(numericSimple(type_column))
        elif searchMode == "I":
            return(numericInterval(type_column))
        else:
            return(getSearchRequest(usedTable, column, type_column))
    
    else:
        print("Il n'est pas possible d'effectuer de recherche sur cette colonne.")
        return(None, None)


def numericSimple(type_column):
    """Numeric search with the possibility of adding a tolerancy
    Return (min, max) or (search, none)"""
    tolerancy = input("Souhaitez-vous donner une valeur simple [S] ou bien indiquer une tolérance [T] ? ")

    if tolerancy == "S":
        number = input("Quel est le nombre recherché ? ")
        if "int" in type_column:
            searched_number = int(number)
        elif "float" in type_column:
            searched_number = float(number)
        return(searched_number, None)
    
    elif tolerancy == "T":
        number = input("Autour de quelle valeur souhaitez-vous effectuer la recherche ? ")
        searched_tolerancy = input("Avec une tolérance de combien ? ")
        if "int" in type_column:
            number = int(number)
            searched_tolerancy = int(searched_tolerancy)
            searched_number_min = number-searched_tolerancy
            searched_number_max = number+searched_tolerancy
        elif "float" in type_column:
            number = float(number)
            searched_tolerancy = float(searched_tolerancy)
            searched_number_min = number-searched_tolerancy
            searched_number_max = number+searched_tolerancy
        return(searched_number_min, searched_number_max)
    
    else:
        return()


def numericInterval(type_column):
    """Giving the interval in which we are gonna search
    Return (min, max)"""
    
    if "int" in type_column:
        searched_min = int(input("Quelle est la valeur du minimum ? "))
        searched_max = int(input("Quelle est la valeur du maximum ? "))
    
    elif "float" in type_column:
        searched_min = float(input("Quelle est la valeur du minimum ? "))
        searched_max = float(input("Quelle est la valeur du maximum ? "))
    
    return(searched_min, searched_max)


def searchDb(sql):
    """Try to execute the sql request"""
