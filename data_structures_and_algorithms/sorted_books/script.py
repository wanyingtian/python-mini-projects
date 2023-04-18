import utils
import sorts

bookshelf = utils.load_books('books_small.csv')
for book in bookshelf:
  print(book['title'])