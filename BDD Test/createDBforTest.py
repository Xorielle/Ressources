#!/usr/bin/python3

"""This file is dedicated only to create the database for the test file.
It allows that the tests' results don't have to be renewed each time a line is modified in the working database"""

import pymysql 

def prepareTest():
    # Connection to db with user xorielle
    db = pymysql.connect('localhost','xorielle','','Test')
    cursor = db.cursor()


    # Clean the tables that already exist
    cursor.execute("DROP TABLE IF EXISTS Pieces;") # Attention au sens ! A cause de la FK, il faut drop Pieces avant
    cursor.execute("DROP TABLE IF EXISTS Materiaux;")
    print("cleaning ok")


    # Prepare the SQL queries to create the tables
    sql1 = """CREATE TABLE IF NOT EXISTS Materiaux (
        id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
        t_m_date DATE NOT NULL,
        t_m_nommodif VARCHAR(12) NOT NULL,
        t_m_nom VARCHAR(12) DEFAULT "do not know",
        t_m_famille VARCHAR(12),
        t_m_prix FLOAT UNSIGNED,
        t_m_massevolumique FLOAT UNSIGNED,
        t_m_durabilite_aqueux TINYINT,
        t_m_application TEXT,
        PRIMARY KEY (id),
        INDEX idx_materiau (t_m_nom(12))
        )
        ENGINE=INNODB;"""


    sql2 = """CREATE TABLE IF NOT EXISTS Pieces (
        id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
        t_p_date DATE NOT NULL,
        t_p_nommodif VARCHAR(12) NOT NULL,
        t_p_nom VARCHAR(12),
        t_p_materiau VARCHAR(12) DEFAULT "do not know",
        t_p_longueur FLOAT UNSIGNED,
        t_p_quantite TINYINT UNSIGNED,
        t_p_etat TINYINT,
        t_p_outil VARCHAR(48),
        PRIMARY KEY(id),
        CONSTRAINT fk_materiau_piece FOREIGN KEY (t_p_materiau) REFERENCES Materiaux(t_m_nom)
        )
        ENGINE=INNODB;"""


    # Prepare the sql requests to fill the table with basics information for further work
    sql3 = """INSERT INTO Materiaux VALUES (1, '2020-07-06', 'xorielle', 'sapin', 'organique', NULL, 450, 2, 'extérieur, construction'),
     (2, '2020-07-06', 'xorielle', 'chêne', 'organique', 12, 800, 3, 'extérieur, jardin, construction'),
     (3, '2020-07-07', 'xorielle', 'cuivre', 'métal', 32, 8800, 4, 'tuyaux, câbles'),
     (4, '2020-07-08', 'A M-R', 'caoutchouc', 'polymère', NULL, NULL, 2, NULL),
     (5, '2020-07-10', 'Amina', 'verre', 'céramique', NULL, NULL, 5, 'vitres, extérieur, serre (jardin)'),
     (6, '2020-07-12', 'Amina', 'chêne vernis', 'organique', NULL, NULL, NULL, 'meuble (l''arbre dont proviennent les planches est très dur !)'''),
     (7, '2020-07-13', 'xorielle', 'pin', 'organique', 5, 450, NULL, 'idem sapin'),
     (8, '2020-07-13', 'xorielle', 'pin parasol', 'organique', 6.5, 450, 3, NULL),
     (9, '2020-07-13', 'xorielle', 'pomme de pin', 'organique', NULL, NULL, NULL, 'allume-feu'),
     (10, '2020-07-13', 'xorielle', 'pin maritime', 'organique', NULL, 450, 3, NULL),
     (11, '2020-07-13', 'xorielle', 'pin noir', 'organique', NULL, 450, NULL, NULL);"""

    sql4 = """INSERT INTO Pieces VALUES (1, '2020-07-08', 'xorielle', 'planche', 'sapin', 120, 42, 3, 'scie, clous, vernis'), 
     (2, '2020-07-08', 'xorielle', 'planche', 'chêne', 150, 3, 3, 'scie, vernis'),
     (3, '2020-07-10', 'Amina', 'rondin', 'chêne', 30, 6, 4, 'hâche, scie'),
     (4, '2020-07-10', 'A M-R', 'tuyau', 'cuivre', 150, 24, 1, NULL),
     (5, '2020-07-14', 'A M-R', 'planche', 'pin parasol', 210, 12, 4, 'scie'),
     (6, '2020-07-14', 'xorielle', 'planches', 'pin maritime', 180, 13, 2, 'scier');"""


    # Create the tables pieces and materiaux
    try:
        cursor.execute(sql1)
        print("Materiaux was successfully created")
        cursor.execute(sql2)
        print("Pieces was successfully created")
        cursor.execute(sql3)
        print("Materiaux was successfully filled")
        cursor.execute(sql4)
        print("Pieces was successfully filled")
        db.commit()
        print("successfully committed")

    except:
        cursor.execute("SHOW WARNINGS;")
        warnings = cursor.fetchall()
        print("warnings : ", warnings)
        db.rollback()
        print("error")

    db.close()
    return(db, cursor)