import customtkinter as ctk
from tkinter import Label, Button, Entry, Listbox, Text
from models.modifier import *

class UpdateDataView(ctk.CTkFrame):
    def __init__(self, parent, app, category, data):
        ctk.CTkFrame.__init__(self, parent)

        self.app = app
        self.category = category

        # Frame pour le titre
        title_frame = ctk.CTkFrame(self)
        title_frame.pack(side='top', fill='x')

        # Bouton "Retour"
        return_button = Button(title_frame, text='Retour', command=app.switch_to_menu_view)
        return_button.grid(row=0, column=0, padx=5, pady=5, sticky='w')

        # Titre principal
        title_label = Label(title_frame, text='Modifier une donnée')
        title_label.grid(row=0, column=1, padx=10)

        # Frame pour les champs de recherche
        self.updateData_frame = ctk.CTkFrame(self)
        self.updateData_frame.pack(fill='x', padx=10, pady=10)

        # Catégorie
        Label(self.updateData_frame, text='Catégorie:').grid(row=0, column=0, padx=5, pady=5)
        Label(self.updateData_frame, text=category).grid(row=0, column=1, padx=5, pady=5)

        self.entries = []

        # Bouton de recherche
        self.update_button = Button(self.updateData_frame, text='Modifier', command=lambda: self.perform_update_element(data[0]))
        self.update_button.grid(row=2, column=0, columnspan=2, pady=10)

        if category == 'Personnalité':
            self.create_personality_update_fields(data)
        elif category == 'Entreprise':
            self.create_company_update_fields(data)
        elif category == 'Technologie':
            self.create_technology_update_fields(data)
        elif category == 'Evénement':
            self.create_event_update_fields(data)
        elif category == 'Prix':
            self.create_price_update_fields(data)

        print("update Data View initiated !")
            
    def clear_entries(self):
        for entry in self.entries:
            entry.destroy()
        self.entries = []

    def create_personality_update_fields(self, data):
        label_lastname = Label(self.updateData_frame, text='Nom:')
        label_lastname.grid(row=1, column=0, padx=5, pady=5)
        entry_lastname = Entry(self.updateData_frame)
        entry_lastname.insert(0, data[1])
        entry_lastname.grid(row=1, column=1, padx=5, pady=5)

        self.entries.append(label_lastname)
        self.entries.append(entry_lastname)

        label_birthdate = Label(self.updateData_frame, text='Année de naissance:')
        label_birthdate.grid(row=2, column=0, padx=5, pady=5)
        entry_birthdate = Entry(self.updateData_frame)
        entry_birthdate.insert(0, data[2])
        entry_birthdate.grid(row=2, column=1, padx=5, pady=5)
        
        self.entries.append(label_birthdate)
        self.entries.append(entry_birthdate)

        label_deathdate = Label(self.updateData_frame, text='Année de décès:')
        label_deathdate.grid(row=3, column=0, padx=5, pady=5)
        entry_deathdate = Entry(self.updateData_frame)
        entry_deathdate.insert(0, data[3])
        entry_deathdate.grid(row=3, column=1, padx=5, pady=5)
        
        self.entries.append(label_deathdate)
        self.entries.append(entry_deathdate)

        label_description = Label(self.updateData_frame, text='Description:')
        label_description.grid(row=4, column=0, padx=5, pady=5)
        entry_description = Text(self.updateData_frame, height=5)
        entry_description.insert("1.0", data[4])
        entry_description.grid(row=4, column=1, padx=5, pady=5)

        self.entries.append(label_description)
        self.entries.append(entry_description)

        self.update_button.grid(row=5, column=1, columnspan=2, pady=10)

    def create_company_update_fields(self, data):
        label_company_name = Label(self.updateData_frame, text='Nom:')
        label_company_name.grid(row=1, column=0, padx=5, pady=5)
        entry_company_name = Entry(self.updateData_frame)
        entry_company_name.insert(0, data[1])
        entry_company_name.grid(row=1, column=1, padx=5, pady=5)

        self.entries.append(label_company_name)
        self.entries.append(entry_company_name)

        label_location = Label(self.updateData_frame, text='Emplacement:')
        label_location.grid(row=2, column=0, padx=5, pady=5)
        entry_location = Entry(self.updateData_frame)
        entry_location.insert(0, data[2])
        entry_location.grid(row=2, column=1, padx=5, pady=5)

        self.entries.append(label_location)
        self.entries.append(entry_location)

        label_creationdate = Label(self.updateData_frame, text='Année de création:')
        label_creationdate.grid(row=3, column=0, padx=5, pady=5)
        entry_creationdate = Entry(self.updateData_frame)
        entry_creationdate.insert(0, data[3])
        entry_creationdate.grid(row=3, column=1, padx=5, pady=5)

        self.entries.append(label_creationdate)
        self.entries.append(entry_creationdate)

        label_description = Label(self.updateData_frame, text='Description:')
        label_description.grid(row=4, column=0, padx=5, pady=5)
        entry_description = Text(self.updateData_frame, height=5)
        entry_description.insert("1.0", data[4])
        entry_description.grid(row=4, column=1, padx=5, pady=5)

        self.entries.append(label_description)
        self.entries.append(entry_description)

        self.update_button.grid(row=5, column=1, columnspan=2, pady=10)

    def create_technology_update_fields(self, data):
        label_name = Label(self.updateData_frame, text='Nom:')
        label_name.grid(row=1, column=0, padx=5, pady=5)
        entry_name = Entry(self.updateData_frame)
        entry_name.insert(0, data[1])
        entry_name.grid(row=1, column=1, padx=5, pady=5)

        self.entries.append(label_name)
        self.entries.append(entry_name)

        label_type = Label(self.updateData_frame, text='Type:')
        label_type.grid(row=2, column=0, padx=5, pady=5)
        entry_type = Entry(self.updateData_frame)
        entry_type.insert(0, data[2])
        entry_type.grid(row=2, column=1, padx=5, pady=5)

        self.entries.append(label_type)
        self.entries.append(entry_type)

        label_year = Label(self.updateData_frame, text='Année de création:')
        label_year.grid(row=3, column=0, padx=5, pady=5)
        entry_year = Entry(self.updateData_frame)
        entry_year.insert(0, data[3])
        entry_year.grid(row=3, column=1, padx=5, pady=5)

        self.entries.append(label_year)
        self.entries.append(entry_year)

        label_description = Label(self.updateData_frame, text='Description:')
        label_description.grid(row=4, column=0, padx=5, pady=5)
        entry_description = Text(self.updateData_frame, height=5)
        entry_description.insert("1.0", data[4])
        entry_description.grid(row=4, column=1, padx=5, pady=5)

        self.entries.append(label_description)
        self.entries.append(entry_description)

        self.update_button.grid(row=5, column=1, columnspan=2, pady=10)

    def create_event_update_fields(self, data):
        label_event_title = Label(self.updateData_frame, text='Titre:')
        label_event_title.grid(row=1, column=0, padx=5, pady=5)
        entry_event_title = Entry(self.updateData_frame)
        entry_event_title.insert(0, data[1])
        entry_event_title.grid(row=1, column=1, padx=5, pady=5)

        self.entries.append(label_event_title)
        self.entries.append(entry_event_title)

        label_date = Label(self.updateData_frame, text='Date:')
        label_date.grid(row=2, column=0, padx=5, pady=5)
        entry_date = Entry(self.updateData_frame)
        entry_date.insert(0, data[2])
        entry_date.grid(row=2, column=1, padx=5, pady=5)

        self.entries.append(label_date)
        self.entries.append(entry_date)

        label_location = Label(self.updateData_frame, text='Lieu:')
        label_location.grid(row=3, column=0, padx=5, pady=5)
        entry_location = Entry(self.updateData_frame)
        entry_location.insert(0, data[3])
        entry_location.grid(row=3, column=1, padx=5, pady=5)

        self.entries.append(label_location)
        self.entries.append(entry_location)

        label_description = Label(self.updateData_frame, text='Description:')
        label_description.grid(row=4, column=0, padx=5, pady=5)
        entry_description = Text(self.updateData_frame, height=5)
        entry_description.insert("1.0", data[4])
        entry_description.grid(row=4, column=1, padx=5, pady=5)

        self.entries.append(label_description)
        self.entries.append(entry_description)

        self.update_button.grid(row=5, column=1, columnspan=2, pady=10)

    def create_price_update_fields(self, data):
        label_price_name = Label(self.updateData_frame, text='Nom:')
        label_price_name.grid(row=1, column=0, padx=5, pady=5)
        entry_price_name = Entry(self.updateData_frame)
        entry_price_name.insert(0, data[1])
        entry_price_name.grid(row=1, column=1, padx=5, pady=5)

        self.entries.append(label_price_name)
        self.entries.append(entry_price_name)

        label_year = Label(self.updateData_frame, text='Année de création:')
        label_year.grid(row=2, column=0, padx=5, pady=5)
        entry_year = Entry(self.updateData_frame)
        entry_year.insert(0, data[2])
        entry_year.grid(row=2, column=1, padx=5, pady=5)

        self.entries.append(label_year)
        self.entries.append(entry_year)

        label_description = Label(self.updateData_frame, text='Description:')
        label_description.grid(row=3, column=0, padx=5, pady=5)
        entry_description = Text(self.updateData_frame, height=5)
        entry_description.insert("1.0", data[3])
        entry_description.grid(row=3, column=1, padx=5, pady=5)

        self.entries.append(label_description)
        self.entries.append(entry_description)

        self.update_button.grid(row=4, column=1, columnspan=2, pady=10)

    def perform_update_element(self, id):
        data=[]
        for widget in self.entries:
            if isinstance(widget, Entry):
                value = widget.get()
                data.append(value)
            if isinstance(widget, Text):
                value = widget.get("1.0", "end-1c")
                data.append(value)
        if self.category == "Personnalité":
            modifier_prenom_une_personnalite(data[0], id)
            modifier_date_de_naissance_une_personnalite(data[1], id)
            modifier_date_de_deces_une_personnalite(data[2], id)
            modifier_description_une_personnalite(data[3], id)
        elif self.category == "Technologie":
            modifier_nom_une_technologie(data[0], id)
            modifier_date_de_creation_une_technologie(data[1], id)
            modifier_type_une_technologie(data[2], id)
            modifier_description_une_technologie(data[3], id)
        elif self.category == "Evénement":
            modifier_titre_un_evenement(data[0], id)
            modifier_date_un_evenement(data[1], id)
            modifier_lieu_un_evenement(data[2], id)
            modifier_description_un_evenement(data[3], id)
        
        self.app.switch_to_menu_view()
