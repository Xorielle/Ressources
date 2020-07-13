#! /usr/bin/python3
# -*- coding: utf-8 -*-


import pymysql
import datetime
import Functions.addRow as fcta
import Functions.search as fcts
import Functions.connectionDb as conn
import Functions.buildSQL as build

results = ((4, 'sapin', 'organique', 3, 'scie, palette'), (5, 'chêne', 'organique', 2, "meuble (l'arbre dont proviennent les planches est très dur !)"), (6, 'pin', 'organique', 3, 'idem sapin'), (7, 'pin', 'organique', 3, 'rien à signaler'), (8, 'Caoutchouc', 'polymères', 0, 'vieux pneus de vélo'), (9, 'Cuivre', 'métal', None, None))
description = (('id', 1, None, 3, 3, 0, False), ('t_m_nom', 253, None, 12, 12, 0, True), ('t_m_famille', 253, None, 12, 12, 0, True), ('t_m_durabilite_aqueux', 1, None, 4, 4, 0, True), ('t_m_application', 252, None, 196605, 196605, 0, True))
sizeRequest = 5

fcts.printResults(results, description, sizeRequest)


usedTable = "Materiaux"
s_columns = ["t_m_id","t_m_nom"]
s_type_columns = ["int","varchar(12)"]
sizeRequest2 = 2

fcts.getSearchCriterias(usedTable, s_columns, s_type_columns, sizeRequest2)