import customtkinter as ctk

from views.AddDataView import AddDataView
from views.SearchDataView import SearchDataView
from views.UpdateDataView import UpdateDataView
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
    
    def show_addData_view(self):
        addData_view = AddDataView(self.container, self)
        addData_view.pack()
    
    def show_updateData_view(self):
        updateData_view = UpdateDataView(self.container, self)
        updateData_view.pack()
    
    def show_searchData_view(self):
        searchData_view = SearchDataView(self.container, self)
        searchData_view.pack()
    
    def show_deleteData_view(self):
        print('Delete Data !')
    
    def show_importData_view(self):
        print('Import Data !')
    
    def show_exportData_view(self):
        print('Export Data !')

    def switch_to_home_view(self):
        self.clear_container()
        self.show_home_view()

    def switch_to_addData_view(self):
        self.clear_container()
        self.show_addData_view()
    
    def switch_to_updateData_view(self):
        self.clear_container()
        self.show_updateData_view()
    
    def switch_to_searchData_view(self):
        self.clear_container()
        self.show_searchData_view()

    def clear_container(self):
        self.container.pack_forget()
        self.container = ctk.CTkFrame(self.root_tk)
        self.container.pack(fill='both', expand=True)

    def run(self):
        self.root_tk.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()