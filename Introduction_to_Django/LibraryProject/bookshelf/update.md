from bookshelf.models import Book

# retrieve book
book = Book.objects.get(title='1984')
# update title
book.title = 'Nineteen Eighty Four'
# save changes
book.save
# confirm changes
print(book.title)
# expected result: Nineteen Eighty Four