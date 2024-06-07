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
            user_actions.search_author()
        elif choice == '3':
            user_actions.search_title()
        elif choice == '4':
            user_actions.select_book()
        elif choice == "5":
            user_actions.return_book()
        elif choice == "6":
            user_actions.process_returns()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
