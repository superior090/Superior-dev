import json
import os
import math

BOOKS_FILE = "books.json"

class Book:
    def __init__(self, title, author, price, stock):
        self.title = title
        self.author = author
        self.price = round(price, 2)  
        self.stock = stock

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "price": self.price,
            "stock": self.stock
        }

    @staticmethod
    def from_dict(data):
        return Book(data["title"], data["author"], data["price"], data["stock"])

def load_inventory():
    if not os.path.exists(BOOKS_FILE):
        return []
    with open(BOOKS_FILE, "r") as file:
        data = json.load(file)
        return [Book.from_dict(item) for item in data]

def save_inventory(inventory):
    with open(BOOKS_FILE, "w") as file:
        json.dump([book.to_dict() for book in inventory], file, indent=4)

def add_book(inventory, book):
    inventory.append(book)
    save_inventory(inventory)

def search_books(inventory, keyword):
    return [book for book in inventory if keyword.lower() in book.title.lower()]