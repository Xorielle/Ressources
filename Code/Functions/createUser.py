#! /usr/bin/python3
# -*- coding: utf-8 -*-


import pymysql


def whatOptions():
    name = input("Quel est le nom du nouvel utilisateur ? Merci d'éviter les caractères spéciaux. ")
    password = 0
    password2 = None
    
    while password != password2:
        password = input("Quel est le mot de passe du nouvel utilisateur ? Merci d'éviter les caractères spéciaux. ")
        password2 = input("Confirmez le mot de passe : ")
    
    print("Merci de répondre par O (oui) ou N (non) à chacune des questions suivantes.")
    insert, update, delete, alter, create, backup, allPrivileges = None, None, None, None, None, None, None
    
    while (allPrivileges != "O") and allPrivileges != "N":
        allPrivileges = input("Souhaitez-vous que l'utilisateur ait tous les droits sur la base de données ? ")
    
    if allPrivileges == "O":
        return(name, password, insert, update, delete, alter, create, backup)

    else:
        while insert != "O" and insert != "N":
            insert = input("Souhaitez-vous que l'utilisateur ait le droit d'ajouter de nouvelles lignes ? ")
        while update != "O" and update != "N":
            update = input("Souhaitez-vous que l'utilisateur ait le droit de modifier des lignes existantes ? ")
        while delete != "O" and delete != "N":
            delete = input("Souhaitez-vous que l'utilisateur ait le droit de supprimer des lignes ? ")
        while alter != "O" and alter != "N":
            alter = input("Souhaitez-vous que l'utilisateur ait le droit de modifier la structure de la base de données ? ")
        while create != "O" and create != "N":
            create = input("Souhaitez-vous que l'utilisateur ait le droit de gérer les utilisateurs (création, suppression, gestion des droits) ? ")
        while backup != "O" and backup != "N":
            backup = input("Souhaitez-vous que l'utilisateur ait le droit de restaurer une backup ? ")
        

        return(name, password, insert, update, delete, alter, create, backup)


def buildRequestAll(name, password):
    requestCreate = "CREATE USER '%s'@'localhost' IDENTIFIED BY '%s';" %(name, password)
    requestGrant = "GRANT ALL PRIVILEGES ON Ressources.* TO '%s'@'localhost' WITH GRANT OPTION;" % name
    requestOption = "GRANT GRANT OPTION ON *.* TO '%s'@'localhost';" %name
    return(requestCreate, requestGrant, requestOption)  


def buildListPrivileges(name, insert, update, delete, alter, create, backup):
    privilegesList = ["GRANT SELECT"]
    if insert == "O":
        privilegesList.append(", INSERT")
    if update == "O":
        privilegesList.append(", UPDATE")
    if delete == "O":
        privilegesList.append(", DELETE")
    if alter == "O":
        privilegesList.append(", ALTER")
    if backup == "O":
        privilegesList.append(", DROP")
        privilegesList.append(", CREATE")
        privilegesList.append(", INDEX")
        privilegesList.append(", LOCK TABLES")

    privilegesList.append(" ON Ressources.* TO '%s'@'localhost';" %name)

    return(privilegesList)



def buildRequestSelected(name, password, privilegesList, create):
    requestCreate = "CREATE USER '%s'@'localhost' IDENTIFIED BY '%s';" %(name, password)
    requestGrant = "".join(privilegesList)
    if create == "O":
        requestOption = "GRANT CREATE USER, GRANT OPTION ON *.* TO '%s'@'localhost';" %name
    else:
        requestOption = "SELECT * FROM Materiaux;"
    return(requestCreate, requestGrant, requestOption)


def userToDelete():
    name = input("Quel utilisateur souhaitez-vous supprimer ? ")
    return(name)


def buildDeleteRequest(name):
    request = "DROP USER '%s'@'localhost';" % name
    return(request)
