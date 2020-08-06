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

letter = input("Souhaitez-vous créer [C] un utilisateur ou supprimer [S] un utilisateur ? ")

if letter == "C":

    name, password, insert, update, delete, alter, create, backup = fct.whatOptions()

    if insert == None:
        requestCreate, requestGrant, requestOption = fct.buildRequestAll(name, password)

    else:
        privilegesList = fct.buildListPrivileges(name, insert, update, delete, alter, create, backup)
        requestCreate, requestGrant, requestOption = fct.buildRequestSelected(name, password, privilegesList, create)
        print(requestOption)

    try:
        cursor.execute(requestCreate)
        print("L'utilisateur a été créé avec succès.")
        cursor.execute(requestGrant)
        cursor.execute(requestOption)
        print("Les privilèges voulus ont été accordés avec succès au nouvel utilisateur.")
        cursor.execute("FLUSH PRIVILEGES;")
        print("Les changements ont bien été enregistrés.")

    except:
        print("Il y a eu un problème lors de la création de l'utilisateur et de ses droits.")


elif letter == "S":
    name = fct.userToDelete()
    request = fct.buildDeleteRequest(name)
    try:
        cursor.execute(request)
        print("L'utilisateur %s a bien été supprimé." %name)
    except:
        print("%s n'a pas été supprimé, vérifiez que vous avez les droits et que le nom est correct." %name)


else:
    print("Vous avez saisi une mauvaise lettre, relancez le programme.")

db.commit()
db.close()