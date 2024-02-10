import customtkinter as ctk

from tkinter import Label, Button

class UpdateDataView(ctk.CTkFrame):
    def __init__(self, parent, app):
        ctk.CTkFrame.__init__(self, parent)

        self.app = app

        # Frame pour le titre et les boutons
        title_frame = ctk.CTkFrame(self)
        title_frame.pack(side='top', fill='x')

        # Titre principal
        title_label = Label(title_frame, text='Modifier cette donnée')
        title_label.pack(padx=10)
        
        print("Updated Data View initiated !")