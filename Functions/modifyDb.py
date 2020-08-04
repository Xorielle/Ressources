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
    print("Quel type de modification souhaitez-vous effectuer dans la structure de la base de données ?")
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
    """Return the title of the columns, the type of data and the number of columns, plus default value and Null or not"""
    cursor.execute('DESCRIBE %s;' % usedTable)
    description = cursor.fetchall()
    columns = []
    type_columns = []
    default_columns = []
    null_columns = []

    for row in description:
        columns.append(row[0])
        type_columns.append(row[1])
        null_columns.append(row[2])
        default_columns.append(row[4])
    sizeTable = len(columns)

    return(columns, type_columns, sizeTable, default_columns, null_columns)


def getColumnToDelete(namesColumns):
    print("Choisissez la colonne à supprimer. Pour cela, tapez entrée jusqu'à arriver à la colonne que vous souhaitez supprimer. \
Pour cette colonne, tapez n'importe quelle touche.")
    inp = ""
    i = 0
    while inp == "":
        name = namesColumns[i]
        inp = input(name + " ")
        i += 1
    return(sureToDelete(name, i-1, namesColumns))


def sureToDelete(name, name_id, namesColumns):
    answer = input("Vous vous apprêtez à supprimer la colonne %s. Êtes-vous sûr de votre choix ? [O/N] " % name)
    if answer == "O":
        return(name_id)
    elif answer == "N":
        return(getColumnToDelete(namesColumns))
    else:
        return(sureToDelete(name, name_id, namesColumns))


def buildSQLDelete(usedTable, supportTable, name_id, used_titles):
    """With this way of doing, id cannot be deleted because the column is named id and not n_id"""
    name = used_titles[name_id]
    request1 = "ALTER TABLE %s DROP COLUMN %s;" % (usedTable, name)
    request2 = "ALTER TABLE %s DROP COLUMN n_%s;" % (supportTable, name)
    return(request1, request2)


def buildList_categories(categories):
    list_categories = []
    for category in categories:
        if (category not in list_categories) and (category != None):
            list_categories.append(category)
    return(list_categories)


def getAddingData(usedTable, list_categories):
    print("Vous souhaitez donc ajouter une colonne à la table %s." % usedTable)
    print("Merci de répondre à ce petit questionnaire, temps estimé trois minutes.")
    print("Merci de respecter strictement la syntaxe imposée pour éviter tout problème ultérieur. \
En cas de besoin, référez-vous au paragraphe correspondant du manuel.")
    
    newName = input("Donnez un nom à votre colonne : ")
    newTitle = input("/!\\ Syntaxe /!\\ Donnez-lui son titre : ")
    newType = input("/!\\ Syntaxe /!\\ Donnez-lui son type : ")
    newUnit = input("Donnez-lui son unité, si elle en a une : ")
    newDefault = input("Donnez-lui sa valeur par défaut, si elle en a une : ")
    
    if newUnit == "":
        newUnit = None
    if newDefault == "":
        newDefault = None
    
    newControlled = input("Doit-elle accepter uniquement les termes autorisés ? [O/N] ")
    
    if newControlled == "O":
        newControlled = "True"
    elif newControlled == "N":
        newControlled = "False"
    else:
        print("Vous avez fait une erreur de saisie, merci de recommencer depuis le début.")
        return(getAddingData(usedTable, list_categories))
    
    print("Voici les catégories d'affichage déjà existantes : ")
    print(list_categories)
    newCategory = input("Dans quelle catégorie doit-elle s'afficher ? ")
    supportTitle = "n_" + newTitle
    return(newName, newTitle, supportTitle, newType, newUnit, newDefault, newControlled, newCategory)
    

def buildSQLAdd(usedTable, supportTable, newName, newTitle, supportTitle, newType, newUnit, newDefault, newControlled, newCategory):
    #Create the new column in main table
    if newDefault != None:
        
        try:
            newDefault = float(newDefault)
            request1 = """ALTER TABLE %s ADD %s %s DEFAULT %d;""" % (usedTable, newTitle, newType, newDefault)
        except:
            request1 = """ALTER TABLE %s ADD %s %s DEFAULT "%s";""" % (usedTable, newTitle, newType, newDefault)
    
    else:
        request1 = "ALTER TABLE %s ADD %s %s;" % (usedTable, newTitle, newType)
    
    #Create the new column in NameTable for metadata
    request2 = "ALTER TABLE %s ADD %s VARCHAR(32);" % (supportTable, supportTitle)
    
    #Create the requests to fill the metadatas
    if supportTable == "NameMateriaux":
        supportColumn = "n_m_date"
    elif supportTable == "NamePieces":
        supportColumn = "n_p_date"
    
    request3 = """UPDATE %s SET %s = "%s" WHERE %s = 'Date de modification';""" %(supportTable, supportTitle, newName, supportColumn)
    request4 = "UPDATE %s SET %s = '%s' WHERE %s = 'False';" %(supportTable, supportTitle, newControlled, supportColumn)
    request6 = """UPDATE %s SET %s = '%s' WHERE %s = 'métadonnées';""" %(supportTable, supportTitle, newCategory, supportColumn)
    
    if newUnit != None:
        request5 = """UPDATE %s SET %s = "%s" WHERE %s <=> NULL;""" %(supportTable, supportTitle, newUnit, supportColumn)
    else:
        request5 = None
    return (request1, request2, request3, request4, request6, request5)


