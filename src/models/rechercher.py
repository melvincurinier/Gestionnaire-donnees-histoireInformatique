import mysql.connector as MC
from models import afficher


def rechercher_une_personnalite(Prenom):
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = ''
        )
        cursor = conn.cursor()
        return afficher.afficher_une_personnalite(Prenom)
    except MC.Error as e:
        print(e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

def rechercher_une_technologie(Nom):
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = ''
        )
        cursor = conn.cursor()
        return afficher.afficher_une_technologie(Nom)
    except MC.Error as e:
        print(e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

def rechercher_un_evenement(Titre):
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = 'root'
        )
        cursor = conn.cursor()
        afficher.afficher_un_evenement(Titre)
    except MC.Error as e:
        print(e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

def rechercher_une_categorie(Nom):
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = 'root'
        )
        cursor = conn.cursor()
        afficher.afficher_une_categorie(Nom)
    except MC.Error as e:
        print(e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")