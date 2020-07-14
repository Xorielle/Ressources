#! /usr/bin/python3
# -*- coding: utf-8 -*-


import pymysql
import Functions.addRow as fct
import Functions.connectionDb as conn


# Initialize users parameters and connection to DB
user_name, date = conn.parameters()
db, cursor = conn.connectionToDb(user_name)


answer_abort = "O"

while answer_abort == "O":

	# Ask about what will be added
	usedTable = fct.chooseTable()
	columns, type_columns, sizeTable, default_columns = fct.getTableStructure(usedTable, cursor)
	raw_row_input = fct.getRowInformation(usedTable, date, user_name, sizeTable, columns, cursor)

	answer_modification = "M"

	while answer_modification == "M":
		# Re-modelling to have the right information
		row_input = fct.verifyRowSyntaxes(raw_row_input, sizeTable, columns, default_columns)
		answer_verification = fct.userConfirmation(usedTable)

		if answer_verification == 'O':
			sql_command = fct.prepareSQLRequest(sizeTable)
			answer_modification = 0

			# Add the row in the db
			fct.addingRowInDb(usedTable, sql_command, row_input, cursor, db)

		else:
			answer_modification = input("Voulez-vous modifier vos entrées [M] ou annuler toute saisie [toute autre touche] ? ")
			
			if answer_modification == "M":
				raw_row_input = fct.modifyRowInformation(row_input, sizeTable, columns)

	answer_abort = input("Souhaitez-vous continuer à compléter la base de données ? [O] pour continuer, toute autre touche pour quitter ")



print("Sortie de la BDD")

db.close()