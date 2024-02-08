import customtkinter as ctk

from views.HomeView import HomeView

class App:
    def __init__(self):
        self.root_tk = ctk.CTk()
        self.root_tk.geometry('1000x500')
        self.root_tk.resizable(False, False)
        self.root_tk.title("Gestionnaire de données sur l'histoire informatique")

        self.container = ctk.CTkFrame(self.root_tk)
        self.container.pack(fill='both', expand=True)

        self.show_home_view()

        print("App initiated !")

    def show_home_view(self):
        home_view = HomeView(self.container, self)
        home_view.pack()

    def run(self):
        self.root_tk.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()