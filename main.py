import mysql.connector as MC



def ajouter_une_personnalité():
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

def ajouter_une_technologie():
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = 'root'
        )
        cursor = conn.cursor()
        req = 'INSERT INTO technologies(Id_technologie, Nom, Date_de_creation, Description) VALUES (%s, %s, %s, %s)'
        infos = (cursor.lastrowid, 'Python', '1991-02-20', 'Langage de programmation')
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

def ajouter_un_evenement():
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = 'root'
        )
        cursor = conn.cursor()
        req = 'INSERT INTO evenements(Id_evenement, Titre, Date, Lieu) VALUES (%s, %s, %s, %s)'
        infos = (cursor.lastrowid, 'Création de Python', '1989-12-20', 'Pays-Bas')
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
    
def ajouter_une_categorie():
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = 'root'
        )
        cursor = conn.cursor()
        req = 'INSERT INTO categories(Id_categorie, Nom) VALUES (%s, %s)'
        infos = (cursor.lastrowid, 'Physique')
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




def modifier_une_personnalite():
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

def modifier_une_technologie():
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = 'root'
        )
        cursor = conn.cursor()
        req = 'UPDATE technologies SET Nom = %s WHERE Id_technologie = %s'
        infos = ('Python', 1)
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
    
def modifier_un_evenement():
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = 'root'
        )
        cursor = conn.cursor()
        req = 'UPDATE evenements SET Titre = %s WHERE Id_evenement = %s'
        infos = ('Création de Python', 1)
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

def modifier_une_categorie():
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = 'root'
        )
        cursor = conn.cursor()
        req = 'UPDATE categories SET Nom = %s WHERE Id_categorie = %s'
        infos = ('Physique', 1)
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
    
def supprimer_une_personnalite():
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

def supprimer_une_technologie():
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = 'root'
        )
        cursor = conn.cursor()
        req = 'DELETE FROM technologies WHERE Id_technologie = %s'
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

def supprimer_un_evenement():
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = 'root'
        )
        cursor = conn.cursor()
        req = 'DELETE FROM evenements WHERE Id_evenement = %s'
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

def supprimer_une_categorie():
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = 'root'
        )
        cursor = conn.cursor()
        req = 'DELETE FROM categories WHERE Id_categorie = %s'
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

def afficher_les_personnalites():
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

def afficher_les_technologies():
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = 'root'
        )
        cursor = conn.cursor()
        req = 'SELECT * FROM technologies'
        cursor.execute(req)
        techlist = cursor.fetchall()
        for tech in techlist:
            print('Nom : {}'.format(tech[1]), 'Date de création : {}'.format(tech[2]), 'Description : {}'.format(tech[3]))
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
            password = 'root'
        )
        cursor = conn.cursor()
        req = 'SELECT * FROM evenements'
        cursor.execute(req)
        evenlist = cursor.fetchall()
        for even in evenlist:
            print('Titre : {}'.format(even[1]), 'Date : {}'.format(even[2]), 'Lieu : {}'.format(even[3]))
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
        req = 'SELECT * FROM categories'
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

def rechercher_une_personnalite():
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

def rechercher_une_technologie():
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = 'root'
        )
        cursor = conn.cursor()
        req = 'SELECT * FROM technologies WHERE Nom = %s'
        infos = ('Python',)
        cursor.execute(req, infos)
        techlist = cursor.fetchall()
        for tech in techlist:
            print('Nom : {}'.format(tech[1]))
    except MC.Error as e:
        print(e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

def rechercher_un_evenement():
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = 'root'
        )
        cursor = conn.cursor()
        req = 'SELECT * FROM evenements WHERE Titre = %s'
        infos = ('Création de Python',)
        cursor.execute(req, infos)
        evenlist = cursor.fetchall()
        for even in evenlist:
            print('Titre : {}'.format(even[1]))
    except MC.Error as e:
        print(e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

def rechercher_une_categorie():
    try:
        conn = MC.connect(
            host="localhost",
            database = 'my_data',
            user ='root',
            password = 'root'
        )
        cursor = conn.cursor()
        req = 'SELECT * FROM categories WHERE Nom = %s'
        infos = ('Physique',)
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

def main():
    # laisse moi choisir ce que je veux faire
    print('1. Ajouter une personnalité')
    print('2. Ajouter une technologie')
    print('3. Ajouter un événement')
    print('4. Ajouter une catégorie')
    print('5. Modifier une personnalité')
    print('6. Modifier une technologie')
    print('7. Modifier un événement')
    print('8. Modifier une catégorie')
    print('9. Supprimer une personnalité')
    print('10. Supprimer une technologie')
    print('11. Supprimer un événement')
    print('12. Supprimer une catégorie')
    print('13. Afficher les personnalités')
    print('14. Afficher les technologies')
    print('15. Afficher les événements')
    print('16. Afficher les catégories')
    print('17. Rechercher une personnalité')
    print('18. Rechercher une technologie')
    print('19. Rechercher un événement')
    print('20. Rechercher une catégorie')
    choix = int(input('Que voulez-vous faire ? : '))
    if choix == 1:
        ajouter_une_personnalité()
    elif choix == 2:
        ajouter_une_technologie()
    elif choix == 3:
        ajouter_un_evenement()
    elif choix == 4:
        ajouter_une_categorie()
    elif choix == 5:
        modifier_une_personnalite()
    elif choix == 6:
        modifier_une_technologie()
    elif choix == 7:
        modifier_un_evenement()
    elif choix == 8:
        modifier_une_categorie()
    elif choix == 9:
        supprimer_une_personnalite()
    elif choix == 10:
        supprimer_une_technologie()
    elif choix == 11:
        supprimer_un_evenement()
    elif choix == 12:
        supprimer_une_categorie()
    elif choix == 13:
        afficher_les_personnalites()
    elif choix == 14:
        afficher_les_technologies()
    elif choix == 15:
        afficher_les_evenements()
    elif choix == 16:
        afficher_les_categories()
    elif choix == 17:
        rechercher_une_personnalite()
    elif choix == 18:
        rechercher_une_technologie()
    elif choix == 19:
        rechercher_un_evenement()
    elif choix == 20:
        rechercher_une_categorie()
    else:
        print('Choix invalide')

if __name__ == '__main__':
    main()