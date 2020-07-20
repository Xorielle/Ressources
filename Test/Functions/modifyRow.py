#! /usr/bin/python3
# -*- coding: utf-8 -*-


import pymysql


def chooseTable():
    """Choose wether we are modifying in Materiaux or Pieces.
    Return usedTable"""
    table = input("Voulez-vous modifier une ligne parmi les matériaux [M] ou les pièces [P] ? ")
    
    if table == "M": 
        return("Materiaux")
    
    if (table == "P"):
        return("Pieces")
    
    else:
        return(chooseTable())


def haveID(usedTable, cursor):
    """Verifying the user knows the id of the row he wants to modify
    Return the tuple (id, "O") or (None, "N")"""
    print("Attention : pour modifier une ligne, vous devez connaître son ID exact.") 
    print("Si ce n'est pas le cas, quittez ce programme et allez chercher l'ID grâce au programme de recherche.")
    answer = input("Connaissez-vous l'ID de la ligne à modifier ? [O/N] ")

    if answer == "O":
        
        try:
            modify_id = int(input("Tapez l'ID : "))
            cursor.execute("SELECT MAX(id) FROM %s;" % usedTable)
            max_id = cursor.fetchone()[0]

            if (modify_id > 0) and (modify_id <= max_id):
                return(modify_id, answer)

            else:
                print("L'ID saisi est en-dehors des plages de valeur acceptées, sortie du programme.")
                return(None, "N")

        except:
            print("L'ID saisi est incorrect, sortie du programme.")
            return(None, "N")
    
    else:
        print("Sortie du programme.")
        return(None, "N")
