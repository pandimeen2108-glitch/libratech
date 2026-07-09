from abc import ABC, abstractmethod

# ------------------ Abstraction ------------------
class LibrarySystem(ABC):

    @abstractmethod
    def display_details(self):
        pass


# ------------------ Encapsulation ------------------
class Book(LibrarySystem):

    def __init__(self, book_id, title, author):
        self.__book_id = book_id      # Private variable
        self.__title = title
        self.__author = author
        self.__available = True

    # Getter methods
    def get_book_id(self):
        return self.__book_id

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def is_available(self):
        return self.__available

    # Setter method
    def set_available(self, status):
        self.__available = status

    # Implementing abstract method
    def display_details(self):
        status = "Available" if self.__available else "Issued"
        print(f"ID: {self.__book_id}")
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")
        print(f"Status: {status}")
        print("-------------------------")


# ------------------ Inheritance ------------------
class Library(Book):

    def __init__(self):
        self.books = []

    def add_book(self):
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        book = Book(book_id, title, author)
        self.books.append(book)

        print("Book Added Successfully!")

    def display_books(self):
        if len(self.books) == 0:
            print("No books available.")
        else:
            for book in self.books:
                book.display_details()

    def issue_book(self):
        book_id = input("Enter Book ID to Issue: ")

        for book in self.books:
            if book.get_book_id() == book_id:
                if book.is_available():
                    book.set_available(False)
                    print("Book Issued Successfully!")
                else:
                    print("Book is already issued.")
                return

        print("Book Not Found.")

    def return_book(self):
        book_id = input("Enter Book ID to Return: ")

        for book in self.books:
            if book.get_book_id() == book_id:
                if not book.is_available():
                    book.set_available(True)
                    print("Book Returned Successfully!")
                else:
                    print("Book was not issued.")
                return

        print("Book Not Found.")


# ------------------ Polymorphism ------------------
class EBook(Book):
    def display_details(self):
        status = "Available" if self.is_available() else "Issued"
        print("E-BOOK DETAILS")
        print(f"ID: {self.get_book_id()}")
        print(f"Title: {self.get_title()}")
        print(f"Author: {self.get_author()}")
        print(f"Status: {status}")
        print("-------------------------")


# ------------------ Main Program ------------------
library = Library()

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Polymorphism Demo")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.display_books()

    elif choice == "3":
        library.issue_book()

    elif choice == "4":
        library.return_book()

    elif choice == "5":
        ebook = EBook("E101", "Python eBook", "John")
        ebook.display_details()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")