import customtkinter as ctk
from tkinter import ttk, Label, Button

class DashboardView(ctk.CTkFrame):
    def __init__(self, parent, app):
        ctk.CTkFrame.__init__(self, parent)

        self.app = app

        # Frame pour le titre et les boutons
        title_frame = ctk.CTkFrame(self)
        title_frame.pack(side='top', fill='x')

        # Bouton "Retour"
        return_button = Button(title_frame, text='Retour', command=app.switch_to_searchData_view)
        return_button.grid(row=0, column=0, sticky='w')

        # Titre principal
        title_label = Label(title_frame, text='Tableau d\'informations')
        title_label.grid(row=0, column=1, padx=10)

        # Tableau
        columns = ('id', 'name', 'brief_description')
        self.tree = ttk.Treeview(self, columns=columns, show='headings')

        # Définir les colonnes
        self.tree.heading('id', text='Identifiant')
        self.tree.heading('name', text='Nom')
        self.tree.heading('brief_description', text='Description briève')

        self.tree.column('id',width=100)

        self.tree.bind('<ButtonRelease-1>', self.on_tree_click)

        # Pack the Treeview widget
        self.tree.pack(side='left', expand=True, fill='both')

        # Frame à droite du tableau pour afficher les informations de l'item
        self.info_frame = ctk.CTkFrame(self)
        self.info_frame.pack(side='left', padx=10)

        data = [
            ('1', 'Tillian Dhume', 'Respo réseau Polytech'),
            ('2', 'Will Smith', 'Acteur américain'),
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
        Label(self.info_frame, text=item_data[1]).grid(row=0, column=1)

        Label(self.info_frame, text='Nom:').grid(row=1, column=0, sticky='e')
        Label(self.info_frame, text=item_data[2]).grid(row=1, column=1)

        Button(self.info_frame, text='Modifier', command=self.updateDataView_button_click).grid(row=3, column=0)
        Button(self.info_frame, text='Supprimer', command=self.deleteData_button_click).grid(row=3, column=1)
    
    def addDataView_button_click(self):
        self.app.switch_to_addData_view()

    def updateDataView_button_click(self):
        self.app.switch_to_updateData_view()
    
    def searchDataView_button_click(self):
        self.app.switch_to_searchData_view()
    
    def deleteData_button_click(self):
        self.app.show_deleteData_view()
    
    def exportDataView_button_click(self):
        self.app.show_importData_view()
    
    def importDataView_button_click(self):
        self.app.show_exportData_view()