def executeAdd(request1, request2, request3, request4, request5, request6, newTitle, supportTable, cursor):
    try:
        cursor.execute(request1)
        print("\nColonne %s ajoutée avec succès." % newTitle)
        cursor.execute(request2)
        print("Colonne ajoutée avec succès dans %s." % supportTable)
        cursor.execute(request3)
        print("Ajout du nom de la colonne.")
        cursor.execute(request4)
        print("Ajout de l'information sur le contrôle.")
        if request5 != None:
            cursor.execute(request5)
            print("Ajout de l'unité.")
        cursor.execute(request6)
        print("Ajout de la catégorie d'affichage.")
        print("\nProcessus d'ajout de colonne terminé, tout s'est bien passé.")
    except:
        print("Le processus s'est arrêté en cours de route. Vérifiez les syntaxes autorisées, et restaurez la base de données avant\
 de faire de nouvelles bêtises.")
    return()


def whatKindOfModification():
    print("\nVous pouvez effectuer deux types de modifications : soit une modification des métadonnées de la colonne (au niveau de \
son affichage, qu'il s'agisse du nom, de l'unité, de la catégorie pour l'affichage restreint, ou encore de si la colonne doit être \
complétée uniquement avec les termes autorisés ou non), soit une modification des données de remplissage de la colonne (son type, \
sa valeur par défaut, est-ce qu'elle a le droit d'être vide ou non).")
    modificationKind = input("Souhaitez-vous modifier les métadonnées [M] ou les données de remplissage [R] ? ")
    if modificationKind == "M":
        return("M")
    elif modificationKind == "R":
        return("R")
    else:
        print("Restez concentré, c'est pas un jeu !")
        return(whatKindOfModification())


def getColumnToModify(namesColumns):
    print("Choisissez la colonne à modifier. Pour cela, tapez entrée jusqu'à arriver à la colonne que vous souhaitez modifier. \
Pour cette colonne, tapez n'importe quelle touche.")
    inp = ""
    i = 0
    iMax = len(namesColumns)
    while inp == "":
        name = namesColumns[i]
        inp = input(name + " ")
        i += 1
        if (i == iMax) and (inp == ""):
            return(getColumnToModify(namesColumns))
    return(sureToModify(name, i-1, namesColumns))


def sureToModify(name, name_id, namesColumns):
    answer = input("Vous vous apprêtez à modifier la colonne %s. Êtes-vous sûr de votre choix ? [O/N] " % name)
    if answer == "O":
        return(name_id)
    elif answer == "N":
        return(getColumnToModify(namesColumns))
    else:
        return(sureToModify(name, name_id, namesColumns))


def getMetaModification(name_id, namesColumns, units, controlled, categories, list_categories):
    name = namesColumns[name_id]
    unit = units[name_id]
    constraint = controlled[name_id]
    category = categories[name_id]
    print("\nVoici les métadonnées actuelles de la colonne. Pour les modifier, taper la nouvelle valeur. Pour ne pas les changer, \
taper entrée. Pour une valeur vide, taper NULL.")
    newName = input("Nom de la colonne : %s " % name)
    if newName == "":
        newName = name
    elif newName == "NULL":
        print("Vous ne pouvez pas imposer un nom de colonne vide, réutilisons le nom initial.")
        newName = name
    
    if unit == None:
        newUnit = input("Pas d'unité actuellement, nouvelle unité ? ")
    else:
        newUnit = input("Unité : %s " % unit)
    if newUnit == "":
        newUnit = unit
    elif newUnit == "NULL":
        newUnit = None
    
    newConstraint = input("/!\\ Syntaxe /!\\ Contrainte actuelle : %s " % constraint)
    if newConstraint == "":
        newConstraint = constraint
    elif newConstraint == "NULL":
        print("Vous ne pouvez pas être indécis sur cette colonne. Réutilisons la contrainte précédente.")
        newConstraint = constraint
    
    print("Voici la liste des catégories d'affichage déjà existantes : ")
    print(list_categories)
    try:
        newCategory = input("Catégorie actuelle : %s " % category)
    except:
        print("Vous ne pouvez pas changer la catégorie de cette colonne, elle s'affiche par défaut.")
        newCategory = None
    if newCategory == "":
        newCategory = category
    elif newCategory == "NULL":
        print("Cette colonne sera donc affichée par défaut quelle que soit la catégorie d'affichage choisie.")
        newCategory = None

    return(newName, newUnit, newConstraint, newCategory)


