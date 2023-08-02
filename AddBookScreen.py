import tkinter as tk
from tkinter import messagebox
import database
from MainMenu import MainMenu

class AddBookScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        # Cria os campos de entrada para adicionar um novo livro
        self.label_title = tk.Label(self, text="Title*:")
        self.label_title.grid(row=1, column=0, padx=5, pady=5)
        self.entry_title = tk.Entry(self)
        self.entry_title.grid(row=1, column=1, padx=5, pady=5)

        self.label_author = tk.Label(self, text="Author*:")
        self.label_author.grid(row=2, column=0, padx=5, pady=5)
        self.entry_author = tk.Entry(self)
        self.entry_author.grid(row=2, column=1, padx=5, pady=5)

        self.label_year = tk.Label(self, text="Year:")
        self.label_year.grid(row=3, column=0, padx=5, pady=5)
        self.entry_year = tk.Entry(self)
        self.entry_year.grid(row=3, column=1, padx=5, pady=5)

        self.label_isbn = tk.Label(self, text="ISBN:")
        self.label_isbn.grid(row=4, column=0, padx=5, pady=5)
        self.entry_isbn = tk.Entry(self)
        self.entry_isbn.grid(row=4, column=1, padx=5, pady=5)

        self.label_pages = tk.Label(self, text="Pages:")
        self.label_pages.grid(row=5, column=0, padx=5, pady=5)
        self.entry_pages = tk.Entry(self)
        self.entry_pages.grid(row=5, column=1, padx=5, pady=5)

        self.label_edition = tk.Label(self, text="Edition:")
        self.label_edition.grid(row=6, column=0, padx=5, pady=5)
        self.entry_edition = tk.Entry(self)
        self.entry_edition.grid(row=6, column=1, padx=5, pady=5)

        self.label_publisher = tk.Label(self, text="Publisher:")
        self.label_publisher.grid(row=7, column=0, padx=5, pady=5)
        self.entry_publisher = tk.Entry(self)
        self.entry_publisher.grid(row=7, column=1, padx=5, pady=5)

        self.label_language = tk.Label(self, text="Language:")
        self.label_language.grid(row=8, column=0, padx=5, pady=5)
        self.entry_language = tk.Entry(self)
        self.entry_language.grid(row=8, column=1, padx=5, pady=5)

        self.label_genre = tk.Label(self, text="Genre:")
        self.label_genre.grid(row=9, column=0, padx=5, pady=5)
        self.entry_genre = tk.Entry(self)
        self.entry_genre.grid(row=9, column=1, padx=5, pady=5)

        self.label_description = tk.Label(self, text="Description:")
        self.label_description.grid(row=10, column=0, padx=5, pady=5)
        self.entry_description = tk.Entry(self)
        self.entry_description.grid(row=10, column=1, padx=5, pady=5)

        self.label_image = tk.Label(self, text="Image:")
        self.label_image.grid(row=11, column=0, padx=5, pady=5)
        self.entry_image = tk.Entry(self)
        self.entry_image.grid(row=11, column=1, padx=5, pady=5)

        # Botão para adicionar um novo livro
        self.btn_add_book_fields = tk.Button(self, text="Add Book", command=self.add_book)
        self.btn_add_book_fields.grid(row=12, column=0, columnspan=2, padx=5, pady=5)
        # Botão para voltar ao menu principal
        self.btn_go_back_to_menu = tk.Button(self, text="Go Back", command=self.go_back_to_menu)
        self.btn_go_back_to_menu.grid(row=12, column=2, columnspan=2, padx=5, pady=5)

        self.grid()

    def add_book(self):
        title = self.entry_title.get()
        author = self.entry_author.get()
        year = self.entry_year.get()
        isbn = self.entry_isbn.get()
        pages = self.entry_pages.get()
        edition = self.entry_edition.get()
        publisher = self.entry_publisher.get()
        language = self.entry_language.get()
        genre = self.entry_genre.get()
        description = self.entry_description.get()
        image = self.entry_image.get()

        if not title or not author:
            messagebox.showerror("Error", "Title and Author are required fields.")
            return

        try:
            if year:
                year = int(year)
            if pages:
                pages = int(pages)
            database.add_book(title, author, year, isbn, pages, edition, publisher, language, genre, description, image)
            messagebox.showinfo("Success", "Book added successfully.")
        except ValueError:
            messagebox.showerror("Error", "Invalid year or pages number. Please enter a valid number.")

    def go_back_to_menu(self):
        self.destroy()  # Destrua a tela atual
        MainMenu(self.master)  # Cria a tela do menu principal novamente
