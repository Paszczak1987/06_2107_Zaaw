from modele import Author
from modele import Book

authors_list = [
    Author("Adam", "Mickiewicz"),
    Author("Henryk", "Sienkiewicz"),]

books_list = [
    Book("Pan Tadeusz", authors_list[0]),
    Book("Potop", authors_list[1]),
]


###################
#     Autorzy     #
###################
def add_author():
    name = input("Podaj imię: ")
    surname = input("Podaj nazwisko: ")
    authors_list.append(Author(name, surname))

def show_authors(authors):
    for author in authors:
        print(f"{author.id}: {author}")
        
def update_author(authors):
    id = input("Podaj id autora: ")
    updating_author = None
    for author in authors:
        if author.id == int(id):
            updating_author = author
            break
    if updating_author is None:
        print("Nie ma takiego autora")
    else:
        name = input("Podaj imię: ")
        surname = input("Podaj nazwisko: ")
        updating_author.first_name = name
        updating_author.last_name = surname
       
def author_service():
    while True:
        user_input = input("""
1 - Dodaj Autora
2 - Wypisz Autorów
3 - Modyfikuj Autora
q - Wyjdź
""")
        if user_input == "1":
            add_author()
        elif user_input == "2":
            show_authors(authors_list)
        elif user_input == "3":
            update_author(authors_list)
        elif user_input == "q":
            break
        
###################
#     Książki     #
###################

def add_book():
    title = input("Podaj tytuł: ")
    show_authors(authors_list)
    author_id = input("Podaj id autora: ")
    book_author = None
    for author in authors_list:
        if author.id == int(author_id):
            book_author = author
            break
    books_list.append(Book(title, book_author))
    
def show_books(books):
    for book in books:
        print(f"{book.id}: {book}")
        
def update_book(books):
    id = input("Podaj id książki: ")
    updating_book = None
    for book in books:
        if book.id == int(id):
            updating_book = book
    if updating_book is None:
        print("Książka nie istnieje")
    else:
        title = input("Podaj tytuł: ")
        show_authors(authors_list)
        author_id = input("Podaj id autora: ")
        book_author = None
        for author in authors_list:
            if author.id == int(author_id):
                book_author = author
                break
        updating_book.title = title
        updating_book.author = book_author

def book_service():
    while True:
        user_input = input("""
1 - Dodaj Książkę
2 - Wypisz Książki
3 - Modyfikuj Książkę
q - Wyjdź
""")
        if user_input == "1":
            add_book()
        elif user_input == "2":
            show_books(books_list)
        elif user_input == "3":
            update_book(books_list)
        elif user_input == "q":
            break


while True:
    books_of_authors = input("Co robimy?\n1 - Autorzy\n2 - Książki\nq - Zakończ\n")
    if books_of_authors == "1":
        author_service()
    elif books_of_authors == "2":
        book_service()
    elif books_of_authors == "q":
        break
    
    