def buildMetaRequest(newName, newUnit, newConstraint, newCategory, supportTable, name_id, columns):
    column = columns[name_id]
    #Create the requests to change the metadatas
    if supportTable == "NameMateriaux":
        supportColumn = "n_m_date"
    elif supportTable == "NamePieces":
        supportColumn = "n_p_date"
    
    request1 = """UPDATE %s SET n_%s = "%s" WHERE %s = 'Date de modification';""" %(supportTable, column, newName, supportColumn)
    request2 = "UPDATE %s SET n_%s = '%s' WHERE %s = 'False';" %(supportTable, column, newConstraint, supportColumn)
    if newCategory != None:
        request3 = """UPDATE %s SET n_%s = '%s' WHERE %s = 'métadonnées';""" %(supportTable, column, newCategory, supportColumn)
    else:
        request3 = "UPDATE %s SET n_%s = NULL WHERE %s = 'métadonnées';" %(supportTable, column, supportColumn)
    if newUnit != None:
        request4 = """UPDATE %s SET n_%s = "%s" WHERE %s <=> NULL;""" %(supportTable, column, newUnit, supportColumn)
    else:
        request4 = "UPDATE %s SET n_%s = NULL WHERE %s <=> NULL;" %(supportTable, column, supportColumn)
    return (request1, request2, request3, request4)


def executeMeta(request1, request2, request3, request4, cursor):
    try:
        cursor.execute(request1)
        print("Nom de la colonne mis à jour.")
        cursor.execute(request2)
        print("Contrainte de la colonne mise à jour.")
        cursor.execute(request3)
        print("Catégorie d'affichage mise à jour.")
        cursor.execute(request4)
        print("Unité de la colonne mise à jour.")
    except:
        print("Une erreur est survenue. Il est conseillé de restaurer la sauvegarde, puis de recommencer en prenant garde à la syntaxe.")


def getFillModification(name_id, namesColumns, used_types, used_nulls, used_defaults):
    name = namesColumns[name_id]
    used_type = used_types[name_id]
    used_null = used_nulls[name_id]
    used_default = used_defaults[name_id]
    print("\nVoici les données actuelles contraignant le remplissage de la colonne %s. Pour les modifier, taper la nouvelle valeur. Pour ne pas les changer, \
taper entrée. Pour une valeur vide, taper NULL." % name)
    
    newType = input("/!\\ Syntaxe /!\\ Type : %s " % used_type)
    if newType == "":
        newType = used_type
    elif newType == "NULL":
        print("Vous ne pouvez pas imposer un type nul. Par conséquent, gardons le type précédent.")
        newType = used_type
    
    if used_default == None:
        newDefault = input("Pas de valeur par défaut pour le moment. En imposer une ? ")
    else:
        newDefault = input("Défaut : %s " % used_default)
    if newDefault == "":
        newDefault = used_default
    elif newDefault == "NULL":
        newDefault = None
    
    if used_null == "NO":
        newNull = input("La colonne ne peut pas être vide. Laisser ainsi ? Taper YES sinon. ")
    elif used_null == "YES":
        newNull = input("La colonne peut être vide. Laisser ainsi ? Taper NO sinon. ")
    if newNull == "" or newNull == "NULL":
        newNull = used_null
    
    return(newType, newDefault, newNull)


def buildFillRequest(newType, newDefault, newNull, usedTable, columns, name_id):
    column = columns[name_id]

    if newNull == "YES":
        request1 = "SELECT 'Hello';"
        if newDefault == None:
            request = "ALTER TABLE %s MODIFY %s %s;" % (usedTable, column, newType)
        else:
            try:
                newDefault = float(newDefault)
                request = """ALTER TABLE %s MODIFY %s %s DEFAULT %d;""" % (usedTable, column, newType, newDefault)
            except:
                request = """ALTER TABLE %s MODIFY %s %s DEFAULT "%s";""" % (usedTable, column, newType, newDefault)


    elif newNull == "NO":
        if newDefault == None:
            request1 = "UPDATE %s SET %s = 'default' WHERE %s <=> NULL;" % (usedTable, column, column)
            request = "ALTER TABLE %s MODIFY %s %s NOT NULL;" % (usedTable, column, newType)
        else:
            try:
                newDefault = float(newDefault)
                request1 = "UPDATE %s SET %s = %d WHERE %s <=> NULL;" % (usedTable, column, newDefault, column)
                request = """ALTER TABLE %s MODIFY %s %s DEFAULT %d;""" % (usedTable, column, newType, newDefault)
            except:
                request1 = """UPDATE %s SET %s = "%s" WHERE %s <=> NULL;""" % (usedTable, column, newDefault, column)
                request = """ALTER TABLE %s MODIFY %s %s DEFAULT "%s";""" % (usedTable, column, newType, newDefault)
    return(request1, request)


def executeFill(request1, request, cursor):
    try:
        cursor.execute(request1)
        cursor.execute(request)
        print("La modification a bien été effectuée.")
    except:
        print("Une erreur est survenue. Vérifiez la syntaxe utilisée, la bonne correspondance des types avec la valeur par défaut, etc.")
    return()