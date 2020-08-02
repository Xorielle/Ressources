#! /usr/bin/python3
# -*- coding: utf-8 -*-


import pymysql
import Functions.connectionDb as conn
import Functions.search as fct

# Initialize users parameters and connection to DB
user_name, date = conn.parametersWithoutPass()
db, cursor = conn.connectionToDb(user_name)

usedTable = fct.chooseTable()
namesColumns, controlled, units, categories = conn.getNamesOfColumns(usedTable, cursor)

size = len(namesColumns)

for i in range (size):
    name = str(namesColumns[i])
    category = str(categories[i])
    input(name + " " + category)