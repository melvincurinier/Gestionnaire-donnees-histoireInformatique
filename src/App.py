from tkinter import *
import customtkinter

from Controller import *
from Model import *
from View import *

class App(Tk):
    def __init__(self):
        super().__init__()

        model = Model()
        view = View(self)
        controller = Controller(model, view)

        print("App initiated !")

if __name__ == "__main__":
    App().mainloop()