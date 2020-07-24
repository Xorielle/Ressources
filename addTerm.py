#! /usr/bin/python3
# -*- coding: utf-8 -*-


import pymysql
import Functions.addRow as fct
import Functions.connectionDb as conn


def getTerm(usedTable, cursor):
    cursor.execute("""SELECT MAX(id) FROM %s;""" % usedTable)
    last_id = cursor.fetchone()

    if last_id[0] == None:
        last_id[0] = 0

    raw_input = [last_id[0]+1]

    print("Pour l'ajout de termes autorisés (à rentrer un par un), l'accentuation est importante mais pas la casse.")
    raw_input.append(input("Quel terme souhaitez-vous autoriser ? "))

    return(raw_input)


# Initialize users parameters and connection to DB
user_name, password, date = conn.parametersWithPass()
db, cursor = conn.connectionToDb(user_name, password=password)

answer_abort = "O"

while answer_abort == "O":

    # Ask about what will be added
    usedTable = "Words"
    print("Ajoutons des termes utilisables pour la complétion et la recherche.")
    columns = ["id", "word"]
    type_columns = ["int", "varchar"]
    sizeTable = 2
    namesColumns = ["ID", "Mot autorisé"]
    raw_input = getTerm(usedTable, cursor)

    sql_command = fct.prepareSQLRequest(sizeTable)
			
	# Add the term in the db
    fct.addingRowInDb(usedTable, sql_command, raw_input, cursor, db)

    answer_abort = input("Souhaitez-vous continuer à compléter la base de données ? [O] pour continuer, toute autre touche pour quitter ")

print("Sortie de la BDD")

db.close()
