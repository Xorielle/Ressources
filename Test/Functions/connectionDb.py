#! /usr/bin/python3
# -*- coding: utf-8 -*-


import pymysql
import datetime


def parametersWithoutPass():
    """Fetch the username and the date
    Return (user_name, date)"""
    user_name = input('Qui utilise la BDD ? ')
    full_date = datetime.datetime.now()
    date = "%s-%s-%s" % (full_date.strftime("%Y"), full_date.strftime("%m"), full_date.strftime("%d"))
    print("Date du jour : ", date)
    
    return(user_name, date)


def parametersWithPass():
    """Fetch the username, the associated password and the date
    Return (user_name, password, date)"""
    user_name = input('Qui utilise la BDD ? ')
    password = input("Mot de passe ? ")
    full_date = datetime.datetime.now()
    date = "%s-%s-%s" % (full_date.strftime("%Y"), full_date.strftime("%m"), full_date.strftime("%d"))
    print("Date du jour : ", date)
    
    return(user_name, password, date)

def connectionToDb(username, host = "localhost", db_name = "TestDB", password = ""):
    """Connect to the DB and get the accessglobal cursor
    Return (db, db.cursor())"""
    db = pymysql.connect(host,username,password,db_name)
    cursor = db.cursor()
    cursor.execute("SET NAMES 'utf8';")
    return(db, cursor)


def getNamesOfColumns(usedTable, cursor):
    """Get the equivalent names of the columns, to have something more readable for the user.
    Return also a "True" or "False" list to know if the column has to get the controlled words or is free of constraints."""
    namesColumns = []
    controlled = []
    cursor.execute("SELECT * FROM name%s;" % usedTable)
    names = cursor.fetchone()

    for name in names:
        namesColumns.append(name)

    constraints = cursor.fetchone()
    for constraint in constraints:
        controlled.append(constraint)

    return(namesColumns, controlled)


def getAuthorizedTerms(cursor):
    """Return the sorted list of the terms you can add in the DB"""
    cursor.execute("SELECT word FROM Words;")
    words = cursor.fetchall()
    authorized = []
    for word in words:
        authorized.append(word[0].lower())
    
    cursor.execute("SELECT t_m_nom FROM Materiaux;")
    noms = cursor.fetchall()
    for nom in noms:
        authorized.append(nom[0].lower())
    
    authorized.sort()
    return(authorized)
