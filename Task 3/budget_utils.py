import json
import os
from datetime import datetime

BUDGET_FILE = "transactions.json"

class Transaction:
    def __init__(self, date, category, amount):
        self.date = date  
        self.category = category
        self.amount = amount

    def to_dict(self):
        return {
            "date": self.date,
            "category": self.category,
            "amount": self.amount
        }

    @staticmethod
    def from_dict(data):
        return Transaction(data["date"], data["category"], data["amount"])

def load_transactions():
    if not os.path.exists(BUDGET_FILE):
        return []
    with open(BUDGET_FILE, "r") as f:
        data = json.load(f)
        return [Transaction.from_dict(t) for t in data]

def save_transactions(transactions):
    with open(BUDGET_FILE, "w") as f:
        json.dump([t.to_dict() for t in transactions], f, indent=4)

def add_transaction(transactions, transaction):
    transactions.append(transaction)
    save_transactions(transactions)

def group_by_category(transactions):
    grouped = {}
    for t in transactions:
        if t.category not in grouped:
            grouped[t.category] = 0
        grouped[t.category] += t.amount
    return grouped

def total_expenses(transactions):
    return sum(t.amount for t in transactions)