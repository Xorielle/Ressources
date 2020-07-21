#! /usr/bin/python3
# -*- coding: utf-8 -*-

import pymysql
import subprocess
import Functions.connectionDb as conn
import Functions.backup as fct

# Get the information to create the name of the file
user_name, date = conn.parameters()

subprocess.run("mysqldump -u %s --opt TestDB > TestDB_%s.sql" % (user_name, date), shell=True)
print("La sauvegarde de la base de données a bien été effectuée.")
# No idea why I needed to add shell=True
# On windows : add Path (with command ? execute the right command to set the path before ?)

# TODO Restaurer la dernière sauvegarde
# TODO Restaurer une sauvegarde plus ancienne (entrer la date manuellement)


# Get the right information to have the name of the file
#user_name, password, date = fct.parameters()