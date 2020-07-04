#! /usr/bin/python3

import pymysql

db = pymysql.connect('localhost','xorielle','','TestDB')
cursor = db.cursor()


# Choose the table we want to complete
usedTable = input('Ajouter à la table Matériaux [M] ou à la table Pièces [P] ? ')

assert usedTable=='M' or usedTable=='P', 'Erreur de saisie, entrer M ou P en majuscule'

if (usedTable == 'M'):
    usedTable = 'Materiaux'
    print('Ajoutons une ligne à la table des Matériaux')
elif (usedTable == 'P'):
    usedTable = 'Pieces'
    print('Ajoutons une ligne à la table des Pièces')


# Get the structure of the table in which we want to add a row
cursor.execute('DESCRIBE %s;' % usedTable)
description = cursor.fetchall()
columns = []
type_column = []

for row in description:
    columns.append(row[0])
    type_column.append(row[1])


# Get the information of the row we want to add
row_input = []

for column in columns:
    row_input.append(input(column + " "))


# Verify the row is correct before committing the data base
print('Est-ce que les données à ajouter à la table ' + usedTable + ' sont correctes ? \n')
for column in range (0, len(columns)):
    print(columns[column], row_input[column], "\n")

answer = input ('Oui [O] ou Non [N] ? ')
assert answer == 'O' or answer == 'N', 'Entrer O ou N en majuscule'

#if answer == 'O':
#    sql = """INSERT INTO %s VALUES (""" % usedTable
#    for nb in range (O, len(columns)-1):
#        sql."%s", "%s"



db.close()