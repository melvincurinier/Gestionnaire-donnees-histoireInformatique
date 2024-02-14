import customtkinter as ctk
from tkinter import Label, Button, Entry, Listbox, Text

class AddDataView(ctk.CTkFrame):
    def __init__(self, parent, app):
        ctk.CTkFrame.__init__(self, parent)

        self.app = app

        # Frame pour le titre
        title_frame = ctk.CTkFrame(self)
        title_frame.pack(side='top', fill='x')

        # Bouton "Retour"
        return_button = Button(title_frame, text='Retour', command=app.switch_to_menu_view)
        return_button.grid(row=0, column=0, padx=5, pady=5, sticky='w')

        # Titre principal
        title_label = Label(title_frame, text='Ajouter une nouvelle donnée')
        title_label.grid(row=0, column=1, padx=10)

        # Frame pour les champs de recherche
        self.addData_frame = ctk.CTkFrame(self)
        self.addData_frame.pack(fill='x', padx=10, pady=10)

        # Catégorie
        label_category = Label(self.addData_frame, text='Catégorie:')
        label_category.grid(row=0, column=0, padx=5, pady=5)

        self.listbox_category = Listbox(self.addData_frame, selectmode='single')
        self.listbox_category.grid(row=0, column=1, padx=5, pady=5)
        self.listbox_category.bind('<<ListboxSelect>>', self.update_add_fields)

        self.listbox_category.insert(1, 'Personnalité')
        self.listbox_category.insert(2, 'Entreprise')
        self.listbox_category.insert(3, 'Technologie')
        self.listbox_category.insert(4, 'Evénement')
        self.listbox_category.insert(5, 'Prix')

        # Variables pour les champs dynamiques
        self.dynamic_entries = []

        # Bouton de recherche
        self.add_button = Button(self.addData_frame, text='Ajouter', command=self.perform_add_element)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

        print("add Data View initiated !")

    def update_add_fields(self, event):
        # Supprime les champs de recherche existants
        self.clear_dynamic_entries()

        selected_index_category = self.listbox_category.curselection()

        if selected_index_category:
            category = self.listbox_category.get(selected_index_category)
            print("Recherche - Catégorie sélectionnée:", category)

            # Crée les champs de recherche spécifiques à la catégorie
            if category == 'Personnalité':
                self.create_personality_add_fields()
            elif category == 'Entreprise':
                self.create_company_add_fields()
            elif category == 'Technologie':
                self.create_technology_add_fields()
            elif category == 'Evénement':
                self.create_event_add_fields()
            elif category == 'Prix':
                self.create_price_add_fields()

    def clear_dynamic_entries(self):
        for entry in self.dynamic_entries:
            entry.destroy()
        self.dynamic_entries = []

    def create_personality_add_fields(self):
        label_lastname = Label(self.addData_frame, text='Nom:')
        label_lastname.grid(row=1, column=0, padx=5, pady=5)
        entry_lastname = Entry(self.addData_frame)
        entry_lastname.grid(row=1, column=1, padx=5, pady=5)

        self.dynamic_entries.append(label_lastname)
        self.dynamic_entries.append(entry_lastname)

        label_firstname = Label(self.addData_frame, text='Prénom:')
        label_firstname.grid(row=2, column=0, padx=5, pady=5)
        entry_firstname = Entry(self.addData_frame)
        entry_firstname.grid(row=2, column=1, padx=5, pady=5)

        self.dynamic_entries.append(label_firstname)
        self.dynamic_entries.append(entry_firstname)

        label_birthdate = Label(self.addData_frame, text='Année de naissance:')
        label_birthdate.grid(row=3, column=0, padx=5, pady=5)
        entry_birthdate = Entry(self.addData_frame)
        entry_birthdate.grid(row=3, column=1, padx=5, pady=5)
        
        self.dynamic_entries.append(label_birthdate)
        self.dynamic_entries.append(entry_birthdate)

        label_deathdate = Label(self.addData_frame, text='Année de décès:')
        label_deathdate.grid(row=4, column=0, padx=5, pady=5)
        entry_deathdate = Entry(self.addData_frame)
        entry_deathdate.grid(row=4, column=1, padx=5, pady=5)
        
        self.dynamic_entries.append(label_deathdate)
        self.dynamic_entries.append(entry_deathdate)

        label_description = Label(self.addData_frame, text='Description:')
        label_description.grid(row=5, column=0, padx=5, pady=5)
        entry_description = Text(self.addData_frame, height=5)
        entry_description.grid(row=5, column=1, padx=5, pady=5)

        self.dynamic_entries.append(label_description)
        self.dynamic_entries.append(entry_description)

        self.add_button.grid(row=6, column=0, columnspan=2, pady=10)

    def create_company_add_fields(self):
        label_company_name = Label(self.addData_frame, text='Nom:')
        label_company_name.grid(row=1, column=0, padx=5, pady=5)
        entry_company_name = Entry(self.addData_frame)
        entry_company_name.grid(row=1, column=1, padx=5, pady=5)

        self.dynamic_entries.append(label_company_name)
        self.dynamic_entries.append(entry_company_name)

        label_location = Label(self.addData_frame, text='Emplacement:')
        label_location.grid(row=2, column=0, padx=5, pady=5)
        entry_location = Entry(self.addData_frame)
        entry_location.grid(row=2, column=1, padx=5, pady=5)

        self.dynamic_entries.append(label_location)
        self.dynamic_entries.append(entry_location)

        label_creationdate = Label(self.addData_frame, text='Année de création:')
        label_creationdate.grid(row=3, column=0, padx=5, pady=5)
        entry_creationdate = Entry(self.addData_frame)
        entry_creationdate.grid(row=3, column=1, padx=5, pady=5)

        self.dynamic_entries.append(label_creationdate)
        self.dynamic_entries.append(entry_creationdate)

        label_description = Label(self.addData_frame, text='Description:')
        label_description.grid(row=4, column=0, padx=5, pady=5)
        entry_description = Text(self.addData_frame, height=5)
        entry_description.grid(row=4, column=1, padx=5, pady=5)

        self.dynamic_entries.append(label_description)
        self.dynamic_entries.append(entry_description)

        self.add_button.grid(row=5, column=0, columnspan=2, pady=10)

    def create_technology_add_fields(self):
        label_name = Label(self.addData_frame, text='Nom:')
        label_name.grid(row=1, column=0, padx=5, pady=5)
        entry_name = Entry(self.addData_frame)
        entry_name.grid(row=1, column=1, padx=5, pady=5)

        self.dynamic_entries.append(label_name)
        self.dynamic_entries.append(entry_name)

        label_type = Label(self.addData_frame, text='Type:')
        label_type.grid(row=2, column=0, padx=5, pady=5)
        entry_type = Entry(self.addData_frame)
        entry_type.grid(row=2, column=1, padx=5, pady=5)

        self.dynamic_entries.append(label_type)
        self.dynamic_entries.append(entry_type)

        label_year = Label(self.addData_frame, text='Année de développement:')
        label_year.grid(row=3, column=0, padx=5, pady=5)
        entry_year = Entry(self.addData_frame)
        entry_year.grid(row=3, column=1, padx=5, pady=5)

        self.dynamic_entries.append(label_year)
        self.dynamic_entries.append(entry_year)

        label_description = Label(self.addData_frame, text='Description:')
        label_description.grid(row=4, column=0, padx=5, pady=5)
        entry_description = Text(self.addData_frame, height=5)
        entry_description.grid(row=4, column=1, padx=5, pady=5)

        self.dynamic_entries.append(label_description)
        self.dynamic_entries.append(entry_description)

        self.add_button.grid(row=5, column=0, columnspan=2, pady=10)

    def create_event_add_fields(self):
        label_event_title = Label(self.addData_frame, text='Titre:')
        label_event_title.grid(row=1, column=0, padx=5, pady=5)
        entry_event_title = Entry(self.addData_frame)
        entry_event_title.grid(row=1, column=1, padx=5, pady=5)

        self.dynamic_entries.append(label_event_title)
        self.dynamic_entries.append(entry_event_title)

        label_date = Label(self.addData_frame, text='Date:')
        label_date.grid(row=2, column=0, padx=5, pady=5)
        entry_date = Entry(self.addData_frame)
        entry_date.grid(row=2, column=1, padx=5, pady=5)

        self.dynamic_entries.append(label_date)
        self.dynamic_entries.append(entry_date)

        label_location = Label(self.addData_frame, text='Lieu:')
        label_location.grid(row=3, column=0, padx=5, pady=5)
        entry_location = Entry(self.addData_frame)
        entry_location.grid(row=3, column=1, padx=5, pady=5)

        self.dynamic_entries.append(label_location)
        self.dynamic_entries.append(entry_location)

        label_description = Label(self.addData_frame, text='Description:')
        label_description.grid(row=4, column=0, padx=5, pady=5)
        entry_description = Text(self.addData_frame, height=5)
        entry_description.grid(row=4, column=1, padx=5, pady=5)

        self.dynamic_entries.append(label_description)
        self.dynamic_entries.append(entry_description)

        self.add_button.grid(row=5, column=0, columnspan=2, pady=10)

    def create_price_add_fields(self):
        label_price_name = Label(self.addData_frame, text='Nom:')
        label_price_name.grid(row=1, column=0, padx=5, pady=5)
        entry_price_name = Entry(self.addData_frame)
        entry_price_name.grid(row=1, column=1, padx=5, pady=5)

        self.dynamic_entries.append(label_price_name)
        self.dynamic_entries.append(entry_price_name)

        label_year = Label(self.addData_frame, text='Année de création:')
        label_year.grid(row=2, column=0, padx=5, pady=5)
        entry_year = Entry(self.addData_frame)
        entry_year.grid(row=2, column=1, padx=5, pady=5)

        self.dynamic_entries.append(label_year)
        self.dynamic_entries.append(entry_year)

        label_description = Label(self.addData_frame, text='Description:')
        label_description.grid(row=3, column=0, padx=5, pady=5)
        entry_description = Text(self.addData_frame, height=5)
        entry_description.grid(row=3, column=1, padx=5, pady=5)

        self.dynamic_entries.append(label_description)
        self.dynamic_entries.append(entry_description)

        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)

    def perform_add_element(self):
        selected_id_category = self.listbox_category.curselection()
        category = self.listbox_category.get(selected_id_category)
        print("Recherche - Catégorie sélectionné:", category)

        for widget in self.dynamic_entries:
            if isinstance(widget, Entry):
                value = widget.get()
                print(f"Valeur de l'Entry : {value}")
            if isinstance(widget, Text):
                value = widget.get("1.0", "end-1c")
                print(f"Valeur de Text : {value}")
        self.app.switch_to_dashboard_view()
