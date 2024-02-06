from tkinter import *

class View(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = None
        print("View initiated !")

    def set_controller(self, controller):
        self.controller = controller