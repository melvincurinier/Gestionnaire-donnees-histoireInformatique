import customtkinter as ctk
from tkinter import ttk, Label, Button

class HomeView(ctk.CTkFrame):
    def __init__(self, parent, app):
        ctk.CTkFrame.__init__(self, parent)

        self.app = app

        # Frame pour le titre et les boutons
        title_frame = ctk.CTkFrame(self)
        title_frame.pack(side='top', fill='x')

        # Titre principal
        title_label = Label(title_frame, text='Tableau d\'informations')
        title_label.pack(padx=10)

        # Bouton Ajouter une donnée
        addDataView_button = Button(title_frame, text='Ajouter une donnée', command=self.addDataView_button_click)
        addDataView_button.pack(side='left')

        # Bouton Recherche avancée
        searchView_button = Button(title_frame, text='Recherche avancée', command=self.searchView_button_click)
        searchView_button.pack(side='left', padx=5)

        # Bouton Exporter une donnée
        exportDataView_button = Button(title_frame, text='Exporter', command=self.exportDataView_button_click)
        exportDataView_button.pack(side='left')

        # Bouton Importer une donnée
        importDataView_button = Button(title_frame, text='Importer', command=self.importDataView_button_click)
        importDataView_button.pack(side='left', padx=5)

        # Tableau
        columns = ('type', 'name', 'brief_description')
        self.tree = ttk.Treeview(self, columns=columns, show='headings')

        # Définir les colonnes
        self.tree.heading('type', text='Type')
        self.tree.heading('name', text='Nom')
        self.tree.heading('brief_description', text='Description briève')

        self.tree.bind('<ButtonRelease-1>', self.on_tree_click)

        # Pack the Treeview widget
        self.tree.pack(side='left', expand=True, fill='both')

        # Frame à droite du tableau pour afficher les informations de l'item
        self.info_frame = ctk.CTkFrame(self)
        self.info_frame.pack(side='left', padx=10)

        data = [
            ('Personnalité', 'Tillian Dhume', 'Respo réseau Polytech'),
            ('Personnalité', 'Will Smith', 'Acteur américain'),
            # Ajoutez autant de lignes que nécessaire
        ]
        for item_data in data:
            self.add_item(item_data)

    def add_item(self, data):
        # Ajoute une ligne avec les données spécifiées
        self.tree.insert('', 'end', values=data)

    def on_tree_click(self, event):
        item = self.tree.selection()

        if item:
            values = self.tree.item(item, 'values')
            self.show_item_info(values)
    
    def show_item_info(self, item_data):
        # Efface les anciennes étiquettes
        for widget in self.info_frame.winfo_children():
            widget.destroy()

        # Ajoute des étiquettes avec les informations de l'item
        Label(self.info_frame, text='Type:').grid(row=0, column=0, sticky='e')
        Label(self.info_frame, text=item_data[0]).grid(row=0, column=1)

        Label(self.info_frame, text='Nom:').grid(row=1, column=0, sticky='e')
        Label(self.info_frame, text=item_data[1]).grid(row=1, column=1)

        Label(self.info_frame, text='Description briève:').grid(row=2, column=0, sticky='e')
        Label(self.info_frame, text=item_data[2]).grid(row=2, column=1)
    
    def addDataView_button_click(self):
        print("Bouton ajouter une donnée cliqué!")
    
    def searchView_button_click(self):
        print("Bouton recherche avancée cliqué!")
    
    def exportDataView_button_click(self):
        print("Bouton exporter cliqué!")
    
    def importDataView_button_click(self):
        print("Bouton importer cliqué!")