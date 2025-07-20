from inventory import Book, load_inventory, add_book, search_books

def main():
    inventory = load_inventory()
    print("📚 Bookstore Inventory System")

    while True:
        print("\n1. Add Book\n2. Search Book\n3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            price = float(input("Price: "))
            stock = int(input("Stock: "))
            book = Book(title, author, price, stock)
            add_book(inventory, book)
            print("✅ Book added successfully.")

        elif choice == "2":
            keyword = input("Enter title to search: ")
            results = search_books(inventory, keyword)
            if results:
                for b in results:
                    print(f"{b.title} by {b.author} - ${b.price} [{b.stock} in stock]")
            else:
                print("No books found.")

        elif choice == "3":
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main() 