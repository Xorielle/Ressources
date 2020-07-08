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
    Return columns"""
    columns = []
    cursor.execute("DESCRIBE %s;" % usedTable)
    description = cursor.fetchall()
    
    for row in description:
        columns.append(row[0])
    
    return(columns)


def getColumnToSearch(columns):
    """Ask in which column (that means wich criteria) the user wants to search
    Return searched_column"""
    print("Dans quelle colonne souhaitez-vous effectuer une recherche ? Tapez Entrée jusqu'à arriver à la colonne souhaitée, puis tapez n'importe quelle touche pour cette colonne-ci.")
    answer = ""
    nb = 0

    while answer == "":
        answer = input(columns[nb] + " ? ")
        nb += 1
    
    return(columns[nb-1])



def getSearchTerm(usedTable):
    """TODO Ask which term is searched in the column"""
