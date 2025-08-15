from bookshelf.models import Book

# CREATE BOOK
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
# display book          
print(book)  
# expected output:      1984 by George Orwell, 1949

# RETRIEVE BOOK
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

# UPDATE BOOK
# retrieve book
book = Book.objects.get(title='1984')
# update title
book.title = 'Nineteen Eighty Four'
# display book
print(book.title)
#  Expected output:'Nineteen Eighty-Four'
#               OR
print(book)
#  Expected output: Nineteen Eighty Four by George Orwell, 1949

#  retrieve book
book = Book.objects.get(title="Nineteen Eighty-Four")   
# delete book
book.delete()                                        
# retrieve all
book.objects.all()
# expected output: <QuerySet []>