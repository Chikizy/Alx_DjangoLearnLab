from bookshelf.models import Book
#  RETRIEVE BOOK
# retrieve the book
retr_book = Book.objects.get(title="1984")
# get book title
Book.objects.get(id = book.id).title()    
#  Expected output:'1984'
#               OR
print(retr_book)
#  Expected output: 1984 by George Orwell, 1949
#           OR
# print book title
print(book.title)
# expected output: 1984
