from bookshelf.models import Book

del_book = Book.objects.get(title="Nineteen Eighty-Four").delete()