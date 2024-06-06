import user_actions
def main():

    while True:
        print('\nLibrary Terminal')
        print('1. Display all books')
        print('2. Search for a book by author')
        print('3. Search for a book by title keyword')
        print('4. Checkout a book')
        print('5. Return a book')
        print('6. Process returned books')
        print('7. Exit')
        choice = input('Please choose which action you would like to take (1-7): ')

        if choice == '1':
            user_actions.book_display()
        elif choice == '2':
            author = input("Enter the author's name: ")
            results = user_actions.search_author(author)
            if results:
                for book in results:
                    print(book.get_info())
                    print("-" * 40)
            else:
                print("No books found by that author.")
        elif choice == '3':
            keyword = input('Enter the title keyword: ')
            results = user_actions.search_title(keyword)
            if results:
                for book in results:
                    print(book.get_info())
                    print("-" * 40)
            else:
                print("No books found with that keyword.")
        elif choice == '4':
            book_title = input("Enter the title of the book to check out: ")
            user_actions.checkout_book(book_title)
        elif choice == "5":
            book_title = input("Enter the title of the book to return: ")
            user_actions.return_book(book_title)
        elif choice == "6":
            user_actions.process_returns()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
