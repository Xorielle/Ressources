#! /usr/bin/python3
# -*- coding: utf-8 -*-

import pymysql
import datetime


def parameters():
    """Fetch the username, password and the date to backup the system
    Return (user_name, password, date)"""
    user_name = input('Qui utilise la BDD (super-utilisateur) ? ')
    password = input('Mot de passe : ')
    full_date = datetime.datetime.now()
    date = "%s-%s-%s" % (full_date.strftime("%Y"), full_date.strftime("%m"), full_date.strftime("%d"))
    print("Date du jour : ", date)
    
    return(user_name, password, date)