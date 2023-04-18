import utils
import sorts
import timer


bookshelf = utils.load_books('books_small.csv')
long_bookshelf = utils.load_books('books_large.csv')
for book in bookshelf:
  print(book['title'])

# comparison functions
def by_title_ascending(book_a, book_b):
  return book_a['title_lower'] > book_b['title_lower']
def by_author_ascending(book_a, book_b):
  return book_a['author_lower'] > book_b['author_lower']
def by_total_length(book_a, book_b):
  return len(book_a['title_lower']) + len(book_a['author_lower']) > len(book_b['title_lower']) + len(book_b['author_lower']) 

print("\n1. Small Bookshelf Sorting: By Title Ascending\n")
timer.tic()
sort_1_b = sorts.bubble_sort(bookshelf, by_title_ascending)
timer.toc()
timer.tic()
sort_1_q = sorts.quicksort(bookshelf, 0, len(bookshelf)-1, by_title_ascending)
print("Quicksort:")
timer.toc()

print("\n2. Small Bookshelf Sorting: By Author Ascending\n")
bookshelf_v1 = bookshelf.copy()
timer.tic()
sort_2_b = sorts.bubble_sort(bookshelf_v1, by_author_ascending)
timer.toc()

bookshelf_v2 = bookshelf.copy()
timer.tic()
sort_2_q = sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2)-1,by_author_ascending)
print("Quicksort:")
timer.toc()

print("\n3. Large Bookshelf Sorting: By Total Length\n")
timer.tic()
sort_3_b = sorts.bubble_sort(long_bookshelf, by_total_length)
timer.toc()

timer.tic()
sort_3_q = sorts.quicksort(long_bookshelf, 0, len(long_bookshelf)-1, by_total_length)
print("Quicksort:")
timer.toc()
