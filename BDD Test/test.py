#! /usr/bin/python3
# -*- coding: utf-8 -*-


import pymysql
import datetime
import Functions.addRow as fcta
import Functions.search as fcts
import Functions.connectionDb as conn
import Functions.buildSQL as build
import createDBforTest


# Creation of the DB and connection to DB for further testing.
# The connection to DB is not tested.

db, cursor = createDBforTest.prepareTest()
print("ok")


# Creation of test indicators
counterGlobal = 0
counterFalse = 0
listFalse = []
ListNotTested = ["addRow: chooseTable", "addRow: getRowInformation", "addRow: modifyRowInformation", "addRow: userConfirmation"]


# Test of addRow's functions
counterGlobal += 1
if fcta.getTableStructure("Materiaux", cursor) != (['id', 't_m_date', 't_m_nommodif', 't_m_nom', 't_m_famille', 't_m_prix', 't_m_massevolumique', 't_m_durabilite_aqueux', 't_m_application'], ['tinyint(3) unsigned', 'date', 'varchar(12)', 'varchar(12)', 'varchar(12)', 'float unsigned', 'float unsigned', 'tinyint(4)', 'text'], 9, [None, None, None, 'do not know', None, None, None, None, None]):
    counterFalse +=1
    listFalse.append("addRow: getTableStructure")

counterGlobal += 1
if fcta.verifyRowSyntaxes([12, '2020-07-21', 'xorielle', '', 'alliage', '24', '8500', '2', ''], 9, ['id', 't_m_date', 't_m_nommodif', 't_m_nom', 't_m_famille', 't_m_prix', 't_m_massevolumique', 't_m_durabilite_aqueux', 't_m_application'], [None, None, None, 'do not know', None, None, None, None, None]) != [12, '2020-07-21', 'xorielle', 'do not know', 'alliage', '24', '8500', '2', None]:
    counterFalse += 1
    listFalse.append("addRow: verifyRowSyntaxes")

counterGlobal += 1
if fcta.prepareSQLRequest(9) != ["(%s", ", %s", ", %s", ", %s", ", %s", ", %s", ", %s", ", %s", ", %s", ");"]:
    counterFalse += 1
    listFalse.append("addRow: prepareSQLrequest")

counterGlobal += 1
if fcta.addingRowInDb("Materiaux", ["(%s", ", %s", ", %s", ", %s", ", %s", ", %s", ", %s", ", %s", ", %s", ");"], [12, '2020-07-21', 'xorielle', 'do not know', 'alliage', '24', '8500', '2', None], cursor, db) != ():
    counterFalse += 1
    listFalse.append("addRow: addingRowInDb")






print("\nLes %d tests ont été effectués." % counterGlobal)

if counterFalse !=0:
    print("Parmi ceux-là, les %d tests suivants sont faux." % counterFalse)
    for row in listFalse:
        print(row)
else:
    print("Parmi ceux-là, aucun n'est faux.")

print("\nLes tests des fonctions suivantes ne sont pas effectués automatiquement, car ils nécessitent des entrées manuelles :")
for row in ListNotTested:
    print(row)

db.close()