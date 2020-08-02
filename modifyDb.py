#! /usr/bin/python3
# -*- coding: utf-8 -*-


import pymysql
import Functions.modifyDb as fct
import Functions.connectionDb as conn


user_name, password, date = conn.parametersWithPass()
db, cursor = conn.connectionToDb(user_name, password=password)

answer = fct.introduction()

while answer:
    modificationType = fct.chooseModificationType()
    usedTable, supportTable = fct.chooseTable()
    namesColumns, controlled, units, categories = fct.getNamesOfColumns(usedTable, cursor)
    used_titles, used_types, sizeTable, used_defaults = fct.getTableStructure(usedTable, cursor)
    print("\nTitle : ", used_titles)
    print("\nType : ", used_types)
    print("\nsizeTable : ", sizeTable)
    print("\nDefault : ", used_defaults)


    
    answer = False



