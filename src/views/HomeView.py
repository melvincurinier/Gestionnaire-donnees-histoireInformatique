import customtkinter as ctk
from tkinter import ttk

class HomeView(ctk.CTkFrame):
    def __init__(self, parent, app):
        ctk.CTkFrame.__init__(self, parent)

        self.app = app

        columns = ('first_name', 'last_name', 'email')

        # Use self instead of parent for Treeview
        self.tree = ttk.Treeview(self, columns=columns, show='headings')

        # define headings
        self.tree.heading('first_name', text='First Name')
        self.tree.heading('last_name', text='Last Name')
        self.tree.heading('email', text='Email')

        # Pack the Treeview widget
        self.tree.pack(expand=True, fill='both')
