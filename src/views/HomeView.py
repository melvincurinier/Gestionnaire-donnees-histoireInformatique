import customtkinter as ctk
from tkinter import ttk

class HomeView(ctk.CTkFrame):
    def __init__(self, parent, app):
        ctk.CTkFrame.__init__(self, parent)

        self.app = app

        columns = ('type', 'name', 'brief_description')

        self.tree = ttk.Treeview(self, columns=columns, show='headings')

        # define headings
        self.tree.heading('type', text='Type')
        self.tree.heading('name', text='Nom')
        self.tree.heading('brief_description', text='Description briève')

        self.tree.bind('<ButtonRelease-1>', self.on_tree_click)

        # Pack the Treeview widget
        self.tree.pack(expand=True, fill='both')

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
            print("Row clicked:", values)