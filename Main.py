import user_actions


def main():

    while True:
        # Displaying the menu options
        print('\nLibrary Terminal')
        print('1. Display all books')
        print('2. Search for a book by author')
        print('3. Search for a book by title')
        print('4. Checkout a book')
        print('5. Return a book')
        print('6. Process returned books')
        print('7. Add a new book')
        print('8. Exit')
        choice = input('Please choose which action you would like to take (1-7): ')

        # Handling different choices made by the user
        if choice == '1':
            # Display all books
            user_actions.book_display()
        elif choice == '2':
            # Search for a book by author
            user_actions.search_author()
        elif choice == '3':
            # Search for a book by title
            user_actions.search_title()
        elif choice == '4':
            # Checkout a book
            user_actions.select_book()
        elif choice == "5":
            # Return a book
            user_actions.return_book()
        elif choice == "6":
            # Process returned books--is this needed?
            user_actions.process_returns()
        elif choice == "7":
            user_actions.add_book()
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
