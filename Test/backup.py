#! /usr/bin/python3
# -*- coding: utf-8 -*-

import pymysql
import Functions.connectionDb as conn
import subprocess


subprocess.run("mysqldump -u xorielle --opt TestDB > testPython.sql", shell=True)
# No idea why I needed to add shell=True
# On windows : add Path (with command ? execute the right command to set the path before ?)