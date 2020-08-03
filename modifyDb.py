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
    list_categories = fct.buildList_categories(categories)
    used_titles, used_types, sizeTable, used_defaults = fct.getTableStructure(usedTable, cursor)

    if modificationType == "A":
        newName, newTitle, supportTitle, newType, newUnit, newDefault, newControlled, newCategory = fct.getAddingData(usedTable, list_categories)
        request1, request2, request3, request4, request6, request5 = fct.buildSQLAdd(usedTable, supportTable, newName, newTitle, supportTitle, newType, newUnit, newDefault, newControlled, newCategory)
        fct.executeAdd(request1, request2, request3, request4, request5, request6, newTitle, supportTable, cursor)
        
    elif modificationType == "S":
        name_id = fct.getColumnToDelete(namesColumns)
        request1, request2 = fct.buildSQLDelete(usedTable, supportTable, name_id, used_titles)
    
        try:
            cursor.execute(request1)
            print("\nColonne supprimée avec succès dans la table. Suppression des métadonnées...")
            cursor.execute(request2)
            print("Métadonnées de la colonne supprimées avec succès dans la table reliée.")
        except:
            print("Ça n'a pas marché. Vous avez dû faire une bêtise. De toute façons, id ne peut pas être supprimée.")
    
    
    elif modificationType == "M":
        print("Vous allez modifier une colonne.")


    print("J'espère que tu aimeras [les changements de la BDD]. Dans le cas contraire, ne m'accuse pas. Accuse plutôt mes amis de l'auuu-deelààà !")
    answer = False



db.commit()
db.close()