#! /usr/bin/python3
# -*- coding: utf-8 -*-


import pymysql
import Functions.createUser as fct
import Functions.connectionDb as conn


# Initialize users parameters and connection to DB
user_name, password, date = conn.parametersWithPass()
db, cursor = conn.connectionToDb(user_name, password=password)

print("Pour créer un nouvel utilisateur, vous avez besoin de plusieurs informations :\
 son nom, son mot de passe, et les droits que vous souhaitez lui allouer.")
print("Pour la liste des droits existants, reportez-vous au manuel d'utilisation.")

name, password, insert, update, delete, alter, create = fct.whatOptions()

if insert == None:
    request = fct.buildRequestAll(name, password)

else:
    privilegesList = fct.buildListPrivileges(insert, update, delete, alter, create)
    request = fct.buildRequest(name, password, privilegesList)

try:
    cursor.execute(request)
    print("L'utilisateur a été créé avec succès.")

except:
    print("Il y a eu un problème lors de la création de l'utilisateur.")
