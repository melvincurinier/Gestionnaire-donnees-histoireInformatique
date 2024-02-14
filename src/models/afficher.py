import mysql.connector as MC

def afficher_les_personnalites():
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = ''
        )
        cursor = conn.cursor()
        req = 'SELECT * FROM personnalites'
        cursor.execute(req)
        persolist = cursor.fetchall()
        return persolist
    except MC.Error as e:
        print(e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

def afficher_une_personnalite(Prenom):
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = ''
        )
        cursor = conn.cursor()
        req = 'SELECT * FROM personnalites WHERE Prenom = %s'
        infos = (Prenom,)
        cursor.execute(req, infos)
        persolist = cursor.fetchall()
        return persolist
    except MC.Error as e:
        print(e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")



def afficher_les_technologies():
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = ''
        )
        cursor = conn.cursor()
        req = 'SELECT * FROM technologie'
        cursor.execute(req)
        techlist = cursor.fetchall()
        return techlist
    except MC.Error as e:
        print(e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

def afficher_une_technologie(Nom):
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = ''
        )
        cursor = conn.cursor()
        req = 'SELECT * FROM technologie WHERE Titre = %s'
        infos = (Nom,)
        cursor.execute(req, infos)
        techlist = cursor.fetchall()
        return techlist
    except MC.Error as e:
        print(e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")


def afficher_les_evenements():
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = ''
        )
        cursor = conn.cursor()
        req = 'SELECT * FROM evenement'
        cursor.execute(req)
        evenlist = cursor.fetchall()
        return evenlist
    except MC.Error as e:
        print(e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

def afficher_un_evenement(Titre):
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = ''
        )
        cursor = conn.cursor()
        req = 'SELECT * FROM evenement WHERE Titre = %s'
        infos = (Titre,)
        cursor.execute(req, infos)
        evenlist = cursor.fetchall()
        return evenlist
    except MC.Error as e:
        print(e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")


def afficher_les_categories():
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = 'root'
        )
        cursor = conn.cursor()
        req = 'SELECT * FROM categorie'
        cursor.execute(req)
        catlist = cursor.fetchall()
        for cat in catlist:
            print('Nom : {}'.format(cat[1]))
    except MC.Error as e:
        print(e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

def afficher_une_categorie(Nom):
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = 'root'
        )
        cursor = conn.cursor()
        req = 'SELECT * FROM categorie WHERE Nom = %s'
        infos = (Nom,)
        cursor.execute(req, infos)
        catlist = cursor.fetchall()
        for cat in catlist:
            print('Nom : {}'.format(cat[1]))
    except MC.Error as e:
        print(e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")