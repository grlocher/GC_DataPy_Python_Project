import user_actions


def main():

    while True:
        print('\nLibrary Terminal')
        print('1. Display all books')
        print('2. Search for a book by author')
        print('3. Search for a book by title')
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
            title = input('Enter the title: ')
            results = user_actions.search_title(title)
            if results:
                for book in results:
                    print(book.get_info())
                    print("-" * 40)
            else:
                print("No books found with that title.")
        elif choice == '4':
            book_title = input("Which book would you like to checkout?: ")
            user_actions.select_book(book_title)
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
