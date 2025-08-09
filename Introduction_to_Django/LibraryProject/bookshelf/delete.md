from bookshelf.models import Book

# retrieve book
book = Book.objects.get(title="Nineteen Eighty-Four")   
# delete book
book.delete()                                        
# retrieve all
book.objects.all()
# expected output: <QuerySet []>