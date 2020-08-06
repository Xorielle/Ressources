#! /usr/bin/python3
# -*- coding: utf-8 -*-


import pymysql
import Functions.connectionDb as conn


# Initialize users parameters and connection to DB
user_name, date = conn.parametersWithoutPass()
db, cursor = conn.connectionToDb(user_name)
authorized = conn.getAuthorizedTerms(cursor)

authorized.pop(0)
print("Les termes autorisés sont : " + ", ".join([term.lower() for term in authorized]))
