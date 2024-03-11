import time
import sys

# bookshelf class should have a Donate, Update Book, Delete Book, Borrow a book, display all books, rating, search for a book, exit
# have a book class, which should have a title author genre price amount rating 



class Book:
    def __init__(self, title, author, genre, price, amount, rating): 
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        self.amount = amount
        self.available_amount = amount
        self.rating = [rating]


class Bookshelf:
    def __init__(self):
        self.inventory = []

    def slow_text(self,text):
        for char in text:
            print(char, end="", flush=True)
            time.sleep(0.04)
        

    def add_book(self, book):
        self.inventory.append(book)

    def update_book(self):
        pass

    def delete_book(self, title):
        updated = []
        for book in self.inventory:
            if book.title.title() != title.title():
                updated.append(book)
        self.inventory = updated

        return self.inventory
    
    def borrow_book(self, title):
        for book in self.inventory:
            if book.title == title:
                if book.available_amount > 0:
                    book.available_amount -=1
                    print(f"The book {title} has been borrowed")
                    print("\n")
                else:
                    print(f"Sorry, the book {title} is not available")
                    print("\n")
        
        
            else:
                print(f"There is no book called {title} in the library")
                print("\n")

    def return_book(self, title):
        for book in self.inventory:
            if book.title == title:
                if book.available_amount < book.amount : # come back to
                    book.available_amount +=1
                    print(f"The book {title} has been returned")
                    print("\n")
                else:
                    print(f"Sorry, the book {title} was not borrowed from the library")
                    print("\n")
    
        print(f"There is no book called {title} in the library")
        print("\n")

            
    def display_all_books(self):
        if not self.inventory:
            print("The library is empty. No books to display.")
        else:
            print("All Books in the Library:")
            for book in self.inventory:
                print("Book Details:")
                print(f"Title: {book.title}")
                print(f"Author: {book.author}")
                print(f"Genre: {book.genre}")
                print(f"Price: {book.price}")
                print(f"Amount: {book.amount}")
                print(f"Available: {book.available_amount}")
                print(f"Rating: {book.rating}")
                print("------------------------")

    def display_popular_books(self): # revist in the future
        pass

        


    def search_books(self, title): # add this later
        for book in self.inventory:
            if book.title.title() == title.title():
                print(f"Title: {book.title}")
                print(f"Author: {book.author}")
                print(f"Genre: {book.genre}")
                print(f"Price: {book.price}")
                print(f"Amount: {book.amount}")
                print(f"Available: {book.available_amount}")
                print(f"Rating: {book.rating}")
            else:
                print(f"No book with the title {title} within the library")
        



       

    def average_rating(self, title, new_rating):
        total_rating = 0
        total_length = 0

        # we first find the book in the inventory
        for book in self.inventory:
            if book.title.title() == title.title():
                total_rating += sum(book.rating)  # takes the sum of the rating of the book in interation
                total_length += len(book.rating)  # takes the length of the current list
                book.rating.append(new_rating)  # Add the new rating to the book's ratings

        # the plus one for the new_rating
        average = (total_rating + new_rating) / (total_length + 1)

        # updating the average rating for all books with the same title
        for book in self.inventory:
            if book.title.title() == title.title():
                book.rating = average





def main():
    shelf = Bookshelf()

    shelf.slow_text("Welcome to our virtual Bookstore! How can we assist you?")
    print("\n")
    while True:
        print("1. Donate a book")
        print("2. Update a book's contents (coming soon)")
        print("3. Delete a book")
        print("4. Borrow a book")
        print("5. Return a book")
        print("6. Display all the books")
        print("7. Search")
        print("8. Leave a rating")
        print("9. Exit")
        print("------------------------")
        choice = input("What would you like to do: ")

        if choice == "1":
            shelf.slow_text("Could you provide more details about the book you'd like to donate?")
            print("\n")
            title = input("Enter the title of the book: ").title()
            author = input("Enter the author of the book: ")
            genre = input("Enter the genre of the book: ")

            price_valid = False
            while not price_valid:
                try:
                    price = float(input("Enter the price of the book: "))
                    price_valid = True
                except ValueError:
                    print("Invalid price. Please enter a numeber.")

            amount = int(input("Enter the amount of copies you want to donate: "))

            donated = True
            while donated:
                if amount > 10:
                    print("You donated to many copies try again: ")
                    amount = int(input("Enter the amount of copies you want to donate: "))
                else:
                    donated = False

            rating_vaild = False
            while not rating_vaild:
                try:
                    rating = float(input("Enter the rating of the book: "))
                    rating_vaild = True
                except ValueError:
                    print("Invalid rating. Please enter a number.")
            book = Book(title, author, genre, price, amount, rating)
            shelf.add_book(book)
            shelf.slow_text("Thank you fo your addition!")
            print("\n")
        elif choice == "2":
            pass
        elif choice == "3":
            title = input("Enter the title of the book you want to delete from the library: ").title()
            shelf.delete_book(title)
        elif choice == "4":
            title = input("Enter the title of the book you want to borrow: ").title()
            shelf.borrow_book(title)
        elif choice == "5":
            title = input("Enter the title of the book you want to return: ").title()
            shelf.return_book(title)
        elif choice == "6":
            shelf.display_all_books()
        elif choice == "7":
            title = input("Enter for the title you are searching for: ")
            shelf.search_books(title)
        elif choice == "8":
            title = input("Enter the title of the book you want to rate: ")
            new_rating = int(input("What would you rate this book: "))
            shelf.average_rating(title, new_rating)
        elif choice == "9":
            shelf.slow_text("Have a wonderful day, and we hope to see you again soon!")
            sys.exit()
        else:
            shelf.slow_text("I'm sorry, I don't understand the following input. Please try again")
main()


                
    