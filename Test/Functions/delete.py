#! /usr/bin/python3
# -*- coding: utf-8 -*-


import pymysql


def chooseTable():
    """Choose wether we are modifying in Materiaux or Pieces.
    Return usedTable"""
    table = input("Voulez-vous supprimer une ligne parmi les matériaux [M] ou les pièces [P] ? ")
    
    if table == "M": 
        return("Materiaux")
    
    if (table == "P"):
        return("Pieces")
    
    else:
        return(chooseTable())


def haveID(usedTable, cursor):
    """Verifying the user knows the id of the row he wants to suppress.
    Return the tuple (id, "O") or (None, "N")"""
    print("\nAttention : pour supprimer une ligne, vous devez connaître son ID exact.") 
    print("Si ce n'est pas le cas, quittez ce programme et allez chercher l'ID grâce au programme de recherche.")
    print("\nAttention, supprimer une ligne est un processus irréversible.")
    print("Si vous avez changé d'avis, veuillez quitter ce programme en sélectionnant N ci-dessous.")
    answer = input("Connaissez-vous l'ID de la ligne à supprimer ? [O/N] ")

    if answer == "O":
        
        try:
            suppressed_id = int(input("Tapez l'ID : "))
            cursor.execute("SELECT MAX(id) FROM %s;" % usedTable)
            max_id = cursor.fetchone()[0]

            if (suppressed_id > 0) and (suppressed_id <= max_id):
                return(suppressed_id, answer)

            else:
                print("L'ID saisi est en-dehors des plages de valeur acceptées, sortie du programme.")
                return(None, "N")

        except:
            print("L'ID saisi est incorrect, sortie du programme.")
            return(None, "N")
    
    else:
        print("Sortie du programme.")
        return(None, "N")


def delete(suppressed_id, usedTable, cursor, db):
    """Delete the row."""
    request = "DELETE FROM %s WHERE id = %d;" % (usedTable, suppressed_id)

    try:
        cursor.execute(request)
        db.commit()
        print("La ligne %d a été supprimée avec succès." % suppressed_id)
    
    except:
        print("Il y a eu une erreur, la ligne %d n'a pas été supprimée." % suppressed_id)
        cursor.execute("SHOW WARNINGS;")
        warnings = cursor.fetchall()
        print("warnings : ", warnings)
    
    return()
