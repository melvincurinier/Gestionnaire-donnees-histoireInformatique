import customtkinter as ctk
from tkinter import Label, Button, Entry, Listbox

from models.rechercher import *
from models.afficher import *

class SearchDataView(ctk.CTkFrame):
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
        title_label = Label(title_frame, text='Recherche une donnée')
        title_label.grid(row=0, column=1, padx=10)

        # Frame pour les champs de recherche
        self.research_frame = ctk.CTkFrame(self)
        self.research_frame.pack(fill='x', padx=10, pady=10)

        # Catégorie
        label_category = Label(self.research_frame, text='Catégorie:')
        label_category.grid(row=0, column=0, padx=5, pady=5)

        self.listbox_category = Listbox(self.research_frame, selectmode='single')
        self.listbox_category.grid(row=0, column=1, padx=5, pady=5)
        self.listbox_category.bind('<<ListboxSelect>>', self.update_search_fields)

        self.listbox_category.insert(1, 'Personnalité')
        self.listbox_category.insert(2, 'Entreprise')
        self.listbox_category.insert(3, 'Technologie')
        self.listbox_category.insert(4, 'Evénement')
        self.listbox_category.insert(5, 'Prix')

        # Variables pour les champs dynamiques
        self.dynamic_entries = []

        # Bouton de recherche
        self.search_button = Button(self.research_frame, text='Rechercher', command=self.perform_search)
        self.search_button.grid(row=3, column=0, columnspan=2, pady=10)

        print("Search Data View initiated !")

    def update_search_fields(self, event):
        self.clear_dynamic_entries()

        selected_index_category = self.listbox_category.curselection()

        if selected_index_category:
            category = self.listbox_category.get(selected_index_category)
            if category == 'Personnalité':
                self.create_personality_search_fields()
            elif category == 'Entreprise':
                self.create_company_search_fields()
            elif category == 'Technologie':
                self.create_technology_search_fields()
            elif category == 'Evénement':
                self.create_event_search_fields()
            elif category == 'Prix':
                self.create_price_search_fields()

    def clear_dynamic_entries(self):
        for entry in self.dynamic_entries:
            entry.destroy()
        self.dynamic_entries = []

    def create_personality_search_fields(self):
        label_lastname = Label(self.research_frame, text='Nom:')
        label_lastname.grid(row=1, column=0, padx=5, pady=5)
        entry_lastname = Entry(self.research_frame)
        entry_lastname.grid(row=1, column=1, padx=5, pady=5)

        self.dynamic_entries.append(label_lastname)
        self.dynamic_entries.append(entry_lastname)

        label_birthdate = Label(self.research_frame, text='Année de naissance:')
        label_birthdate.grid(row=2, column=0, padx=5, pady=5)
        entry_birthdate = Entry(self.research_frame)
        entry_birthdate.grid(row=2, column=1, padx=5, pady=5)
        
        self.dynamic_entries.append(label_birthdate)
        self.dynamic_entries.append(entry_birthdate)

        label_deathdate = Label(self.research_frame, text='Année de décès:')
        label_deathdate.grid(row=3, column=0, padx=5, pady=5)
        entry_deathdate = Entry(self.research_frame)
        entry_deathdate.grid(row=3, column=1, padx=5, pady=5)
        
        self.dynamic_entries.append(label_deathdate)
        self.dynamic_entries.append(entry_deathdate)

        label_keyword = Label(self.research_frame, text='Mot-clé:')
        label_keyword.grid(row=4, column=0, padx=5, pady=5)
        entry_keyword = Entry(self.research_frame)
        entry_keyword.grid(row=4, column=1, padx=5, pady=5)

        self.dynamic_entries.append(label_keyword)
        self.dynamic_entries.append(entry_keyword)

        self.search_button.grid(row=5, column=0, columnspan=2, pady=10)

    def create_company_search_fields(self):
        label_company_name = Label(self.research_frame, text='Nom:')
        label_company_name.grid(row=1, column=0, padx=5, pady=5)
        entry_company_name = Entry(self.research_frame)
        entry_company_name.grid(row=1, column=1, padx=5, pady=5)

        self.dynamic_entries.append(label_company_name)
        self.dynamic_entries.append(entry_company_name)

        label_location = Label(self.research_frame, text='Emplacement:')
        label_location.grid(row=2, column=0, padx=5, pady=5)
        entry_location = Entry(self.research_frame)
        entry_location.grid(row=2, column=1, padx=5, pady=5)

        self.dynamic_entries.append(label_location)
        self.dynamic_entries.append(entry_location)

        label_creationdate = Label(self.research_frame, text='Année de création:')
        label_creationdate.grid(row=3, column=0, padx=5, pady=5)
        entry_creationdate = Entry(self.research_frame)
        entry_creationdate.grid(row=3, column=1, padx=5, pady=5)

        self.dynamic_entries.append(label_creationdate)
        self.dynamic_entries.append(entry_creationdate)

        label_keyword = Label(self.research_frame, text='Mot-clé:')
        label_keyword.grid(row=4, column=0, padx=5, pady=5)
        entry_keyword = Entry(self.research_frame)
        entry_keyword.grid(row=4, column=1, padx=5, pady=5)

        self.dynamic_entries.append(label_keyword)
        self.dynamic_entries.append(entry_keyword)

        self.search_button.grid(row=5, column=0, columnspan=2, pady=10)

    def create_technology_search_fields(self):
        label_name = Label(self.research_frame, text='Nom:')
        label_name.grid(row=1, column=0, padx=5, pady=5)
        entry_name = Entry(self.research_frame)
        entry_name.grid(row=1, column=1, padx=5, pady=5)

        self.dynamic_entries.append(label_name)
        self.dynamic_entries.append(entry_name)

        label_type = Label(self.research_frame, text='Type:')
        label_type.grid(row=2, column=0, padx=5, pady=5)
        entry_type = Entry(self.research_frame)
        entry_type.grid(row=2, column=1, padx=5, pady=5)

        self.dynamic_entries.append(label_type)
        self.dynamic_entries.append(entry_type)

        label_year = Label(self.research_frame, text='Année de développement:')
        label_year.grid(row=3, column=0, padx=5, pady=5)
        entry_year = Entry(self.research_frame)
        entry_year.grid(row=3, column=1, padx=5, pady=5)

        self.dynamic_entries.append(label_year)
        self.dynamic_entries.append(entry_year)

        label_keyword = Label(self.research_frame, text='Mot-clé:')
        label_keyword.grid(row=4, column=0, padx=5, pady=5)
        entry_keyword = Entry(self.research_frame)
        entry_keyword.grid(row=4, column=1, padx=5, pady=5)

        self.dynamic_entries.append(label_keyword)
        self.dynamic_entries.append(entry_keyword)

        self.search_button.grid(row=5, column=0, columnspan=2, pady=10)

    def create_event_search_fields(self):
        label_event_title = Label(self.research_frame, text='Titre:')
        label_event_title.grid(row=1, column=0, padx=5, pady=5)
        entry_event_title = Entry(self.research_frame)
        entry_event_title.grid(row=1, column=1, padx=5, pady=5)

        self.dynamic_entries.append(label_event_title)
        self.dynamic_entries.append(entry_event_title)

        label_date = Label(self.research_frame, text='Date:')
        label_date.grid(row=2, column=0, padx=5, pady=5)
        entry_date = Entry(self.research_frame)
        entry_date.grid(row=2, column=1, padx=5, pady=5)

        self.dynamic_entries.append(label_date)
        self.dynamic_entries.append(entry_date)

        label_location = Label(self.research_frame, text='Lieu:')
        label_location.grid(row=3, column=0, padx=5, pady=5)
        entry_location = Entry(self.research_frame)
        entry_location.grid(row=3, column=1, padx=5, pady=5)

        self.dynamic_entries.append(label_location)
        self.dynamic_entries.append(entry_location)

        label_keyword = Label(self.research_frame, text='Mot-clé:')
        label_keyword.grid(row=4, column=0, padx=5, pady=5)
        entry_keyword = Entry(self.research_frame)
        entry_keyword.grid(row=4, column=1, padx=5, pady=5)

        self.dynamic_entries.append(label_keyword)
        self.dynamic_entries.append(entry_keyword)

        self.search_button.grid(row=5, column=0, columnspan=2, pady=10)

    def create_price_search_fields(self):
        label_price_name = Label(self.research_frame, text='Nom:')
        label_price_name.grid(row=1, column=0, padx=5, pady=5)
        entry_price_name = Entry(self.research_frame)
        entry_price_name.grid(row=1, column=1, padx=5, pady=5)

        self.dynamic_entries.append(label_price_name)
        self.dynamic_entries.append(entry_price_name)

        label_year = Label(self.research_frame, text='Année de création:')
        label_year.grid(row=2, column=0, padx=5, pady=5)
        entry_year = Entry(self.research_frame)
        entry_year.grid(row=2, column=1, padx=5, pady=5)

        self.dynamic_entries.append(label_year)
        self.dynamic_entries.append(entry_year)

        label_keyword = Label(self.research_frame, text='Mot-clé:')
        label_keyword.grid(row=3, column=0, padx=5, pady=5)
        entry_keyword = Entry(self.research_frame)
        entry_keyword.grid(row=3, column=1, padx=5, pady=5)

        self.dynamic_entries.append(label_keyword)
        self.dynamic_entries.append(entry_keyword)

        self.search_button.grid(row=4, column=0, columnspan=2, pady=10)

    def perform_search(self):
        selected_id_category = self.listbox_category.curselection()
        category = self.listbox_category.get(selected_id_category)

        searchdata = []
        for widget in self.dynamic_entries:
            if isinstance(widget, Entry):
                value = widget.get()
                searchdata.append(value)

        if(category == "Personnalité"):
            if(searchdata[0] != ''):
                data = rechercher_une_personnalite(searchdata[0])
            else:
                data = afficher_les_personnalites()
        elif(category == "Technologie"):
            if(searchdata[0] != ''):
                data = rechercher_une_technologie(searchdata[0])
            else:
                data = afficher_les_technologies()
        elif(category == "Evénement"):
            if(searchdata[0] != ''):
                data = rechercher_un_evenement(searchdata[0])
            else:
                data = afficher_les_evenements()
        
        self.app.switch_to_dashboard_view(category, data)
