#!/usr/bin/python3

import pymysql
import Functions.connectionDb as conn

print("Attention, si vous continuez, vous effacerez toutes les entrées actuelles de la base de données.")
create = input("Souhaitez-vous continuer ? [C] Appuyer sur toute autre touche pour annuler.")

if create == "C":

    # Connection to db 
    username, password, date = conn.parametersWithPass()
    db, cursor = conn.connectionToDb(username, password=password)


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


    # Create the tables pieces and materiaux
    try:
        cursor.execute(sql1)
        print("Materiaux was successfully created")
        cursor.execute(sql2)
        print("Pieces was successfully created")
        db.commit()
        print("successfully committed")

    except:
        cursor.execute("SHOW WARNINGS;")
        warnings = cursor.fetchall()
        print("warnings : ", warnings)
        db.rollback()
        print("error")


    db.close()

else:
    print("L'opération a été abandonnée.")

