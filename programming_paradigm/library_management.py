# library_management.py

class Book:
    def __init__(self, title: str, author: str):
        """Initialize a Book with public title, author and private availability flag"""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Mark the book as checked out"""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as available"""
        self._is_checked_out = False

    def is_available(self) -> bool:
        """Return True if the book is available, False if checked out"""
        return not self._is_checked_out

    def __str__(self):
        """String representation of the book"""
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        """Initialize the Library with a private list of books"""
        self._books = []

    def add_book(self, book: Book):
        """Add a Book instance to the library"""
        self._books.append(book)

    def check_out_book(self, title: str):
        """Check out a book by title if available"""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        print(f"Book '{title}' is not available for checkout.")

    def return_book(self, title: str):
        """Return a book by title"""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return
        print(f"Book '{title}' was not checked out or does not exist.")

    def list_available_books(self):
        """Print all available books in the library"""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No available books.")
        else:
            for book in available_books:
                print(book)