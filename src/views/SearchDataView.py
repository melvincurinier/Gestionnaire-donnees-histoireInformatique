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
        research_frame = ctk.CTkFrame(self)
        research_frame.pack(fill='x', padx=10, pady=10)

        label_category = Label(research_frame, text='Catégorie:')
        label_category.grid(row=0, column=0, padx=5, pady=5)
        self.listbox_category = Listbox(research_frame, selectmode='single')
        self.listbox_category.grid(row=0, column=1, padx=5, pady=5)

        # Ajout d'éléments à la liste (exemple)
        self.listbox_category.insert(1, 'Personnalité')
        self.listbox_category.insert(2, 'Entreprise')
        self.listbox_category.insert(2, 'Technologie')
        self.listbox_category.insert(3, 'Evénement')
        self.listbox_category.insert(4, 'Prix')

        # Bouton de recherche
        search_button = Button(research_frame, text='Rechercher', command=self.perform_search)
        search_button.grid(row=3, column=0, columnspan=2, pady=10)

        print("Search Data View initiated !")

    def perform_search(self):
        selected_id_category = self.listbox_category.curselection()
        category = self.listbox_category.get(selected_id_category)
        print("Recherche - Catégorie sélectionné:", category)
