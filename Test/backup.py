#! /usr/bin/python3
# -*- coding: utf-8 -*-

import pymysql
import subprocess
import Functions.connectionDb as conn
import Functions.backup as fct

# Get the information to create the name of the file
user_name, date = conn.parameters()

answerBackup = fct.askBackup()

# Create the path to the folder where the backups are stored

if answerBackup == "O":

# On windows : add Path (with command ? execute the right command to set the path before ?)
    
    try:
        subprocess.run("mysqldump -u %s --opt TestDB > TestDB_%s.sql" % (user_name, date), shell=True)
        # No idea why I needed to add shell=True
        print("La sauvegarde de la base de données a bien été effectuée.")
    
    except:
        print("La sauvegarde a échoué.")    
    
    print("Sortie du programme.")

else: # Considering nobody is willing to save the database and then restore another version. Should be change ?
    # Also knowing the program can just be run two times if someone wants it.
    answerRestore = fct.askRestore()

    if answerRestore == "O":
        dateBackup = fct.dateBackup(date)
        
        try:
            subprocess.run("mysql -u %s TestDB < TestDB_%s.sql" % (user_name, dateBackup), shell=True)
            # To restore, the DB should already be created. Create the DB manually if you are importing it on a new device.
            print("Les données en date du %s ont bien été restaurées." % dateBackup)
        
        except:
            print("Une erreur est survenue lors de la restauration des données.")    

        print("Sortie du programme.")

    else:
        print("Sortie du programme sans aucune action.")


# TODO Restaurer la dernière sauvegarde
# TODO Restaurer une sauvegarde plus ancienne (entrer la date manuellement)
