#! /usr/bin/python3
# -*- coding: utf-8 -*-

import pymysql
import datetime


def askBackup():
    """Return 'O' or 'N'."""
    print("Attention, effectuer une sauvegarde effacera toute sauvegarde précédemment effectuée aujourd'hui.")
    answer = input("Souhaitez-vous effectuer une nouvelle sauvegarde de la base de données ? [O/N] ")

    if (answer == "O") or (answer == "N"):
        return(answer)

    else:
        return(askBackup())


def askRestore():
    """Return 'O' or 'N'"""
    print("Attention, restaurer une sauvegarde effacera toute modification effectuée depuis la sauvegarde.")
    answer = input("Souhaitez-vous restaurer une sauvegarde de la base de données ? [O/N] ")

    if (answer == "O") or (answer == "N"):
        return(answer)

    else:
        return(askRestore())


def dateBackup(date):
    """Returns the date of the backup to restore"""
    print("Date du jour : ", date)
    answer = input("Souhaitez-vous utiliser la date du jour ? [O/N]")

    if answer == "O":
        return(date)
    
    elif answer == "N":
        print("Quelle est la date de la backup que vous souhaitez restaurer ?")
        date = input("Entrez la date sous la forme aaaa-mm-jj : ")
        return(date)

    else:
        return(dateBackup(date))