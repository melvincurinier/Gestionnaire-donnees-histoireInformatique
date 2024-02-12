import mysql.connector as MC



def ajouter():
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user = 'root',
            password = 'root'
        )
        cursor = conn.cursor()
        req = 'INSERT INTO personnalites(Id_personnalite, Prenom, Date_de_naissance, Date_de_deces, Description) VALUES (%s, %s, %s, %s, %s)'
        infos = (cursor.lastrowid, 'Albert', '1879-03-14', '1955-04-18', 'Physicien théoricien')
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

def modifier():
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user = 'root',
            password = 'root'
        )
        cursor = conn.cursor()
        req = 'UPDATE personnalites SET Prenom = %s WHERE Id_personnalite = %s'
        infos = ('Albert', 1)
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

def supprimer():
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = 'root'
        )
        cursor = conn.cursor()
        req = 'DELETE FROM personnalites WHERE Id_personnalite = %s'
        infos = (5,)
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

def afficher():
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = 'root'
        )
        cursor = conn.cursor()
        req = 'SELECT * FROM personnalites'
        cursor.execute(req)
        persolist = cursor.fetchall()
        for perso in persolist:
            print('Prenom : {}'.format(perso[1]), 'Date de naissance : {}'.format(perso[2]), 'Date de deces : {}'.format(perso[3]), 'Description : {}'.format(perso[4]))
    except MC.Error as e:
        print(e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

def rechercher():
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = 'root'
        )
        cursor = conn.cursor()
        req = 'SELECT * FROM personnalites WHERE Prenom = %s'
        infos = ('Albert',)
        cursor.execute(req, infos)
        persolist = cursor.fetchall()
        for perso in persolist:
            print('Prenom : {}'.format(perso[1]))
    except MC.Error as e:
        print(e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

def main():
    print('1. Ajouter')
    print('2. Modifier')
    print('3. Supprimer')
    print('4. Afficher')
    print('5. Rechercher')
    choix = int(input('Faites votre choix : '))
    if choix == 1:
        ajouter()
    elif choix == 2:
        modifier()
    elif choix == 3:
        supprimer()
    elif choix == 4:
        afficher()
    elif choix == 5:
        rechercher()
    else:
        print('Choix invalide')

if __name__ == '__main__':
    main()

