import mysql.connector as MC
import afficher
import rechercher
import modifier
import supprimer
import telecharger
import ajouter

def main():
    print('Bienvenue dans le programme de gestion de données')
    print('1. Rechercher des données')
    print('2. Modifier des données')
    print('3. Supprimer des données')
    print('4. Télécharger des données')
    print('5. Ajouter des données')
    print('7. Quitter')
    choix = input('Entrez votre choix : ')
    if choix == '1':
        print('1. Rechercher une personnalité')
        print('2. Rechercher une technologie')
        print('3. Rechercher un événement')
        print('4. Retour')
        choix_recherche = input('Entrez votre choix : ')
        if choix_recherche == '1':
            print('Entrez le prénom de la personnalité que vous voulez rechercher')
            prenom = input('Prénom : ')
            rechercher.rechercher_une_personnalite(prenom)
        elif choix_recherche == '2':
            print('Entrez le nom de la technologie que vous voulez rechercher')
            nom = input('Nom : ')
            rechercher.rechercher_une_technologie(nom)
        elif choix_recherche == '3':
            print('Entrez le titre de l événement que vous voulez rechercher')
            titre = input('Titre : ')
            rechercher.rechercher_un_evenement(titre)
        elif choix_recherche == '4':
            main()
        else:
            print('Choix invalide')
            main()
    elif choix == '2':
        print('1. Modifier une personnalité')
        print('2. Modifier une technologie')
        print('3. Modifier un événement')
        print('4. Retour')
        choix_modifier = input('Entrez votre choix : ')
        if choix_modifier == '1':
            print('Entrez l id de la personnalité que vous voulez modifier')
            id_modifier_personnalite = input('Id : ')
            print('1. Modifier le prénom')
            print('2. Modifier la date de naissance')
            print('3. Modifier la date de décès')
            print('4. Modifier la description')
            print('5. Retour')
            choix_modifier_personnalite = input('Entrez votre choix : ')
            if choix_modifier_personnalite == '1':
                print('Entrez le nouveau prénom')
                prenom_personnalite_modifier = input('Prénom : ')
                modifier.modifier_prenom_une_personnalite(prenom_personnalite_modifier, id_modifier_personnalite)
            elif choix_modifier_personnalite == '2':
                print('Entrez la nouvelle date de naissance')
                date_de_naissance_personnalite_modifier = input('Date de naissance : ')
                modifier.modifier_date_de_naissance_une_personnalite(date_de_naissance_personnalite_modifier, id_modifier_personnalite)
            elif choix_modifier_personnalite == '3':
                print('Entrez la nouvelle date de décès')
                date_de_deces_personnalite_modifier = input('Date de décès : ')
                modifier.modifier_date_de_deces_une_personnalite(date_de_deces_personnalite_modifier, id_modifier_personnalite)
            elif choix_modifier_personnalite == '4':
                print('Entrez la nouvelle description')
                description_personnalite_modifier = input('Description : ')
                modifier.modifier_description_une_personnalite(description, id_modifier_personnalite)
            elif choix_modifier_personnalite == '5':
                main()
        elif choix_modifier == '2':
            print('Entrez l id de la technologie que vous voulez modifier')
            id_modifier_technologie = input('Id : ')
            print('1. Modifier le nom')
            print('2. Modifier la date de création')
            print('3. Modifier la description')
            print('4. Retour')
            choix_modifier_technologie = input('Entrez votre choix : ')
            if choix_modifier_technologie == '1':
                print('Entrez le nouveau nom')
                nom = input('Nom : ')
                modifier.modifier_nom_une_technologie(nom, id_modifier_technologie)
            elif choix_modifier_technologie == '2':
                print('Entrez la nouvelle date de création')
                date_de_creation = input('Date de création : ')
                modifier.modifier_date_de_creation_une_technologie(date_de_creation, id_modifier_technologie)
            elif choix_modifier_technologie == '3':
                print('Entrez la nouvelle description')
                description = input('Description : ')
                modifier.modifier_description_une_technologie(description, id_modifier_technologie)
            elif choix_modifier_technologie == '4':
                main()
        elif choix_modifier == '3':
            print('Entrez l id de l événement que vous voulez modifier')
            id_modifier_evenement = input('Id : ')
            print('1. Modifier le titre')
            print('2. Modifier la date')
            print('3. Modifier le lieu')
            print('4. Retour')
            choix_modifier_evenement = input('Entrez votre choix : ')
            if choix_modifier_evenement == '1':
                print('Entrez le nouveau titre')
                titre = input('Titre : ')
                modifier.modifier_titre_un_evenement(titre, id_modifier_evenement)
            elif choix_modifier_evenement == '2':
                print('Entrez la nouvelle date')
                date = input('Date : ')
                modifier.modifier_date_un_evenement(date, id_modifier_evenement)
            elif choix_modifier_evenement == '3':
                print('Entrez le nouveau lieu')
                lieu = input('Lieu : ')
                modifier.modifier_lieu_un_evenement(lieu, id_modifier_evenement)
            elif choix_modifier_evenement == '4':
                main()
        elif choix_modifier == '4':
            main()
        else:
            print('Choix invalide')
            main()
    elif choix == '3':
        print('1. Supprimer une personnalité')
        print('2. Supprimer une technologie')
        print('3. Supprimer un événement')
        print('4. Retour')
        choix_supprimer = input('Entrez votre choix : ')
        if choix_supprimer == '1':
            print('Entrez l id de la personnalité que vous voulez supprimer')
            id_supprimer_personnalite = input('id : ')
            supprimer.supprimer_une_personnalite(id_supprimer_personnalite)
        elif choix_supprimer == '2':
            print('Entrez l id de la technologie que vous voulez supprimer')
            id_supprimer_technologie = input('id : ')
            supprimer.supprimer_une_technologie(id_supprimer_technologie)
        elif choix_supprimer == '3':
            print('Entrez l id de l événement que vous voulez supprimer')
            id_supprimer_evenement = input('id : ')
            supprimer.supprimer_un_evenement(id_supprimer_evenement)
        elif choix_supprimer == '4':
            main()
        else:
            print('Choix invalide')
            main()
    elif choix == '4':
        print('1. Télécharger les personnalités')
        print('2. Télécharger les technologies')
        print('3. Télécharger les événements')
        print('4. Retour')
        choix_telecharger = input('Entrez votre choix : ')
        if choix_telecharger == '1':
            print('1. Télécharger toutes les personnalités')
            print('2. Télécharger une personnalité')
            print('3. Retour')
            choix_telecharger_personnalite = input('Entrez votre choix : ')
            if choix_telecharger_personnalite == '1':
                telecharger.telecharger_les_personnalites()
            elif choix_telecharger_personnalite == '2':
                print('Entrez le prénom de la personnalité que vous voulez télécharger')
                prenom_personnalite_telecherger = input('Prénom : ')
                telecharger.telecherger_une_personnalite(prenom_personnalite_telecherger)
            elif choix == '3':
                main()
            else:
                print('Choix invalide')
                main()
        elif choix_telecharger == '2':
            print('1. Télécharger toutes les technologies')
            print('2. Télécharger une technologie')
            print('3. Retour')
            choix_telecharger_technologie = input('Entrez votre choix : ')
            if choix_telecharger_technologie == '1':
                telecharger.telecharger_les_technologies()
            elif choix_telecharger_technologie == '2':
                print('Entrez le nom de la technologie que vous voulez télécharger')
                nom_technologie_telechrger = input('Nom : ')
                telecharger.telecharger_une_technologie(nom_technologie_telechrger)
            elif choix == '3':
                main()
            else:
                print('Choix invalide')
                main()
        elif choix_telecharger == '3':
            print('1. Télécharger tous les événements')
            print('2. Télécharger un événement')
            print('3. Retour')
            choix_telecharger_evenement = input('Entrez votre choix : ')
            if choix_telecharger_evenement == '1':
                telecharger.telecharger_les_evenements()
            elif choix_telecharger_evenement == '2':
                print('Entrez le titre de l événement que vous voulez télécharger')
                titre_evenemnet_telecharger = input('Titre : ')
                telecharger.telecharger_un_evenement(titre_evenemnet_telecharger)
            elif choix_telecharger_evenement == '3':
                main()
            else:
                print('Choix invalide')
                main()
        elif choix_telecharger == '4':
            main()
        else:
            print('Choix invalide')
            main()
    elif choix == '5':
        print('1. Ajouter une personnalité')
        print('2. Ajouter une technologie')
        print('3. Ajouter un événement')
        print('4. Retour')
        choix_ajouter = input('Entrez votre choix : ')
        if choix_ajouter == '1':
            print('Entrez le prénom de la personnalité')
            prenom_personnalite_ajouter = input('Prénom : ')
            print('Entrez la date de naissance de la personnalité')
            date_de_naissance_personnalite_ajouter = input('Date de naissance : ')
            print('Entrez la date de décès de la personnalité')
            date_de_deces_personnalite_ajouter = input('Date de décès : ')
            print('Entrez la description de la personnalité')
            description_personnalite_ajouter = input('Description : ')
            ajouter.ajouter_une_personnalité(prenom_personnalite_ajouter, date_de_naissance_personnalite_ajouter, date_de_deces_personnalite_ajouter, description_personnalite_ajouter)
        elif choix_ajouter == '2':
            print('Entrez le nom de la technologie')
            nom_technologie_ajouter = input('Nom : ')
            print('Entrez la date de création de la technologie')
            date_de_creation_technologie_ajouter = input('Date de création : ')
            print('Entrez la description de la technologie')
            description_technologie_ajouter = input('Description : ')
            print('Entrez le type de la technologie')
            type_technologie_ajouter = input('Type : ')
            ajouter.ajouter_une_technologie(nom_technologie_ajouter, date_de_creation_technologie_ajouter, description_technologie_ajouter, type_technologie_ajouter)
        elif choix_ajouter == '3':
            print('Entrez le titre de l événement')
            titre_evenement_ajouter = input('Titre : ')
            print('Entrez la date de l événement')
            date_evenement_ajouter = input('Date : ')
            print('Entrez le lieu de l événement')
            lieu_evenement_ajouter = input('Lieu : ')
            print('Entrez la description de l événement')
            description_evenement_ajouter = input('Description : ')
            ajouter.ajouter_un_evenement(titre_evenement_ajouter, date_evenement_ajouter, lieu_evenement_ajouter, description_evenement_ajouter)
        elif choix_ajouter == '4':
            main()
        else:
            print('Choix invalide')
            main()
    elif choix == '6':
        print('Merci d\'avoir utilisé le programme de gestion de données')
    else:
        print('Choix invalide')
        main()
    
main()
