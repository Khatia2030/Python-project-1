# წიგნის კლასის განსაზღვრა
class Book:
    # კონსტრუქტორი (__init__) აინიციალიზებს წიგნის ობიექტს, რომელსაც აქვს სათაური, ავტორი და გამოსვლის წელი.
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        # აბრუნებს სტრინგს ფორმატში
        return f"{self.title} by {self.author}, {self.year}"

# წიგნების მართვის კლასის განსაზღვრა
class BookManager:
    # კონსტრუქტორი (__init__) ინიციალიზებს ცარიელ სიას წიგნების შესანახად.
    def __init__(self):
        # ცარიელი სია წიგნების მონაცემების შესანახად
        self.books = [] 
    # add_book წიგნის დამატება სიაში.
    def add_book(self, title: str, author: str, year: int):
        # ვალიდაცია: სათაური და ავტორი არ შეიძლება იყოს ცარიელი, წელი უნდა იყოს დადებითი მთელი რიცხვი2
        if not title or not author or not isinstance(year, int) or year <= 0:
            print("Invalid book details. Please try again.")
            return
        book = Book(title, author, year)
        self.books.append(book)
        print("Book added successfully!")

    def list_books(self):
        if not self.books:
            print("No books available.")
            return
        print("\nBook List:")
        for book in self.books:
            print(book)
    # search_book მეთოდი ეძებს წიგნს სათაურით.
    def search_book(self, title: str):
        found_books = [book for book in self.books if book.title.lower() == title.lower()]
        if found_books:
            print("\nSearch Results:")
            for book in found_books:
                print(book)
        else:
            print("Book not found.")

# მთავარი ფუნქცია, მომხმარებელის მხარე
def main():
    # BookManager კლასის ობიექტი, რომელიც მართავს წიგნების კოლექციას
    manager = BookManager()
    # ციკლი, მენიუსთვის, მომხმარებლის მიერ მენიუს არჩევა
    while True:
        print("\nBook Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            try:
                year = int(input("Enter publication year: "))
                manager.add_book(title, author, year)
            except ValueError:
                print("Invalid year. Please enter a valid number.")
        elif choice == "2":
            manager.list_books()
        elif choice == "3":
            title = input("Enter book title to search: ")
            manager.search_book(title)
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# მთავარი ფუნქციის გაშვება
if __name__ == "__main__":
    main()
