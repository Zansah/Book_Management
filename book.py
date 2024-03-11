import time
import sys

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
            if book.title != title:
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

            
    def display_books(self, title):
        for book in self.inventory:
            if book.title == title:
                print("Book Details")
                print(f"Title: {book.title}")
                print(f"Author: {book.author}")
                print(f"Genre: {book.genre}")
                print(f"Price: {book.price}")
                print(f"Quanitity: {book.amount}")
                print(f"Available: {book.available_amount}")
                print(f"Rating: {book.rating}")
            else:
                print(f"{title} was not found within the library here are all the books")
                print("\n")
                for book in self.inventory:
                    print(f"Title: {book.title}, Author: {book.author} ")
                    print("\n")

       

    def average_rating(self):
        pass


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
        print("7. Leave a rating")
        print("8. Exit")
        print("------------------------")
        choice = input("What would you like to do: ")

        if choice == "1":
            shelf.slow_text("Could you provide more details about the book you'd like to donate?")
            print("\n")
            title = input("Enter the title of the book: ").title()
            author = input("Enter the author of the book: ")
            genre = input("Enter the genre of the book: ")
            price = float(input("Enter the price of the book: "))
            amount = int(input("Enter the amount of books you want to donate: "))
            rating = float(input("Enter the rating for the book: "))
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
            title = input("Enter the title of the book you want to display")
            shelf.display_books(title)
        elif choice == "7":
            pass
        elif choice == "8":
            shelf.slow_text("Have a wonderful day, and we hope to see you again soon!")
            sys.exit()
        else:
            shelf.slow_text("I'm sorry, I don't understand the following input. Please try again")
main()


                
    