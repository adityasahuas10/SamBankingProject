from faker import Faker
import pandas as pd
import random
import os
from datetime import datetime

# =========================================================
# CREATE DATASETS FOLDER
# =========================================================

os.makedirs("datasets", exist_ok=True)

# =========================================================
# INITIALIZE FAKER
# =========================================================

fake = Faker('en_IN')

# =========================================================
# 1. GENERATE CUSTOMERS DATA
# =========================================================

print("Generating customers data...")

customers = []

for i in range(50000):

    customers.append({

        "customer_id": i + 1,

        "customer_name": fake.name(),

        "age": random.randint(18, 75),

        "gender": random.choice([
            "Male",
            "Female"
        ]),

        "city": fake.city(),

        "state": fake.state(),

        "email": fake.unique.email(),

        "phone_number": fake.phone_number()
    })

customers_df = pd.DataFrame(customers)

customers_df.to_csv(
    "datasets/customers.csv",
    index=False
)

print("customers.csv generated")

# =========================================================
# 2. GENERATE BRANCHES DATA
# =========================================================

print("Generating branches data...")

branches = [

    [1, "Kolkata Main", "Kolkata", "West Bengal", "SBIN0001"],

    [2, "Mumbai Central", "Mumbai", "Maharashtra", "SBIN0002"],

    [3, "Delhi Branch", "Delhi", "Delhi", "SBIN0003"],

    [4, "Bangalore Tech", "Bangalore", "Karnataka", "SBIN0004"],

    [5, "Chennai South", "Chennai", "Tamil Nadu", "SBIN0005"]

]

branches_df = pd.DataFrame(

    branches,

    columns=[
        "branch_id",
        "branch_name",
        "city",
        "state",
        "ifsc_code"
    ]
)

branches_df.to_csv(
    "datasets/branches.csv",
    index=False
)

print("branches.csv generated")

# =========================================================
# 3. GENERATE ACCOUNTS DATA
# =========================================================

print("Generating accounts data...")

accounts = []

for i in range(100000):

    accounts.append({

        "account_id": i + 1,

        "customer_id": random.randint(1, 50000),

        "branch_id": random.randint(1, 5),

        "account_type": random.choice([
            "Savings",
            "Current"
        ]),

        "balance": round(
            random.uniform(1000, 500000),
            2
        ),

        "account_status": random.choice([
            "ACTIVE",
            "INACTIVE"
        ])
    })

accounts_df = pd.DataFrame(accounts)

accounts_df.to_csv(
    "datasets/accounts.csv",
    index=False
)

print("accounts.csv generated")

# =========================================================
# 4. GENERATE LOANS DATA
# =========================================================

print("Generating loans data...")

loans = []

for i in range(50000):

    loan_amount = random.randint(
        50000,
        5000000
    )

    loans.append({

        "loan_id": i + 1,

        "customer_id": random.randint(
            1,
            50000
        ),

        "loan_type": random.choice([
            "Home Loan",
            "Car Loan",
            "Personal Loan"
        ]),

        "loan_amount": loan_amount,

        "interest_rate": round(
            random.uniform(7, 15),
            2
        ),

        "emi_amount": round(
            loan_amount / 60,
            2
        ),

        "loan_status": random.choice([
            "ACTIVE",
            "CLOSED",
            "DEFAULT"
        ])
    })

loans_df = pd.DataFrame(loans)

loans_df.to_csv(
    "datasets/loans.csv",
    index=False
)

print("loans.csv generated")

# # =========================================================
# # 5. GENERATE TRANSACTIONS DATA
# # =========================================================

# print("Generating transactions data...")

# transactions = []

# txn_types = [
#     "DEBIT",
#     "CREDIT"
# ]

# txn_modes = [
#     "UPI",
#     "ATM",
#     "CARD",
#     "NEFT"
# ]

# locations = [
#     "Kolkata",
#     "Mumbai",
#     "Delhi",
#     "Bangalore",
#     "Chennai"
# ]

# for i in range(1000000):

#     txn_time = fake.date_time_between(
#         start_date='-90d',
#         end_date='now'
#     )

#     amount = round(
#         random.uniform(100, 200000),
#         2
#     )

#     transactions.append({

#         "transaction_id": i + 1,

#         "account_id": random.randint(
#             1,
#             100000
#         ),

#         "txn_type": random.choice(
#             txn_types
#         ),

#         "amount": amount,

#         "txn_status": random.choice([
#             "SUCCESS",
#             "FAILED"
#         ]),

#         "txn_mode": random.choice(
#             txn_modes
#         ),

#         "txn_location": random.choice(
#             locations
#         ),

#         "txn_time": txn_time
#     })

# # =========================================================
# # 6. ADD FRAUD TRANSACTIONS
# # =========================================================

# print("Adding fraudulent transactions...")

# fraud_account = 9999

# for i in range(500):

#     transactions.append({

#         "transaction_id": 1000001 + i,

#         "account_id": fraud_account,

#         "txn_type": "DEBIT",

#         "amount": random.randint(
#             500000,
#             2000000
#         ),

#         "txn_status": "SUCCESS",

#         "txn_mode": random.choice([
#             "UPI",
#             "CARD"
#         ]),

#         "txn_location": random.choice([
#             "Delhi",
#             "Mumbai",
#             "Kolkata",
#             "Chennai"
#         ]),

#         "txn_time": datetime.now()
#     })

# transactions_df = pd.DataFrame(
#     transactions
# )

# transactions_df.to_csv(
#     "datasets/transactions.csv",
#     index=False
# )

# print("transactions.csv generated")

# =========================================================
# COMPLETED
# =========================================================

print("\n===================================")
print("ALL DATA GENERATED SUCCESSFULLY")
print("===================================")

print("\nGenerated Files:")

print("1. datasets/customers.csv")
print("2. datasets/branches.csv")
print("3. datasets/accounts.csv")
print("4. datasets/loans.csv")
print("5. datasets/transactions.csv")