#!/bin/python3

class Book:
    """Represents a book with a title, author, and availability status."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Marks the book as checked out if it's available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Returns True if the book is available, False if checked out."""
        return not self._is_checked_out


class Library:
    """Represents a library containing a collection of books."""

    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Adds a new book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Checks out a book by its title if it's available."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"The book '{title}' has been checked out.")
                else:
                    print(f"Sorry, the book '{title}' is already checked out.")
                return
        print(f"Book titled '{title}' not found in the library.")

    def return_book(self, title):
        """Returns a book by its title to the library (makes it available)."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"The book '{title}' has been returned.")
                else:
                    print(f"The book '{title}' was not checked out.")
                return
        print(f"Book titled '{title}' not found in the library.")

    def list_available_books(self):
        """Lists all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No available books at the moment.")
