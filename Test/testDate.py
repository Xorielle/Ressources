#! /usr/bin/python3
# -*- coding: utf-8 -*-


import pymysql
import datetime
import Functions.search as fcts
import Functions.connectionDb as conn
import Functions.buildSQL as build
import createDBforTest


# Creation of the DB and connection to DB for further testing.
# The connection to DB is not tested.

db, cursor = createDBforTest.prepareTest()
print("Database created")

def getDate():
    date_min = str(input("Date initiale ? "))
    date_max = input("Date de fin ? ")
    print(date_min + " " + date_max)
    return(date_min, date_max)

date_min, date_max = getDate()

sql = ["SELECT %s, %s, %s FROM Materiaux WHERE t_m_date BETWEEN '", date_min, "' AND '", date_max, "';"]
selected_columns = ["id", "t_m_date", "t_m_nom"]

results, description = fcts.searchDb(sql, selected_columns, cursor)

fcts.printResults(results, description, 3)