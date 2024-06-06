import datetime
import media

book_title = book[0]
book_author = book[1]
checked_out = book[2]
book_condtion = book[3]

# Display the entire list of books. Format it nicely - Possibly done?
def book_display():
    for i, book in enumerate(all_books, 1):
        if checked_out:
            print(f'{i}. {book_title} by {book_author} is currently checked out. It\'s current condition is: {book_condtion}')
        else:
            print(f'{i}. {book_title} by {book_author} is available. It\'s current condition is: {book_condtion}')

# Search for a book by author - Possibly done?
def search_author():
    author_search = str(input('Search for a book by author: '))
    matching_books = []
    for book in all_books:
        if author_search in book_author:
            matching_books.append()
            print(f'{book_title} by {book_author}')

# Search for a book by title keyword - Possibly done?
def search_title():
    title_search = str(input('Search for a book by title: '))
    matching_books = []
    for book in all_books:
        if title_search in book_title:
            matching_books.append()
            print(f'{book_title} by {book_author}')

# Select a book from the list to check out - DONE
# If it’s already checked out, let them know - DONE
# If not, check it out to them and set the due date to 2 weeks from today. Also degrade the condition of the book - DONE
def select_book():
    book_search = str(input('Enter the book you would like to search for: '))
    if book_search == book_title:
        if checked_out == True:
            print('Sorry, this book is not available at the moment')
        else:
            today = datetime.datetime.today()
            date_delta = datetime.timedelta(days=14)
            due_date = today + date_delta
            print(f'Here is {book_title}. Your due date is on {due_date}. Happy reading!')
        # Update status to checked out
            book[2] = True
        # Degrade book condition by 1 with 0 being the lowest
            book[3] = book_condtion - 1


# Take in a book object and add it to a stack or queue representing book returns
# First check the condition of the book, if it is too degraded, recycle it, which will remove it from circulation.
# If the books ' condition is okay, update the due dates to null, and set the status of the books as on shelf
def return_book():