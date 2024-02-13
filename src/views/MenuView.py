import customtkinter as ctk
from tkinter import Label, Button

class MenuView(ctk.CTkFrame):
    def __init__(self, parent, app):
        ctk.CTkFrame.__init__(self, parent)

        self.app = app

        # Frame pour le titre et les boutons
        title_frame = ctk.CTkFrame(self)
        title_frame.pack(side='top', fill='x')

        # Titre principal
        title_label = Label(title_frame, text='Menu principal')
        title_label.pack(padx=10)

        # Bouton Ajouter une donnée
        addDataView_button = Button(title_frame, text='Ajouter une donnée', command=self.addDataView_button_click)
        addDataView_button.pack()

        # Bouton Recherche avancée
        searchView_button = Button(title_frame, text='Recherche avancée', command=self.searchDataView_button_click)
        searchView_button.pack()

        # Bouton Importer une donnée
        importDataView_button = Button(title_frame, text='Importer', command=self.importDataView_button_click)
        importDataView_button.pack()

        # Définir les colonnes
    
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