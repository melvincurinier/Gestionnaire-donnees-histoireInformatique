import mysql.connector as MC
    
def supprimer_une_personnalite(Id_personnalite):
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = ''
        )
        cursor = conn.cursor()
        req = 'DELETE FROM personnalites WHERE Id_personnalite = %s'
        infos = (Id_personnalite,)
        cursor.execute(req, infos)
        conn.commit()
        print('Suppression effectuée avec succès')
    except MC.Error as e:
        print(e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

def supprimer_une_technologie(Id_technologie):
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = 'root'
        )
        cursor = conn.cursor()
        req = 'DELETE FROM technologie WHERE ID_technologie = %s'
        infos = (Id_technologie,)
        cursor.execute(req, infos)
        conn.commit()
        print('Suppression effectuée avec succès')
    except MC.Error as e:
        print(e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

def supprimer_un_evenement(Id_evenement):
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = 'root'
        )
        cursor = conn.cursor()
        req = 'DELETE FROM evenement WHERE Id_Evenement = %s'
        infos = (Id_evenement,)
        cursor.execute(req, infos)
        conn.commit()
        print('Suppression effectuée avec succès')
    except MC.Error as e:
        print(e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

def supprimer_une_categorie(Id_categorie):
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = 'root'
        )
        cursor = conn.cursor()
        req = 'DELETE FROM categorie WHERE Id_categorie = %s'
        infos = (Id_categorie,)
        cursor.execute(req, infos)
        conn.commit()
        print('Suppression effectuée avec succès')
    except MC.Error as e:
        print(e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")