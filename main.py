

class Library:

    def __init__(self, list_of_books, library_name):
        self.lend_data = {}
        self.list_of_books = list_of_books
        self.library_name = library_name

        for books in self.lend_data:
            self.lend_data[books] = None

    def display_books(self):
        return self.list_of_books

    def lend_book(self, book, reader):
        if book in self.list_of_books:
            if self.lend_data[book] is None:
                self.lend_data[book] = reader
                return "You have borrowed the book."
            else:
                return f"Book not available. It is borrowed by {self.lend_data[book]}"
        else:
            return "You have written a wrong book name"

    def add_book(self, book_name):
        self.list_of_books.append(book_name)
        self.lend_data[book_name] = None
    
    def return_book(self, book, reader):
        if book in self.list_of_books:
            if self.lend_data[book] is not None:
                self.lend_data.pop(book)
            else:
                return "Sorry but this book is not borrowed by anyone"
        else:
            return "You have written a wrong book name"


def main():
        books_in_aaryan_library = ["The Power Of Our Subconsious Mind", "Anna Karenina",
        "To Kill a Mockingbird", "The Great Gatsby", "One Hundred Years of Solitude"]
        libraryname = "Aaryan"

        Aaryan = Library(books_in_aaryan_library, libraryname)
    
        print(f"Welcome to {libraryname} library \n Press q For Exitting The Library \n Press d for Displaying Books \n Press l to Lend A Book \n Press r to Return a Book \n Press a To Add A Book In Library")

        Exit = False

        while(Exit is False):
            user_input = input("option : ")

            if user_input == 'q':
                Exit = True
            
            if user_input == 'd':
                print(Aaryan.display_books())
            
            if user_input == 'l':
                lend_person_name = input("Enter Your Full Name \n")
                lend_book_name = input("Enter the name of book you want to borrow \n")
                print(Aaryan.lend_book(lend_person_name, lend_book_name))

            if user_input == 'r':
                return_person_name = input("Enter Your Full Name \n")
                return_book_name = input("Enter the name of book you want to return \n")
                print(Aaryan.return_book(return_book_name, return_person_name))
                
            if user_input == 'a':
                add_book_name = input("Enter the name of book you want to add in the library \n")
                print(Aaryan.add_book(add_book_name))
            
if __name__ == "__main__":
    main()
