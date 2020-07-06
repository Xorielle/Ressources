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
print(type_column)


# Get the information of the row we want to add
row_input = []

for column in columns:
    row_input.append(input(column + " "))


# Verify the row is correct before committing the data base
for column in range (0, sizeTable):
    print("\n", columns[column], row_input[column])

print("\n", 'Est-ce que les données ci-dessus à ajouter à la table ' + usedTable + ' sont correctes ?')
answer = input ('Oui [O] ou Non [N] ? ')
assert answer == 'O' or answer == 'N', 'Entrer O ou N en majuscule' # Trouver comment ne pas revenir au début du programme...
# + let the possibility to go back and modify the inputs without writing all again


# Prepare to add in db with correct type
if answer == 'O':
    row_input_typed = []
    for nb in range(0,sizeTable-1):
        print(type_column[nb])
        if ("int" in type_column[nb]):
            row_input_typed.append(int(row_input[nb]))
        elif ("float" in type_column[nb]):
            row_input_typed.append(float(row_input[nb]))
        else:
            row_input_typed.append(row_input[nb])
        row_input_typed.append(", ")
    print(type_column[sizeTable-1])
    if "int" in type_column[sizeTable-1]:
        row_input_typed.append(int(row_input[sizeTable-1]))
    elif "float" in type_column[sizeTable-1]:
        row_input_typed.append(float(row_input[sizeTable-1]))
    else:
        row_input_typed.append(row_input[sizeTable-1])

else:
    print("mauvaise entrée")

sql = ("""INSERT INTO""" + usedTable + """VALUES (""" + "".join(row_input_typed) + ");")
print(sql)

try:
    cursor.execute(sql)
    print("Ligne ajoutée")
    db.commit()
    print("BDD mise à jour avec succès")

except:
    cursor.execute("SHOW WARNINGS;")
    warnings = cursor.fetchall()
    print("warnings : ", warnings)
    db.rollback()



db.close()