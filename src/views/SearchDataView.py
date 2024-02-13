import customtkinter as ctk
from tkinter import Label, Button, Entry, Listbox

class SearchDataView(ctk.CTkFrame):
    def __init__(self, parent, app):
        ctk.CTkFrame.__init__(self, parent)

        self.app = app

        # Frame pour le titre
        title_frame = ctk.CTkFrame(self)
        title_frame.pack(side='top', fill='x')

        # Titre principal
        title_label = Label(title_frame, text='Recherche une donnée')
        title_label.pack(padx=10)

        # Frame pour les champs de recherche
        self.research_frame = ctk.CTkFrame(self)
        self.research_frame.pack(fill='x', padx=10, pady=10)

        # Catégorie
        label_category = Label(self.research_frame, text='Catégorie:')
        label_category.grid(row=0, column=0, padx=5, pady=5)

        self.listbox_category = Listbox(self.research_frame, selectmode='single')
        self.listbox_category.grid(row=0, column=1, padx=5, pady=5)
        self.listbox_category.bind('<<ListboxSelect>>', self.update_search_fields)

        # Ajout d'éléments à la liste (exemple)
        self.listbox_category.insert(1, 'Personnalité')
        self.listbox_category.insert(2, 'Entreprise')
        self.listbox_category.insert(3, 'Technologie')
        self.listbox_category.insert(4, 'Evénement')
        self.listbox_category.insert(5, 'Prix')

        # Variables pour les champs dynamiques
        self.dynamic_entries = []

        # Bouton de recherche
        search_button = Button(self.research_frame, text='Rechercher', command=self.perform_search)
        search_button.grid(row=3, column=0, columnspan=2, pady=10)

        print("Search Data View initiated !")

    def update_search_fields(self, event):
        # Supprime les champs de recherche existants
        self.clear_dynamic_entries()

        selected_index_category = self.listbox_category.curselection()

        if selected_index_category:
            category = self.listbox_category.get(selected_index_category)
            print("Recherche - Catégorie sélectionnée:", category)

            # Crée les champs de recherche spécifiques à la catégorie
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
        # Efface les champs de recherche précédents
        for entry in self.dynamic_entries:
            entry.destroy()
        self.dynamic_entries = []

    def create_personality_search_fields(self):
        # Crée les champs de recherche spécifiques à la catégorie 'Personnalité'
        label_name = Label(self.research_frame, text='Nom:')
        label_name.grid(row=1, column=0, padx=5, pady=5)

        entry_name = Entry(self.research_frame)
        entry_name.grid(row=1, column=1, padx=5, pady=5)
        self.dynamic_entries.append(label_name)
        self.dynamic_entries.append(entry_name)

    def create_company_search_fields(self):
        # Crée les champs de recherche spécifiques à la catégorie 'Entreprise'
        label_company_name = Label(self.research_frame, text='Nom de l\'entreprise:')
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

    def create_technology_search_fields(self):
        # Crée les champs de recherche spécifiques à la catégorie 'Technologie'
        label_technology_name = Label(self.research_frame, text='Nom de la technologie:')
        label_technology_name.grid(row=1, column=0, padx=5, pady=5)

        entry_technology_name = Entry(self.research_frame)
        entry_technology_name.grid(row=1, column=1, padx=5, pady=5)
        self.dynamic_entries.append(label_technology_name)
        self.dynamic_entries.append(entry_technology_name)

        label_year = Label(self.research_frame, text='Année de développement:')
        label_year.grid(row=2, column=0, padx=5, pady=5)

        entry_year = Entry(self.research_frame)
        entry_year.grid(row=2, column=1, padx=5, pady=5)
        self.dynamic_entries.append(label_year)
        self.dynamic_entries.append(entry_year)

    def create_event_search_fields(self):
        # Crée les champs de recherche spécifiques à la catégorie 'Evénement'
        label_event_name = Label(self.research_frame, text='Nom de l\'événement:')
        label_event_name.grid(row=1, column=0, padx=5, pady=5)

        entry_event_name = Entry(self.research_frame)
        entry_event_name.grid(row=1, column=1, padx=5, pady=5)
        self.dynamic_entries.append(label_event_name)
        self.dynamic_entries.append(entry_event_name)

        label_date = Label(self.research_frame, text='Date de l\'événement:')
        label_date.grid(row=2, column=0, padx=5, pady=5)

        entry_date = Entry(self.research_frame)
        entry_date.grid(row=2, column=1, padx=5, pady=5)
        self.dynamic_entries.append(label_date)
        self.dynamic_entries.append(entry_date)

    def create_price_search_fields(self):
        # Crée les champs de recherche spécifiques à la catégorie 'Prix'
        label_price_name = Label(self.research_frame, text='Nom du prix:')
        label_price_name.grid(row=1, column=0, padx=5, pady=5)

        entry_price_name = Entry(self.research_frame)
        entry_price_name.grid(row=1, column=1, padx=5, pady=5)
        self.dynamic_entries.append(label_price_name)
        self.dynamic_entries.append(entry_price_name)

        label_year = Label(self.research_frame, text='Année du prix:')
        label_year.grid(row=2, column=0, padx=5, pady=5)

        entry_year = Entry(self.research_frame)
        entry_year.grid(row=2, column=1, padx=5, pady=5)
        self.dynamic_entries.append(label_year)
        self.dynamic_entries.append(entry_year)

    def perform_search(self):
        selected_id_category = self.listbox_category.curselection()
        category = self.listbox_category.get(selected_id_category)
        print("Recherche - Catégorie sélectionné:", category)
