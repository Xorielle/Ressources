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

sizeTable = len(columns)


# Get the information of the row we want to add
row_input = []

for column in columns:
    row_input.append(input(column + " "))


# Verify the row is correct before committing the data base
for column in range (0, sizeTable):
    print("\n", columns[column], row_input[column])

print('\nEst-ce que les données ci-dessus à ajouter à la table ' + usedTable + ' sont correctes ?')
answer = input ('Oui [O] ou Non [N] ? ')
assert answer == 'O' or answer == 'N', 'Entrer O ou N en majuscule' # Trouver comment ne pas revenir au début du programme...
# + let the possibility to go back and modify the inputs without writing all again


# Prepare to add in db with correct type
if answer == 'O':
    sql_command = ["(%s"]
    for nb in range(1, sizeTable):
        sql_command.append(", %s")
    sql_command.append(");")

else:
    print("mauvaise entrée")



# Add the row in the db if there is no SQL issue
try:
    cursor.execute("INSERT INTO %s VALUES " % usedTable + "".join(sql_command), tuple(row_input))
    print("Ligne ajoutée")
    db.commit()
    print("BDD mise à jour avec succès")

except:
    cursor.execute("SHOW WARNINGS;")
    warnings = cursor.fetchall()
    print("warnings 3: ", warnings)
    db.rollback()



db.close()