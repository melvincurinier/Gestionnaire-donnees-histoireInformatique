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


# telechrger les resultats sous forme d'un fichier csv selon la fonction d'affichage
def telecharger_les_resultats():
    print('1. Télécharger les personnalités')
    print('2. Télécharger les technologies')
    print('3. Télécharger les événements')
    print('4. Télécharger les catégories')
    choix = int(input('Que voulez-vous faire ? : '))
    if choix == 1:
        telecharger_les_personnalites()
    elif choix == 2:
        telecharger_les_technologies()
    elif choix == 3:
        telecharger_les_evenements()
    elif choix == 4:
        telecharger_les_categories()
    else:
        print('Choix invalide')

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
            req = 'SELECT * FROM evenements'
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
            req = 'SELECT * FROM categories'
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


def main():
    print('1. Ajouter quelque chose')
    print('2. Modifier quelque chose')
    print('3. Supprimer quelque chose')
    print('4. Afficher quelque chose')
    print('5. Rechercher quelque chose')
    choix = int(input('Que voulez-vous faire ? : '))
    if choix == 1:
        print('1. Ajouter une personnalité')
        print('2. Ajouter une technologie')
        print('3. Ajouter un événement')
        print('4. Ajouter une catégorie')
        choix2 = int(input('Que voulez-vous faire ? : '))
        if choix2 == 1:
            ajouter_une_personnalité()
        elif choix2 == 2:
            ajouter_une_technologie()
        elif choix2 == 3:
            ajouter_un_evenement()
        elif choix2 == 4:
            ajouter_une_categorie()
        else:
            print('Choix invalide')
    elif choix == 2:
        print('1. Modifier une personnalité')
        print('2. Modifier une technologie')
        print('3. Modifier un événement')
        print('4. Modifier une catégorie')
        choix2 = int(input('Que voulez-vous faire ? : '))
        if choix2 == 1:
            modifier_une_personnalite()
        elif choix2 == 2:
            modifier_une_technologie()
        elif choix2 == 3:
            modifier_un_evenement()
        elif choix2 == 4:
            modifier_une_categorie()
        else:
            print('Choix invalide')
    elif choix == 3:
        print('1. Supprimer une personnalité')
        print('2. Supprimer une technologie')
        print('3. Supprimer un événement')
        print('4. Supprimer une catégorie')
        choix2 = int(input('Que voulez-vous faire ? : '))
        if choix2 == 1:
            supprimer_une_personnalite()
        elif choix2 == 2:
            supprimer_une_technologie()
        elif choix2 == 3:
            supprimer_un_evenement()
        elif choix2 == 4:
            supprimer_une_categorie()
        else:
            print('Choix invalide')
    elif choix == 4:
        print('1. Afficher les personnalités')
        print('2. Afficher les technologies')
        print('3. Afficher les événements')
        print('4. Afficher les catégories')
        choix2 = int(input('Que voulez-vous faire ? : '))
        if choix2 == 1:
            afficher_les_personnalites()
            print('Voulez-vous télécharger les résultats ?')
            choix2 = int(input('1. Oui\n2. Non\n'))
            if choix2 == 1:
                telecharger_les_personnalites()
            elif choix2 == 2:
                pass
            else:
                print('Choix invalide')
        elif choix == 2:
            afficher_les_technologies()
            print('Voulez-vous télécharger les résultats ?')
            choix2 = int(input('1. Oui\n2. Non\n'))
            if choix2 == 1:
                telecharger_les_technologies()
            elif choix2 == 2:
                pass
            else:
                print('Choix invalide')
        elif choix == 3:
            afficher_les_evenements()
            print('Voulez-vous télécharger les résultats ?')
            choix2 = int(input('1. Oui\n2. Non\n'))
            if choix2 == 1:
                telecharger_les_evenements()
            elif choix2 == 2:
                pass
            else:
                print('Choix invalide')
        elif choix == 4:
            afficher_les_categories()
            print('Voulez-vous télécharger les résultats ?')
            choix2 = int(input('1. Oui\n2. Non\n'))
            if choix2 == 1:
                telecharger_les_categories()
            elif choix2 == 2:
                pass
            else:
                print('Choix invalide')
        else:
            print('Choix invalide')
    elif choix == 5:
        print('1. Rechercher une personnalité')
        print('2. Rechercher une technologie')
        print('3. Rechercher un événement')
        print('4. Rechercher une catégorie')
        choix = int(input('Que voulez-vous faire ? : '))
        if choix2 == 1:
            rechercher_une_personnalite()
        elif choix2 == 2:
            rechercher_une_technologie()
        elif choix2 == 3:
            rechercher_un_evenement()
        elif choix2 == 4:
            rechercher_une_categorie()
        else:
            print('Choix invalide')

if __name__ == '__main__':
    main()