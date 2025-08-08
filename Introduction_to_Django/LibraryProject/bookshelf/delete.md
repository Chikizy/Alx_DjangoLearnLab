from bookshelf.models import Book

del_book = Book.objects.filter(title="Nineteen Eighty-Four").delete()