#! /usr/bin/python3
# -*- coding: utf-8 -*-


import pymysql


def introduction():
    print("\nAttention, vous entrez dans la matrice. Soyez sûrs de ce que vous faites, ou passez votre chemin. \
        \n Il vous est d'ailleurs conseillé d'effectuer une backup avant de continuer à arpenter les méandres \
de ces lieux, à trifouiller les tréfonds obscurs qui s'offrent à vous, à vous immerger dans ces sombres reco...\
Bref, venons-en aux faits.")
    answer = input("Etes-vous sûr de vouloir continuer ? [O/N] ")
    if answer == "O":
        return(True)
    elif answer == "N":
        return(False)
    else:
        return(introduction())

    
def chooseModificationType():
    print("Quel type de modification souhaitez-vous effectuer ?")
    modificationType = input("Ajouter une colonne [A], supprimer une colonne [S], modifier une colonne existante [M] ? ")
    if (modificationType != "A") and (modificationType != "S") and (modificationType != "M"):
        print("Concentrez-vous, vous allez faire des bêtises sinon !")
        return(chooseModificationType())
    return(modificationType)


def chooseTable():
    table = input("Souhaitez-vous effectuer cette modification parmi les Matériaux [M] ou les Pièces [P] ? ")
    if table == "M":
        usedTable = "Materiaux"
        supportTable = "NameMateriaux"
    elif table == "P":
        usedTable = "Pieces"
        supportTable = "NamePieces"
    else:
        print("Concentrez-vous, c'est sérieux !")
        return(chooseTable())
    return(usedTable, supportTable)


def getNamesOfColumns(usedTable, cursor):
    """Get four lists : namesColumns, controlled, units, categories."""
    namesColumns = []
    controlled = []
    units = []
    categories = []

    cursor.execute("SELECT * FROM Name%s;" % usedTable)
    
    names = cursor.fetchone()
    for name in names:
        namesColumns.append(name)

    constraints = cursor.fetchone()
    for constraint in constraints:
        controlled.append(constraint)

    units_table = cursor.fetchone()
    for unit in units_table:
        units.append(unit)

    categories_table = cursor.fetchone()
    for category in categories_table:
        categories.append(category)

    return(namesColumns, controlled, units, categories)


def getTableStructure(usedTable, cursor):
    """Return the title of the columns, the type of data and the number of columns"""
    cursor.execute('DESCRIBE %s;' % usedTable)
    description = cursor.fetchall()
    columns = []
    type_columns = []
    default_columns = []

    for row in description:
        columns.append(row[0])
        type_columns.append(row[1])
        default_columns.append(row[4])
    sizeTable = len(columns)

    return(columns, type_columns, sizeTable, default_columns)

