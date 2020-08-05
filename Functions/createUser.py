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
    insert, update, delete, alter, create = None, None, None, None, None
    
    while insert != "O" or insert != "N":
        insert = input("Souhaitez-vous que l'utilisateur ait le droit d'ajouter de nouvelles lignes ? ")
    while update != "O" or update != "N":
        update = input("Souhaitez-vous que l'utilisateur ait le droit de modifier des lignes existantes ? ")
    while delete != "O" or delete != "N":
        delete = input("Souhaitez-vous que l'utilisateur ait le droit de supprimer des lignes ? ")
    while alter != "O" or alter != "N":
        alter = input("Souhaitez-vous que l'utilisateur ait le droit de modifier la structure de la base de données ? ")
    while create != "O" or create != "N":
        create = input("Souhaitez-vous que l'utilisateur ait le droit de créer de nouveaux utilisateurs ? ")

    return(name, password, insert, update, delete, alter, create)


def whatFunctionToUse(insert, update, delete, alter, create):
    