class Books:
    def __init__(self, title: str, author: str, checked_out: bool, condition: int, due_date: str):
        self.title = title
        self.author = author
        self.checked_out = checked_out
        self.condition = condition
        self.due_date = due_date

    def update_condition(self):
        self.condition -= 1
        return self.condition

    def return_book(self):
        return self.checked_out is False

    def get_info(self):
        return f'Title: {self.title}\nAuthor: {self.author}'

    def provide_condition(self):
        if self.condition == 5:
            print('Perfect')
        elif self.condition == 4:
            print('Excellent')
        elif self.condition == 3:
            print('Good')
        elif self.condition == 2:
            print('OK')
        elif self.condition == 1:
            print('Poor')
        else:
            print('Unreadable')

    def set_due_date(self):
        return self.due_date == ""


all_books = [Books("1984", "George Orwell", False, 4, ""),
             Books("The Great Gatsby", "F. Scott Fitzgerald", True, 5, "2024-06-24"),
             Books("The Hobbit", "J.R.R. Tolkien", False, 2, ""),
             Books("Brave New World", "Aldous Huxley", False, 3, ""),
             Books("To Kill a Mockingbird", "Harper Lee", True, 1, "2024-06-18"),
             Books("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", False, 4, ""),
             Books("The Martian", "Andy Weir", True, 4, "2024-06-22"),
             Books("Beloved", "Toni Morrison", False, 5, ""),
             Books("The Road", "Cormac McCarthy", False, 4, ""),
             Books("The Name of the Wind", "Patrick Rothfuss", True, 2, "2024-06-14"),
             Books("The Handmaid's Tale", "Margaret Atwood", False, 3, ""),
             Books("The Night Circus", "Erin Morgenstern", True, 4, "2024-06-17"),
             Books("The Picture of Dorian Gray", "Oscar Wilde", False, 1, ""),
             Books("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", False, 3, "")]
