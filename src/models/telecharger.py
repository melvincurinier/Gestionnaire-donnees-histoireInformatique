import mysql.connector as MC

def telecharger_les_personnalites():
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = 'root'
        )
        cursor = conn.cursor()
        with open('personnalites.csv', 'w') as f:
            req = 'SELECT * FROM personnalites'
            cursor.execute(req)
            persolist = cursor.fetchall()
            for perso in persolist:
                f.write('Prenom : {}'.format(perso[1])+''+ 'Date de naissance : {}'.format(perso[2])+''+ 'Date de deces : {}'.format(perso[3])+''+ 'Description : {}'.format(perso[4]))
        print('Téléchargement effectué avec succès')
    except MC.Error as e:
        print(e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

def telecherger_une_personnalite(Prenom):
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = 'root'
        )
        cursor = conn.cursor()
        with open('personnalite.csv', 'w') as f:
            req = 'SELECT * FROM personnalites WHERE Prenom = %s'
            infos = (Prenom,)
            cursor.execute(req, infos)
            persolist = cursor.fetchall()
            for perso in persolist:
                f.write('Prenom : {}'.format(perso[1])+''+ 'Date de naissance : {}'.format(perso[2])+''+ 'Date de deces : {}'.format(perso[3])+''+ 'Description : {}'.format(perso[4]))
        print('Téléchargement effectué avec succès')
    except MC.Error as e:
        print(e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")


def telecharger_les_technologies():
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = 'root'
        )
        cursor = conn.cursor()
        with open('technologies.csv', 'w') as f:
            req = 'SELECT * FROM technologies'
            cursor.execute(req)
            techlist = cursor.fetchall()
            for tech in techlist:
                f.write('Nom : {}'.format(tech[1]) +''+ 'Date de création : {}'.format(tech[2]) +''+ 'Description : {}'.format(tech[3]))
        print('Téléchargement effectué avec succès')
    except MC.Error as e:
        print(e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

def telecharger_une_technologie(Nom):
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = 'root'
        )
        cursor = conn.cursor()
        with open('technologie.csv', 'w') as f:
            req = 'SELECT * FROM technologie WHERE Titre = %s'
            infos = (Nom,)
            cursor.execute(req, infos)
            techlist = cursor.fetchall()
            for tech in techlist:
                f.write('Nom : {}'.format(tech[1]) +''+ 'Date de création : {}'.format(tech[2]) +''+ 'Description : {}'.format(tech[3]))
        print('Téléchargement effectué avec succès')
    except MC.Error as e:
        print(e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")



def telecharger_les_evenements():
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = 'root'
        )
        cursor = conn.cursor()
        with open('evenements.csv', 'w') as f:
            req = 'SELECT * FROM evenement'
            cursor.execute(req)
            evenlist = cursor.fetchall()
            for even in evenlist:
                f.write('Titre : {}'.format(even[1]) +''+ 'Date : {}'.format(even[2]) +''+ 'Lieu : {}'.format(even[3]))
        print('Téléchargement effectué avec succès')
    except MC.Error as e:
        print(e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

def telecharger_un_evenement(Titre):
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = 'root'
        )
        cursor = conn.cursor()
        with open('evenement.csv', 'w') as f:
            req = 'SELECT * FROM evenement WHERE Titre = %s'
            infos = (Titre,)
            cursor.execute(req, infos)
            evenlist = cursor.fetchall()
            for even in evenlist:
                f.write('Titre : {}'.format(even[1]) +''+ 'Date : {}'.format(even[2]) +''+ 'Lieu : {}'.format(even[3]))
        print('Téléchargement effectué avec succès')
    except MC.Error as e:
        print(e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")


def telecharger_les_categories():
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = 'root'
        )
        cursor = conn.cursor()
        with open('categories.csv', 'w') as f:
            req = 'SELECT * FROM categorie'
            cursor.execute(req)
            catlist = cursor.fetchall()
            for cat in catlist:
                f.write('Nom : {}'.format(cat[1]))
        print('Téléchargement effectué avec succès')
    except MC.Error as e:
        print(e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

def telecharger_une_categorie(Nom):
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = 'root'
        )
        cursor = conn.cursor()
        with open('categorie.csv', 'w') as f:
            req = 'SELECT * FROM categorie WHERE Nom = %s'
            infos = (Nom,)
            cursor.execute(req, infos)
            catlist = cursor.fetchall()
            for cat in catlist:
                f.write('Nom : {}'.format(cat[1]))
        print('Téléchargement effectué avec succès')
    except MC.Error as e:
        print(e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")