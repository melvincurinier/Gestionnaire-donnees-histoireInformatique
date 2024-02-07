#------------------------------------------------------------
#        Script MySQL.
#------------------------------------------------------------
CREATE DATABASE IF NOT EXISTS `My_Database` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `My_Database`;

#------------------------------------------------------------
# Table: Technologie
#------------------------------------------------------------

CREATE TABLE Technologie(
        ID_technologie Int  Auto_increment  NOT NULL ,
        Titre          Char (20) NOT NULL ,
        Date           Date NOT NULL ,
        Description    Char (100) NOT NULL ,
        Type           Char (20) NOT NULL
	,CONSTRAINT Technologie_PK PRIMARY KEY (ID_technologie)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Evenement
#------------------------------------------------------------

CREATE TABLE Evenement(
        Id_Evenement Int  Auto_increment  NOT NULL ,
        Titre        Char (20) NOT NULL ,
        Date         Date NOT NULL ,
        Lieu         Char (20) NOT NULL ,
        Description  Char (100) NOT NULL
	,CONSTRAINT Evenement_PK PRIMARY KEY (Id_Evenement)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Entite
#------------------------------------------------------------

CREATE TABLE Entite(
        Id_Entite   Int  Auto_increment  NOT NULL ,
        Nom         Varchar (100) ,
        Description Varchar (100) NOT NULL
	,CONSTRAINT Entite_PK PRIMARY KEY (Id_Entite)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Personne
#------------------------------------------------------------

CREATE TABLE Personne(
        Id_Entite         Int NOT NULL ,
        Prenom            Varchar (100) NOT NULL ,
        Date_de_naissance Date NOT NULL ,
        date_de_deces     Date ,
        Nom               Varchar (100) ,
        Description       Varchar (100) NOT NULL
	,CONSTRAINT Personne_PK PRIMARY KEY (Id_Entite)

	,CONSTRAINT Personne_Entite_FK FOREIGN KEY (Id_Entite) REFERENCES Entite(Id_Entite)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Entreprise
#------------------------------------------------------------

CREATE TABLE Entreprise(
        Id_Entite        Int NOT NULL ,
        Date_de_creation Date NOT NULL ,
        Nom              Varchar (100) ,
        Description      Varchar (100) NOT NULL
	,CONSTRAINT Entreprise_PK PRIMARY KEY (Id_Entite)

	,CONSTRAINT Entreprise_Entite_FK FOREIGN KEY (Id_Entite) REFERENCES Entite(Id_Entite)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: INVENTER
#------------------------------------------------------------

CREATE TABLE INVENTER(
        Id_Entite      Int NOT NULL ,
        ID_technologie Int NOT NULL
	,CONSTRAINT INVENTER_PK PRIMARY KEY (Id_Entite,ID_technologie)

	,CONSTRAINT INVENTER_Entite_FK FOREIGN KEY (Id_Entite) REFERENCES Entite(Id_Entite)
	,CONSTRAINT INVENTER_Technologie0_FK FOREIGN KEY (ID_technologie) REFERENCES Technologie(ID_technologie)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: ORGANISER
#------------------------------------------------------------

CREATE TABLE ORGANISER(
        Id_Entite    Int NOT NULL ,
        Id_Evenement Int NOT NULL
	,CONSTRAINT ORGANISER_PK PRIMARY KEY (Id_Entite,Id_Evenement)

	,CONSTRAINT ORGANISER_Entite_FK FOREIGN KEY (Id_Entite) REFERENCES Entite(Id_Entite)
	,CONSTRAINT ORGANISER_Evenement0_FK FOREIGN KEY (Id_Evenement) REFERENCES Evenement(Id_Evenement)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: APPARTENIR
#------------------------------------------------------------

CREATE TABLE APPARTENIR(
        Id_Entite          Int NOT NULL ,
        Id_Entite_Personne Int NOT NULL
	,CONSTRAINT APPARTENIR_PK PRIMARY KEY (Id_Entite,Id_Entite_Personne)

	,CONSTRAINT APPARTENIR_Entreprise_FK FOREIGN KEY (Id_Entite) REFERENCES Entreprise(Id_Entite)
	,CONSTRAINT APPARTENIR_Personne0_FK FOREIGN KEY (Id_Entite_Personne) REFERENCES Personne(Id_Entite)
)ENGINE=InnoDB;

```