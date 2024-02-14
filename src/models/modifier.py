import mysql.connector as MC
from datetime import datetime


def modifier_prenom_une_personnalite(Prenom, Id_personnalite):
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user = 'root',
            password = ''
        )
        cursor = conn.cursor()
        req = 'UPDATE personnalites SET Prenom = %s WHERE Id_personnalite = %s'
        infos = (Prenom, Id_personnalite)
        cursor.execute(req, infos)
        conn.commit()
        print('Modification effectuée avec succès')
    except MC.Error as e:
        print(e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

def modifier_date_de_naissance_une_personnalite(Date_de_naissance, Id_personnalite):
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = 'root'
        )
        cursor = conn.cursor()
        req = 'UPDATE personnalites SET Date_de_naissance = %s WHERE Id_personnalite = %s'
        Date_de_naissance_str = datetime.strptime(Date_de_naissance, '%Y-%m-%d')
        infos = (Date_de_naissance_str, Id_personnalite)
        cursor.execute(req, infos)
        conn.commit()
        print('Modification effectuée avec succès')
    except MC.Error as e:
        print(e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

def modifier_date_de_deces_une_personnalite(Date_de_deces, Id_personnalite):
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = 'root'
        )
        cursor = conn.cursor()
        req = 'UPDATE personnalites SET Date_de_deces = %s WHERE Id_personnalite = %s'
        Date_de_deces_str = datetime.strptime(Date_de_deces, '%Y-%m-%d')
        infos = (Date_de_deces_str, Id_personnalite)
        cursor.execute(req, infos)
        conn.commit()
        print('Modification effectuée avec succès')
    except MC.Error as e:
        print(e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

def modifier_description_une_personnalite(Description, Id_personnalite):
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = 'root'
        )
        cursor = conn.cursor()
        req = 'UPDATE personnalites SET Description = %s WHERE Id_personnalite = %s'
        infos = (Description, Id_personnalite)
        cursor.execute(req, infos)
        conn.commit()
        print('Modification effectuée avec succès')
    except MC.Error as e:
        print(e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

def modifier_nom_une_technologie(Nom, Id_technologie):
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = 'root'
        )
        cursor = conn.cursor()
        req = 'UPDATE technologie SET Titre = %s WHERE ID_technologie = %s'
        infos = (Nom, Id_technologie)
        cursor.execute(req, infos)
        conn.commit()
        print('Modification effectuée avec succès')
    except MC.Error as e:
        print(e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

def modifier_date_de_creation_une_technologie(Date_de_creation, Id_technologie):
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = 'root'
        )
        cursor = conn.cursor()
        req = 'UPDATE technologie SET Date = %s WHERE ID_technologie = %s'
        Date_de_creation_str = datetime.strptime(Date_de_creation, '%Y-%m-%d')
        infos = (Date_de_creation_str, Id_technologie)
        cursor.execute(req, infos)
        conn.commit()
        print('Modification effectuée avec succès')
    except MC.Error as e:
        print(e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

def modifier_description_une_technologie(Description, Id_technologie):
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = 'root'
        )
        cursor = conn.cursor()
        req = 'UPDATE technologie SET Description = %s WHERE ID_technologie = %s'
        infos = (Description, Id_technologie)
        cursor.execute(req, infos)
        conn.commit()
        print('Modification effectuée avec succès')
    except MC.Error as e:
        print(e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

def modifier_type_une_technologie(Type, Id_technologie):
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = 'root'
        )
        cursor = conn.cursor()
        req = 'UPDATE technologie SET Type = %s WHERE ID_technologie = %s'
        infos = (Type, Id_technologie)
        cursor.execute(req, infos)
        conn.commit()
        print('Modification effectuée avec succès')
    except MC.Error as e:
        print(e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

def modifier_titre_un_evenement(Titre, Id_evenement):
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = 'root'
        )
        cursor = conn.cursor()
        req = 'UPDATE evenement SET Titre = %s WHERE Id_Evenement = %s'
        infos = (Titre, Id_evenement)
        cursor.execute(req, infos)
        conn.commit()
        print('Modification effectuée avec succès')
    except MC.Error as e:
        print(e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

def modifier_date_un_evenement(Date, Id_evenement):
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = 'root'
        )
        cursor = conn.cursor()
        req = 'UPDATE evenement SET Date = %s WHERE Id_Evenement = %s'
        Date_str = datetime.strptime(Date, '%Y-%m-%d')
        infos = (Date_str, Id_evenement)
        cursor.execute(req, infos)
        conn.commit()
        print('Modification effectuée avec succès')
    except MC.Error as e:
        print(e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

def modifier_lieu_un_evenement(Lieu, Id_evenement):
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = 'root'
        )
        cursor = conn.cursor()
        req = 'UPDATE evenement SET Lieu = %s WHERE Id_Evenement = %s'
        infos = (Lieu, Id_evenement)
        cursor.execute(req, infos)
        conn.commit()
        print('Modification effectuée avec succès')
    except MC.Error as e:
        print(e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

def modifier_description_un_evenement(Description, Id_evenement):
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = 'root'
        )
        cursor = conn.cursor()
        req = 'UPDATE evenement SET Description = %s WHERE Id_Evenement = %s'
        infos = (Description, Id_evenement)
        cursor.execute(req, infos)
        conn.commit()
        print('Modification effectuée avec succès')
    except MC.Error as e:
        print(e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")


def modifier_nom_une_categorie(Nom, Id_categorie):
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = 'root'
        )
        cursor = conn.cursor()
        req = 'UPDATE categorie SET Nom = %s WHERE Id_categorie = %s'
        infos = (Nom, Id_categorie)
        cursor.execute(req, infos)
        conn.commit()
        print('Modification effectuée avec succès')
    except MC.Error as e:
        print(e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")