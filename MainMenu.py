import tkinter as tk
from tkinter import messagebox
import database
from AddBookScreen import AddBookScreen

class MainMenu(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("pyBookshelf")

        self.label_menu_title = tk.Label(self, text="Menu Principal")
        self.label_menu_title.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.btn_add_book = tk.Button(self, text="Add Book", command=self.show_add_book)
        self.btn_add_book.grid(row=1, column=0, padx=5, pady=5)

        self.btn_view_books = tk.Button(self, text="View Books", command=self.view_books)
        self.btn_view_books.grid(row=1, column=1, padx=5, pady=5)

        self.btn_exit = tk.Button(self, text="Exit", command=self.exit_app)
        self.btn_exit.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.grid()

    def show_add_book(self):
        self.destroy()  # Destrua a tela atual
        AddBookScreen(self.master)  # Cria a tela para adicionar um novo livro

    def view_books(self):
        # Código para visualizar todos os livros
        pass

    def exit_app(self):
        self.master.destroy()
