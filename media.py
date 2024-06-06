class Books:
    def __init__(self, title: str, author: str, checked_out: bool, condition: int):
        self.title = title
        self.author = author
        self.checked_out = checked_out
        self.condition = condition

    def update_condition(self):
        self.condition -= 1
        return self.condition

    def get_info(self):
        return f'Title: {self.title}\nAuthor: {self.author}'


all_books = [Books("1984", "George Orwell", False, 4),
             Books("The Great Gatsby", "F. Scott Fitzgerald", True, 5),
             Books("The Hobbit", "J.R.R. Tolkien", False, 2),
             Books("Brave New World", "Aldous Huxley", False, 3),
             Books("To Kill a Mockingbird", "Harper Lee", True, 1),
             Books("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", False, 4),
             Books("The Martian", "Andy Weir", True, 4),
             Books("Beloved", "Toni Morrison", False, 5),
             Books("The Road", "Cormac McCarthy", False, 4),
             Books("The Name of the Wind", "Patrick Rothfuss", True, 2),
             Books("The Handmaid's Tale", "Margaret Atwood", False, 3),
             Books("The Night Circus", "Erin Morgenstern", True, 4),
             Books("The Picture of Dorian Gray", "Oscar Wilde", False, 1),
             Books("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", False, 3)]

# print(f'Starting Condition: {all_books[0].condition}')
# all_books[0].update_condition()
# print(f'Updated Condition: {all_books[0].condition}')

'''
class Media:
    def __init__(self, title: int, checked_out: bool)
    self.title = title
    self.checked_out = checked_out


class Books(Media):
    def __init__(self, title: str, author: str, checked_out: bool, condition: int):
        super()__init__(title, checked_out)
        self.author = author
        self.condition = condition
        
    def update_condition(self):
        self.condition -= 1
        return self.condition

    def get_info(self):
        return f'Title: {self.title}\nAuthor: {self.author}'
 
    
class Movies(Media):
    def __init__(self, title: int, director: str, runtime: int, checked_out: bool)
    super()__init__(title, checked_out)
    self.director = director
    self.runtime = runtime
    
    def get_info(self):
        return f'Title: {self.title}\nDirector: {self.director}\nRuntime: {self.runtime}'


all media = {
'movies': [],
'books': [Books("1984", "George Orwell", False, 4),
             Books("The Great Gatsby", "F. Scott Fitzgerald", True, 5),
             Books("The Hobbit", "J.R.R. Tolkien", False, 2),
             Books("Brave New World", "Aldous Huxley", False, 3),
             Books("To Kill a Mockingbird", "Harper Lee", True, 1),
             Books("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", False, 4),
             Books("The Martian", "Andy Weir", True, 4),
             Books("Beloved", "Toni Morrison", False, 5),
             Books("The Road", "Cormac McCarthy", False, 4),
             Books("The Name of the Wind", "Patrick Rothfuss", True, 2),
             Books("The Handmaid's Tale", "Margaret Atwood", False, 3),
             Books("The Night Circus", "Erin Morgenstern", True, 4),
             Books("The Picture of Dorian Gray", "Oscar Wilde", False, 1),
             Books("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", False, 3)]
}


'''
