import mysql.connector as MC
from datetime import datetime



def ajouter_une_personnalité(Prenom, Date_de_naissance, Date_de_deces, Description):
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user = 'root',
            password = ''
        )
        cursor = conn.cursor()
        req = 'INSERT INTO personnalites(Id_personnalite, Prenom, Date_de_naissance, Date_de_deces, Description) VALUES (%s, %s, %s, %s, %s)'
        Date_de_naissance_str = datetime.strptime(Date_de_naissance, '%Y-%m-%d')
        Date_de_deces_str = datetime.strptime(Date_de_deces, '%Y-%m-%d')
        infos = (cursor.lastrowid, Prenom, Date_de_naissance_str, Date_de_deces_str, Description)
        cursor.execute(req, infos)
        conn.commit()
        print('Ajout effectué avec succès')
    except MC.Error as e:
        print(e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

def ajouter_une_technologie(Nom, Date_de_creation, Description, Type):
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = ''
        )
        cursor = conn.cursor()
        req = 'INSERT INTO technologie(ID_technologie, Titre, Date, Description, Type) VALUES (%s, %s, %s, %s, %s)'
        Date_de_creation_str = datetime.strptime(Date_de_creation, '%Y-%m-%d')
        infos = (cursor.lastrowid, Nom, Date_de_creation_str, Description, Type)
        cursor.execute(req, infos)
        conn.commit()
        print('Ajout effectué avec succès')
    except MC.Error as e:
        print(e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

def ajouter_un_evenement(Titre, Date, Lieu, Description):
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = ''
        )
        cursor = conn.cursor()
        req = 'INSERT INTO evenement(Id_Evenement, Titre, Date, Lieu, Description) VALUES (%s, %s, %s, %s, %s)'
        Date_str = datetime.strptime(Date, '%Y-%m-%d')
        infos = (cursor.lastrowid, Titre, Date_str, Lieu, Description)
        cursor.execute(req, infos)
        conn.commit()
        print('Ajout effectué avec succès')
    except MC.Error as e:
        print(e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")
    
def ajouter_une_categorie(Nom):
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = 'root'
        )
        cursor = conn.cursor()
        req = 'INSERT INTO categorie(Id_categorie, Nom) VALUES (%s, %s)'
        infos = (cursor.lastrowid, Nom)
        cursor.execute(req, infos)
        conn.commit()
        print('Ajout effectué avec succès')
    except MC.Error as e:
        print(e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")