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
ListNotTested = ["addRow: chooseTable", "addRow: getRowInformation", "addRow: modifyRowInformation", "addRow: userConfirmation", "search: typeOfSearch", "search: chooseTable", "search: getColumnToSearch", "search: getColumnsToSearch", "search: getSearchCriteria", "search: getSearchCriterias", "search: getNewCriteriaText", "search: numericSimple", "search: numericInterval", "search: selectColumnsToPrint"]


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


# Let's test the search functions
counterGlobal += 1
if fcts.getTableStructure("Materiaux", cursor) != (['id', 't_m_date', 't_m_nommodif', 't_m_nom', 't_m_famille', 't_m_prix', 't_m_massevolumique', 't_m_durabilite_aqueux', 't_m_application'], ['tinyint(3) unsigned', 'date', 'varchar(12)', 'varchar(12)', 'varchar(12)', 'float unsigned', 'float unsigned', 'tinyint(4)', 'text'], 9):
    counterFalse += 1
    listFalse.append("search: getTableStructure")

counterGlobal += 1
if fcts.prepareSQLRequestSimple("pin", None, "Materiaux", ["id", "t_m_nom", "t_m_famille"], "t_m_nom", "varchar(12)") != (["SELECT %s", ", %s", ", %s", " FROM Materiaux WHERE t_m_nom LIKE '%%pin%%';"], 3):
    counterFalse += 1
    listFalse.append("search: prepareSQLRequestSimple")

counterGlobal += 1
if fcts.prepareSQLRequestAdvanced("Materiaux", ["id", "t_m_nom", "t_m_famille"], [" t_m_nom LIKE '%%pin%%'"]) != (["SELECT %s", ", %s", ", %s", " FROM Materiaux WHERE", " t_m_nom LIKE '%%pin%%'", ";"], 3):
    counterFalse += 1
    listFalse.append("search: prepareSQLRequestAdvanced")

counterGlobal += 1
if fcts.searchDb(["SELECT %s", ", %s", ", %s", ", %s", " FROM Materiaux WHERE", " t_m_nom LIKE '%%pin%%'", "AND", " t_m_nom NOT LIKE '%%maritime%%'", "AND", " t_m_nom NOT LIKE '%%parasol%%'", ";"], ["id", "t_m_date", "t_m_nom", "t_m_famille"], cursor) != (((1, datetime.date(2020, 7, 6), 'sapin', 'organique'), (7, datetime.date(2020, 7, 13), 'pin', 'organique'), (9, datetime.date(2020, 7, 13), 'pomme de pin', 'organique'), (11, datetime.date(2020, 7, 13), 'pin noir', 'organique')), (('id', 1, None, 3, 3, 0, False), ('t_m_date', 10, None, 10, 10, 0, False), ('t_m_nom', 253, None, 48, 48, 0, True), ('t_m_famille', 253, None, 48, 48, 0, True))):
    counterFalse += 1
    listFalse.append("search: searchDb")



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