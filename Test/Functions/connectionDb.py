#! /usr/bin/python3
# -*- coding: utf-8 -*-


import pymysql
import datetime


def parameters():
    """Fetch the username and the date
    Return (user_name, date)"""
    user_name = input('Qui utilise la BDD ? ')
    full_date = datetime.datetime.now()
    date = "%s-%s-%s" % (full_date.strftime("%Y"), full_date.strftime("%m"), full_date.strftime("%d"))
    print("Date du jour : ", date)
    
    return(user_name, date)


def connectionToDb(username, host = "localhost", db_name = "TestDB", password = ""):
    """Connect to the DB and get the accessglobal cursor
    Return (db, db.cursor())"""
    db = pymysql.connect(host,username,password,db_name)
    cursor = db.cursor()
    cursor.execute("SET NAMES 'utf8';")
    return(db, cursor)


def getNamesOfColumns(usedTable, cursor):
    """Get the equivalent names of the columns, to have something more readable for the user"""
    namesColumns = []
    cursor.execute("SELECT * FROM name%s;" % usedTable)
    names = cursor.fetchone()

    for name in names:
        namesColumns.append(name)

    return(namesColumns)
