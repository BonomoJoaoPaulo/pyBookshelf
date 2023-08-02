import database

menu = """Please select one of the following options:
1) Add new book
2) View all books
3) Read a book
4) View readed books
5) Exit

Your selection: """
welcome = "Welcome to the pyBookshelf!"


print(welcome)
database.create_tables()

while (user_input := input(menu)) != "5":
    if user_input == "1":
        pass
    elif user_input == "2":
        pass
    elif user_input == "3":
        pass
    elif user_input == "4":
        pass
    else:
        print("Invalid input, please try again!")
