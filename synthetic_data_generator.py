import csv
import random
import string
from datetime import datetime, timedelta

# Define the number of transac, the number of unique traders,
# and the number of traders who are in both the buyer and seller IDs
num_transac = 15000
num_unique_traders = 14785
num_shared_traders = 215

# Generate a list of unique trader IDs
unique_trader_ids = [''.join(random.choices(string.ascii_uppercase + string.digits, k=4)) for _ in range(num_unique_traders)]

# Choose a few traders who are in both the buyer and seller IDs
shared_traders = random.sample(unique_trader_ids, num_shared_traders)

# Combine the unique and shared traders to create the full list of trader IDs
trader_ids = unique_trader_ids + shared_traders

# Initialize an empty list to store the transac
transac = []

# Generate random transac
start_date = datetime(2022, 1, 1)
for i in range(num_transac):
    # Choose a random buyer and seller from the list of traders
    buyer = random.choice(trader_ids)
    seller = random.choice(trader_ids)

    # Generate a random amount between 1,000 and 10,00,000 INR
    amount = random.randint(1000, 1000000)

    # Generate a random date within the first quarter of 2022
    date = start_date + timedelta(days=random.randint(0, 89))

    # Append the transaction to the list
    transac.append((i+1, buyer, seller, amount, date.strftime('%Y-%m-%d')))

    # If the buyer is also a seller, choose another random seller to trade with
    # and generate a second transaction in the opposite direction (i.e., seller buys from buyer)
    if buyer == seller and buyer in shared_traders:
        other_seller = random.choice([s for s in shared_traders if s != seller])
        other_amount = random.randint(1000, min(amount, 5000))
        other_date = start_date + timedelta(days=random.randint(0, 89))
        transac.append((i+1, seller, other_seller, other_amount, other_date.strftime('%Y-%m-%d')))
        transac.append((i+1, other_seller, buyer, other_amount, other_date.strftime('%Y-%m-%d')))

# Save the transac as a CSV file
with open('Data_Files\\Synthetic_Data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['TransactionID', 'BuyerID', 'SellerID', 'Amount(INR)', 'Date'])
    for transaction in transac:
        # Write the transaction to the CSV file
        writer.writerow(transaction)



