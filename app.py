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


def print_book_list(books):
    pass


print(welcome)
database.create_tables()

while (user_input := input(menu)) != "6":
    if user_input == "1":
        prompt_add_book()
    elif user_input == "2":
        pass
    elif user_input == "3":
        pass
    elif user_input == "4":
        pass
    elif user_input == "5":
        pass
    else:
        print("Invalid input, please try again!")
