#------------------------------------------------------------
#        Script MySQL.
#------------------------------------------------------------

CREATE DATABASE IF NOT EXISTS `my_data`;
USE `my_data`;

#------------------------------------------------------------
# Table: Personnalités
#------------------------------------------------------------

CREATE TABLE Personnalites(
        Id_personnalite   Int  Auto_increment  NOT NULL ,
        Prenom            Varchar (100) NOT NULL ,
        Date_de_naissance Date NOT NULL ,
        date_de_deces     Date ,
        Description       Char (255)
	,CONSTRAINT Personnalites_PK PRIMARY KEY (Id_personnalite)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Technologie
#------------------------------------------------------------

CREATE TABLE Technologie(
        ID_technologie Int  Auto_increment  NOT NULL ,
        Titre          Char (50) NOT NULL ,
        Date           Date NOT NULL ,
        Description    Char (255) NOT NULL ,
        Type           Char (50) NOT NULL
	,CONSTRAINT Technologie_PK PRIMARY KEY (ID_technologie)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Evenement
#------------------------------------------------------------

CREATE TABLE Evenement(
        Id_Evenement Int  Auto_increment  NOT NULL ,
        Titre        Char (50) NOT NULL ,
        Date         Date NOT NULL ,
        Lieu         Char (50) NOT NULL ,
        Description  Char (250) NOT NULL
	,CONSTRAINT Evenement_PK PRIMARY KEY (Id_Evenement)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Categorie
#------------------------------------------------------------

CREATE TABLE Categorie(
        Id_categorie Int NOT NULL ,
        Nom          Varchar (100) NOT NULL
	,CONSTRAINT Categorie_PK PRIMARY KEY (Id_categorie)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: participer
#------------------------------------------------------------

CREATE TABLE participer(
        Id_Evenement    Int NOT NULL ,
        Id_personnalite Int NOT NULL
	,CONSTRAINT participer_PK PRIMARY KEY (Id_Evenement,Id_personnalite)

	,CONSTRAINT participer_Evenement_FK FOREIGN KEY (Id_Evenement) REFERENCES Evenement(Id_Evenement)
	,CONSTRAINT participer_Personnalites0_FK FOREIGN KEY (Id_personnalite) REFERENCES Personnalites(Id_personnalite)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: associer
#------------------------------------------------------------

CREATE TABLE associer(
        ID_technologie Int NOT NULL ,
        Id_Evenement   Int NOT NULL
	,CONSTRAINT associer_PK PRIMARY KEY (ID_technologie,Id_Evenement)

	,CONSTRAINT associer_Technologie_FK FOREIGN KEY (ID_technologie) REFERENCES Technologie(ID_technologie)
	,CONSTRAINT associer_Evenement0_FK FOREIGN KEY (Id_Evenement) REFERENCES Evenement(Id_Evenement)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: appartenir
#------------------------------------------------------------

CREATE TABLE appartenir(
        Id_categorie Int NOT NULL ,
        Id_Evenement Int NOT NULL
	,CONSTRAINT appartenir_PK PRIMARY KEY (Id_categorie,Id_Evenement)

	,CONSTRAINT appartenir_Categorie_FK FOREIGN KEY (Id_categorie) REFERENCES Categorie(Id_categorie)
	,CONSTRAINT appartenir_Evenement0_FK FOREIGN KEY (Id_Evenement) REFERENCES Evenement(Id_Evenement)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: impliquer
#------------------------------------------------------------

CREATE TABLE impliquer(
        ID_technologie  Int NOT NULL ,
        Id_personnalite Int NOT NULL
	,CONSTRAINT impliquer_PK PRIMARY KEY (ID_technologie,Id_personnalite)

	,CONSTRAINT impliquer_Technologie_FK FOREIGN KEY (ID_technologie) REFERENCES Technologie(ID_technologie)
	,CONSTRAINT impliquer_Personnalites0_FK FOREIGN KEY (Id_personnalite) REFERENCES Personnalites(Id_personnalite)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Contenir
#------------------------------------------------------------

CREATE TABLE Contenir(
        ID_technologie Int NOT NULL ,
        Id_categorie   Int NOT NULL
	,CONSTRAINT Contenir_PK PRIMARY KEY (ID_technologie,Id_categorie)

	,CONSTRAINT Contenir_Technologie_FK FOREIGN KEY (ID_technologie) REFERENCES Technologie(ID_technologie)
	,CONSTRAINT Contenir_Categorie0_FK FOREIGN KEY (Id_categorie) REFERENCES Categorie(Id_categorie)
)ENGINE=InnoDB;


-- Ajout de données dans la table Personnalites
INSERT INTO Personnalites (Prenom, Date_de_naissance, date_de_deces, Description) VALUES 
('Alan', '1912-06-23', '1954-06-07', 'Mathématicien et cryptanalyste britannique'),
('Grace', '1906-12-09', '1992-01-01', 'Informaticienne américaine, pionnière du langage COBOL'),
('Dennis', '1941-09-09', '2011-10-12', 'Informaticien américain, co-créateur du langage C');

-- Ajout de données dans la table Technologie
INSERT INTO Technologie (Titre, Date, Description, Type) VALUES 
('COBOL', '1959-01-01', 'Langage de programmation impératif, utilisé principalement dans le domaine des affaires', 'Langage de programmation'),
('C', '1972-01-01', 'Langage de programmation procédural et impératif, largement utilisé dans le développement de systèmes', 'Langage de programmation'),
('Python', '1991-01-01', 'Langage de programmation interprété, multi-paradigme, orienté objet', 'Langage de programmation');

-- Ajout de données dans la table Evenement
INSERT INTO Evenement (Titre, Date, Lieu, Description) VALUES 
('Invention du langage C', '1972-01-01', 'Bell Labs', 'Invention du langage de programmation C par Dennis Ritchie et Ken Thompson'),
('Lancement de Python', '1991-02-20', 'CWI', 'Guido van Rossum publie la première version de Python'),
('Première utilisation de COBOL', '1960-01-01','', 'La première utilisation commerciale de COBOL est faite par GE');

-- Ajout de données dans la table Categorie
INSERT INTO Categorie (Id_categorie, Nom) VALUES 
(1, 'Langages de programmation'),
(2, 'Mathématiques'),
(3, 'Histoire de l informatique');

-- Ajout de données dans la table participer
INSERT INTO participer (Id_Evenement, Id_personnalite) VALUES 
(1, 3),
(2, 3),
(3, 1);

-- Ajout de données dans la table associer
INSERT INTO associer (ID_technologie, Id_Evenement) VALUES 
(2, 1),
(3, 2),
(1, 3);

-- Ajout de données dans la table appartenir
INSERT INTO appartenir (Id_categorie, Id_Evenement) VALUES 
(1, 1),
(1, 2),
(1, 3);

-- Ajout de données dans la table impliquer
INSERT INTO impliquer (ID_technologie, Id_personnalite) VALUES 
(2, 3),
(3, 1),
(1, 2);

-- Ajout de données dans la table Contenir
INSERT INTO Contenir (ID_technologie, Id_categorie) VALUES 
(1, 1),
(2, 1),
(3, 1);

```

