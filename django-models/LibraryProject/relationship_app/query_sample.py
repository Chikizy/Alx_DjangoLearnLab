from .models import Author, Book, Librarian, Library

def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books

def list_books(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

def get_lib_librarian(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian