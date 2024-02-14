import customtkinter as ctk
from tkinter import ttk, Label, Button
from models.supprimer import *


class DashboardView(ctk.CTkFrame):
    def __init__(self, parent, app, category, data):
        ctk.CTkFrame.__init__(self, parent)

        self.app = app
        self.category = category

        title_frame = ctk.CTkFrame(self)
        title_frame.pack(side='top', fill='x')

        return_button = Button(title_frame, text='Retour', command=app.switch_to_searchData_view)
        return_button.grid(row=0, column=0, sticky='w')

        title_label = Label(title_frame, text='Tableau d\'informations')
        title_label.grid(row=0, column=1, padx=10)

        if self.category == "Personnalité":
            columns = ('id', 'name', 'birthdate', 'deathdate', 'description')
            self.tree = ttk.Treeview(self, columns=columns, show='headings')

            self.tree.heading('id', text='Identifiant')
            self.tree.heading('name', text='Nom')
            self.tree.heading('birthdate', text='Année de naissance')
            self.tree.heading('deathdate', text='Année de décès')
            self.tree.heading('description', text='Description')

            self.tree.column('id',width=100)
            self.tree.column('name',width=100)
            self.tree.column('birthdate',width=100)
            self.tree.column('deathdate',width=100)
            self.tree.column('description',width=200)
        elif self.category == "Technologie":
            columns = ('id', 'title', 'creationdate', 'type', 'description')
            self.tree = ttk.Treeview(self, columns=columns, show='headings')

            self.tree.heading('id', text='Identifiant')
            self.tree.heading('title', text='Titre')
            self.tree.heading('creationdate', text='Année de création')
            self.tree.heading('type', text='Type')
            self.tree.heading('description', text='Description')

            self.tree.column('id',width=100)
            self.tree.column('title',width=200)
            self.tree.column('creationdate',width=100)
            self.tree.column('type',width=200)
            self.tree.column('description',width=200)
        elif self.category == "Evénement":
            columns = ('id', 'title', 'date', 'location', 'description')
            self.tree = ttk.Treeview(self, columns=columns, show='headings')

            self.tree.heading('id', text='Identifiant')
            self.tree.heading('title', text='Titre')
            self.tree.heading('date', text='Année')
            self.tree.heading('location', text='Lieu')
            self.tree.heading('description', text='Description')

            self.tree.column('id',width=100)
            self.tree.column('title',width=200)
            self.tree.column('date',width=100)
            self.tree.column('location',width=100)
            self.tree.column('description',width=200)
        else:
            columns = ('id', 'nom', 'date', 'description')
            self.tree = ttk.Treeview(self, columns=columns, show='headings')

        self.tree.bind('<ButtonRelease-1>', self.on_tree_click)

        self.tree.pack(side='left', expand=False, fill='both')

        self.info_frame = ctk.CTkFrame(self)
        self.info_frame.pack(side='left', padx=10)
      
        if data:
            for item_data in data:
                self.add_item(item_data)

    def add_item(self, data):
        self.tree.insert('', 'end', values=data)

    def on_tree_click(self, event):
        item = self.tree.selection()
        self.show_item_info(item)
    
    def show_item_info(self, item):
        if item:
            values = self.tree.item(item, 'values')

        for widget in self.info_frame.winfo_children():
            widget.destroy()

        if self.category == "Personnalité":
            Label(self.info_frame, text='Nom:').grid(row=0, column=0, sticky='e')
            Label(self.info_frame, text=values[1]).grid(row=0, column=1)

            Label(self.info_frame, text='Année de naissance:').grid(row=1, column=0, sticky='e')
            Label(self.info_frame, text=values[2]).grid(row=1, column=1)

            Label(self.info_frame, text='Année de décès:').grid(row=2, column=0, sticky='e')
            Label(self.info_frame, text=values[3]).grid(row=2, column=1)

            Label(self.info_frame, text='Description:').grid(row=3, column=0, sticky='e')
            Label(self.info_frame, text=values[4],  wraplength=250).grid(row=3, column=1)
        elif self.category == "Technologie":
            Label(self.info_frame, text='Title:').grid(row=0, column=0, sticky='e')
            Label(self.info_frame, text=values[1]).grid(row=0, column=1)

            Label(self.info_frame, text='Type:').grid(row=1, column=0, sticky='e')
            Label(self.info_frame, text=values[4]).grid(row=1, column=1)

            Label(self.info_frame, text='Année de création:').grid(row=2, column=0, sticky='e')
            Label(self.info_frame, text=values[2]).grid(row=2, column=1)

            Label(self.info_frame, text='Description:').grid(row=3, column=0, sticky='e')
            Label(self.info_frame, text=values[3], wraplength=250).grid(row=3, column=1)
        elif self.category == "Evénement":
            Label(self.info_frame, text='Title:').grid(row=0, column=0, sticky='e')
            Label(self.info_frame, text=values[1]).grid(row=0, column=1)

            Label(self.info_frame, text='Année:').grid(row=1, column=0, sticky='e')
            Label(self.info_frame, text=values[2]).grid(row=1, column=1)

            Label(self.info_frame, text='Lieu:').grid(row=2, column=0, sticky='e')
            Label(self.info_frame, text=values[3]).grid(row=2, column=1)

            Label(self.info_frame, text='Description:').grid(row=3, column=0, sticky='e')
            Label(self.info_frame, text=values[4], wraplength=250).grid(row=3, column=1)

        Button(self.info_frame, text='Modifier', command=self.updateDataView_button_click).grid(row=4, column=1)
        Button(self.info_frame, text='Supprimer', command=lambda: self.deleteData_button_click(values[0], item)).grid(row=5, column=1)
    
    def addDataView_button_click(self):
        self.app.switch_to_addData_view()

    def updateDataView_button_click(self):
        self.app.switch_to_updateData_view()
    
    def searchDataView_button_click(self):
        self.app.switch_to_searchData_view()
    
    def deleteData_button_click(self, id, item):
        if self.category == "Personnalité":
            supprimer_une_personnalite(id)
        elif self.category == "Technologie":
            supprimer_une_technologie(id)
        elif self.category == "Evénement":
            supprimer_un_evenement(id)
        self.tree.delete(item)
        for widget in self.info_frame.winfo_children():
            widget.destroy()
    
    def exportDataView_button_click(self):
        self.app.show_importData_view()
    
    def importDataView_button_click(self):
        self.app.show_exportData_view()