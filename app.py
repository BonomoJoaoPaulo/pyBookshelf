import database

menu = """Please select one of the following options:
1) Add new book
2) View all books
3) View readed books
4) Read a book
5) Add new reader
6) Delete a book
7) Delete a reader
8) Search for a book
9) Exit

Your selection: """
welcome = "Welcome to the pyBookshelf!"


def prompt_add_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    year = int(input("Enter book year: "))
    isbn = input("Enter book ISBN: ")
    pages = int(input("Enter book number of pages: "))
    edition = input("Enter book edition: ")
    publisher = input("Enter book publisher: ")
    language = input("Enter book language: ")
    genre = input("Enter book genre: ")
    description = input("Enter book description: ")
    image = input("Enter book image: ")

    database.add_book(title, author, year, isbn, pages, edition, publisher, language, genre, description, image)


def prompt_add_user():
    name = input("Enter reader name: ")
    surname = input("Enter reader surname: ")
    age = int(input("Enter reader age: "))

    database.add_reader(name, surname, age)


def print_book_list(heading, books):
    print(f"-- {heading} books --")
    print("------------------------------------")
    for book in books:
        print(f"""{book[1]} by {book[2]} ({book[3]})
            ID: {book[0]}
            Publisher: {book[7]}
            Pages Number: {book[5]}
            ISBN: {book[4]}
            Language: {book[8]}
            Edition: {book[6]}
            Genre: {book[9]}
        {book[10]}""")
    print("------------------------------------")
    print("END OF LIST.\n\n")


def print_readed_book_list(books, reader_id):
    reader_name = database.get_reader_name(reader_id)

    print(f"-- {reader_name}'s readed books --")
    print("------------------------------------")
    for book in books:
        print(f"""{book[1]} by {book[2]} ({book[3]})
            ID: {book[0]}
            Publisher: {book[7]}
            Pages Number: {book[5]}
            ISBN: {book[4]}
            Language: {book[8]}
            Edition: {book[6]}
            Genre: {book[9]}
        {book[10]}""")
    print("------------------------------------")
    print("END OF LIST.\n\n")


def prompt_read_book():
    reader_id = input("Enter the ID of the reader: ")
    book_id = input(f"Enter the ID of the book:: ")
    database.read_book(reader_id, book_id)


def prompt_search_book():
    search_title = input("Enter the partial title of the book you want to search: ")
    books = database.search_books(search_title)
    print_book_list("Search results: \n", books)


def prompt_delete_book():
    title = input("Enter the title of the book you want to delete: ")
    database.delete_book(title)


def prompt_delete_user():
    user_id = input("Enter the ID of the reader you want to delete: ")
    database.delete_reader(user_id)


print(welcome)
database.create_tables()

while (user_input := input(menu)) != "9":
    if user_input == "1":
        prompt_add_book()
    elif user_input == "2":
        books = database.get_books()
        print_book_list("All", books)
    elif user_input == "3":
        reader_id = input("Enter the ID of the reader: ")
        books = database.get_readed_books(reader_id)
        print_readed_book_list(books, reader_id)
    elif user_input == "4":
        prompt_read_book()
    elif user_input == "5":
        prompt_add_user()
    elif user_input == "6":
        prompt_delete_book()
    elif user_input == "7":
        prompt_delete_user()
    elif user_input == "8":
        prompt_search_book()
    else:
        print("Invalid input, please try again!\n")
