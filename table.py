#! /usr/bin/python3
# -*- coding: utf-8 -*-

import pymysql
import Functions.connectionDb as conn


def getNamesOfColumns(usedTable, cursor):
    """Get the equivalent names of the columns, to have something more readable for the user.
    Return also a "True" or "False" list to know if the column has to get the controlled words or is free of constraints."""
    namesColumns = []
    controlled = []
    units = []
    categories = []
    
    cursor.execute("SELECT * FROM Name%s;" % usedTable)
    names = cursor.fetchone()

    for name in names:
        namesColumns.append(name)

    constraints = cursor.fetchone()
    for constraint in constraints:
        controlled.append(constraint)

    unitsTable = cursor.fetchone()
    for unit in unitsTable:
        units.append(unit)

    categoriesTable = cursor.fetchone()
    for category in categoriesTable:
        categories.append(category)

    return(namesColumns, controlled, units, categories)


def getTableStructure(usedTable, cursor):
    """Return the title of the columns, the type of data and the number of columns"""
    cursor.execute('DESCRIBE %s;' % usedTable)
    description = cursor.fetchall()
    columns = []
    type_columns = []
    default_columns = []
    null = []

    for row in description:
        columns.append(row[0])
        type_columns.append(row[1])
        null.append(row[2])
        default_columns.append(row[4])
    sizeTable = len(columns)

    return(columns, type_columns, sizeTable, default_columns, null)


def createRows(sizeTable, columns, namesColumns, type_columns, default_columns, null, controlled, units, categories):
    f = open("table2.txt", "w")
    f.write("\\begin{tabular}{|c|c|c|c|c|c|c|c|}\n\\hline\nTitre & Nom affiché & Type & Unité & Catégorie d'affichage & Limité ? & Valeur par défaut & Peut être vide ? \\\\")
    for i in range(sizeTable):
        unit = units[i]
        default_column = default_columns[i]
        column = columns[i]
        reformat = column.split("_")
        column = "\\_".join(reformat)
        if unit == None:
            unit = " "
        if default_column == None:
            default_column = ""
        f.write("\n\\hline\n%s & %s & %s & $%s$ & %s & %s & %s & %s \\\\" % (column, namesColumns[i], type_columns[i], unit, categories[i], controlled[i], default_column, null[i]))
    f.write("\n\\hline\n\\end{tabular}")
    f.close()


db, cursor = conn.connectionToDb(username = 'xorielle')
columns, type_columns, sizeTable, default_columns, null = getTableStructure("Pieces", cursor)
namesColumns, controlled, units, categories = getNamesOfColumns("Pieces", cursor)
createRows(sizeTable, columns, namesColumns, type_columns, default_columns, null, controlled, units, categories)

