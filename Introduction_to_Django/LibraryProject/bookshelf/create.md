from bookshelf.models import Book

# create book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
# display book
print(book)
# expected output:      1984 by George Orwell, 1949