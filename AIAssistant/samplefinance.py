import pandas as pd
import random
from datetime import datetime, timedelta

# Define random transaction details
transaction_details = [
    ("Hotel ABC", "Debit"), ("Gas Station XYZ", "Debit"), ("Restaurant Delight", "Debit"),
    ("Coffee Shop Bliss", "Debit"), ("Online Store A1", "Debit"), ("Utility Bill - Electric", "Debit"),
    ("Utility Bill - Water", "Debit"), ("Salary Credit", "Credit"), ("ATM Withdrawal", "Debit"),
    ("Subscription Service", "Debit"), ("Friend John", "Credit"), ("Family Member Lisa", "Credit"),
    ("Insurance Premium", "Debit"), ("Car Service Center", "Debit"), ("Health Clinic", "Debit")
]

# Function to generate random transactions
def generate_transactions(start_date, num_days, num_entries):
    transactions = []
    for _ in range(num_entries):
        # Randomize date within the range
        date = start_date + timedelta(days=random.randint(0, num_days))
        time = f"{random.randint(1, 12):02}:{random.randint(0, 59):02} {'AM' if random.random() < 0.5 else 'PM'}"
        date_str = date.strftime(f"%b %d, %Y\n{time}")

        # Randomly select transaction details
        detail, transaction_type = random.choice(transaction_details)

        # Generate amount based on transaction type
        amount = round(random.uniform(50, 10000), 2) if transaction_type == "Debit" else round(random.uniform(1000, 50000), 2)

        # Create description
        account = "XX1382"
        description = f"{'Paid to' if transaction_type == 'Debit' else 'Received from'} {detail}\n{'Debited from' if transaction_type == 'Debit' else 'Credited to'} {account}"

        transactions.append((date_str, description, transaction_type, f"INR {amount:,.2f}"))
    return transactions

# Generate six months of transactions
start_date = datetime(2023, 1, 1)
num_days = 180
num_entries = 50
transactions = generate_transactions(start_date, num_days, num_entries)

# Convert to DataFrame
df = pd.DataFrame(transactions, columns=["Date", "Transaction Details", "Type", "Amount"])

# Save to Excel
excel_filename = "sample_bank_statement.xlsx"
df.to_excel(excel_filename, index=False)

print(f"Bank statement saved to {excel_filename}")
