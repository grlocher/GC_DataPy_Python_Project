import datetime
from media import all_books, Books


def book_display():
    for i, book in enumerate(all_books, 1):
        text = ''
        if book.checked_out:
            text = "is currently checked out. It\'s current condition is: "
        else:
            text = "is available. It\'s current condition is: "
        print(f'{i}. {book.title} by {book.author} {text}', end="")
        book.provide_condition()


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
    book = all_books[book_search - 1]
    if book.checked_out:
        print('Sorry, this book is not available at the moment')
    else:
        today = datetime.datetime.today()
        date_delta = datetime.timedelta(days=14)
        due_date = (today + date_delta).date()
        print(f'Here is {book.title}. Your due date is on {due_date}. Happy reading!')
        book.checked_out = True
        book.update_condition()


def add_book():
    new_title = str(input('Enter the title: ')).capitalize()
    new_author = str(input('Enter the author: ')).capitalize()
    checked_out = False
    print('From the following options, what is the condition of your book?')
    print('Excellent, Good, OK, Poor, Unreadable')
    condition = str(input('Condition: ')).capitalize()
    condition_dict = {'Perfect': 5, 'Excellent': 4, 'Good': 3, 'OK': 2, 'Poor': 1, 'Unreadable': 0}
    new_condition = condition_dict.get(condition)
    new_book = Books(new_title, new_author, checked_out, new_condition)
    all_books.append(new_book)
    print('Book has been added!')

add_book()
book_display()