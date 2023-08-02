import database

menu = """Please select one of the following options:
1) Add new book
2) View all books
3) View readed books
4) View not readed books
5) Read a book
6) Exit

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


def print_book_list(heading, books):
    print(f"-- {heading} books --")
    print("------------------------------------")
    for book in books:
        print(f"""{book[0]} by {book[1]} ({book[2]})
            Publisher: {book[6]}
            Pages Number: {book[4]}
            ISBN: {book[3]}
            Language: {book[7]}
            Edition: {book[5]}
            Genre: {book[8]}
        {book[9]}""")
    print("------------------------------------")
    print("END OF LIST.\n\n")


def prompt_read_book():
    title = input("Enter the title of the book you just finished reading: ")
    database.read_book(title)


print(welcome)
database.create_tables()

while (user_input := input(menu)) != "6":
    if user_input == "1":
        prompt_add_book()
    elif user_input == "2":
        books = database.get_books()
        print_book_list("All", books)
    elif user_input == "3":
        books = database.get_readed_books()
        print_book_list("Readed", books)
    elif user_input == "4":
        books = database.get_not_readed_books()
        print_book_list("Not readed", books)
    elif user_input == "5":
        prompt_read_book()
    else:
        print("Invalid input, please try again!\n")
