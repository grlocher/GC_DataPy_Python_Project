import datetime
from media import all_books, Books


def book_display():
    for i, book in enumerate(all_books, 1):
        if book.checked_out:
            print(f'{i}. {book.title} by {book.author} is currently checked out. It\'s current condition is: {book.condition}')
        else:
            print(f'{i}. {book.title} by {book.author} is available. It\'s current condition is: {book.condition}')


def search_author():
    author_search = str(input('Search for a book by author: ')).lower()
    for book in all_books:
        if author_search in book.author.lower():
            print(f'{book.title} by {book.author}')


def search_title():
    title_search = str(input('Search for a book by title: ')).lower()
    for book in all_books:
        if title_search in book.title.lower():
            print(f'{book.title} by {book.author}')


def select_book():
    book_search = int(input('Enter the book you would like to check out: '))
    book = all_books[book_search]
    if book.checked_out:
        print('Sorry, this book is not available at the moment')
    else:
        today = datetime.datetime.today()
        date_delta = datetime.timedelta(days=14)
        due_date = (today + date_delta).date()
        print(f'Here is {book.title}. Your due date is on {due_date}. Happy reading!')
    # Update status to checked out
        book.checked_out = True
    # Degrade book condition by 1 with 0 being the lowest
        book.update_condition()
