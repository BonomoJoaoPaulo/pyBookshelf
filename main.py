import tkinter as tk
from tkinter import messagebox
import database

# Função para adicionar um novo livro ao banco de dados
def add_book():
    title = entry_title.get()
    author = entry_author.get()
    year = entry_year.get()
    isbn = entry_isbn.get()
    pages = entry_pages.get()
    edition = entry_edition.get()
    publisher = entry_publisher.get()
    language = entry_language.get()
    genre = entry_genre.get()
    description = entry_description.get()
    image = entry_image.get()

    if not title or not author:
        messagebox.showerror("Error", "Title and Author are required fields.")
        return

    try:
        year = int(year)
        pages = int(pages)
        database.add_book(title, author, year, isbn, pages, edition, publisher, language, genre, description, image)
        messagebox.showinfo("Success", "Book added successfully.")
    except ValueError:
        messagebox.showerror("Error", "Invalid year or pages number. Please enter a valid number.")

# Criação da janela principal
root = tk.Tk()
root.title("pyBookshelf")

# Criação dos campos de entrada para adicionar um novo livro
label_title = tk.Label(root, text="Title*:")
label_title.pack()
entry_title = tk.Entry(root)
entry_title.pack()

label_author = tk.Label(root, text="Author*:")
label_author.pack()
entry_author = tk.Entry(root)
entry_author.pack()

label_year = tk.Label(root, text="Year:")
label_year.pack()
entry_year = tk.Entry(root)
entry_year.pack()

label_isbn = tk.Label(root, text="ISBN:")
label_isbn.pack()
entry_isbn = tk.Entry(root)
entry_isbn.pack()

label_pages = tk.Label(root, text="Pages:")
label_pages.pack()
entry_pages = tk.Entry(root)
entry_pages.pack()

label_edition = tk.Label(root, text="Edition:")
label_edition.pack()
entry_edition = tk.Entry(root)
entry_edition.pack()

label_publisher = tk.Label(root, text="Publisher:")
label_publisher.pack()
entry_publisher = tk.Entry(root)
entry_publisher.pack()

label_language = tk.Label(root, text="Language:")
label_language.pack()
entry_language = tk.Entry(root)
entry_language.pack()

label_genre = tk.Label(root, text="Genre:")
label_genre.pack()
entry_genre = tk.Entry(root)
entry_genre.pack()

label_description = tk.Label(root, text="Description:")
label_description.pack()
entry_description = tk.Entry(root)
entry_description.pack()

label_image = tk.Label(root, text="Image:")
label_image.pack()
entry_image = tk.Entry(root)
entry_image.pack()

# Botão para adicionar um novo livro
btn_add_book = tk.Button(root, text="Add Book", command=add_book)
btn_add_book.pack()

# Configurando o tamanho padrão da janela
root.geometry("800x600")

# Inicie o loop principal do Tkinter
root.mainloop()
