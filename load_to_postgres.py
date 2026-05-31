# =========================================================

# PROJECT : Banking Data Engineering Platform

# MODULE  : PostgreSQL Data Loader

# AUTHOR  : Aditya Sahu

#

# PURPOSE :

# Load Branches, Customers and Accounts data

# into Azure PostgreSQL.

#

# SOURCE FILES :

# datasets/branches.csv

# datasets/customers.csv

# datasets/accounts.csv

#

# TARGET TABLES :

# banking.branches

# banking.customers

# banking.accounts

#

# =========================================================

from sqlalchemy import create_engine
import pandas as pd
from urllib.parse import quote_plus

# =========================================================

# AZURE POSTGRESQL CONNECTION

# =========================================================

password = quote_plus("#Sqladmin")

engine = create_engine(
f"postgresql+psycopg2://postgress:{password}@banking-postgres-server.postgres.database.azure.com:5432/bankingdb?sslmode=require"
)

print("=" * 60)
print("BANKING DATA LOAD STARTED")
print("=" * 60)

# =========================================================

# LOAD BRANCHES

# =========================================================

print("\nLoading branches...")

branches_df = pd.read_csv("datasets/branches.csv")

branches_df.to_sql(
name="branches",
con=engine,
schema="banking",
if_exists="append",
index=False
)

print(f"Branches Loaded : {len(branches_df)}")

# =========================================================

# LOAD CUSTOMERS

# =========================================================

print("\nLoading customers...")

customers_df = pd.read_csv("datasets/customers.csv")

customers_df.to_sql(
name="customers",
con=engine,
schema="banking",
if_exists="append",
index=False,
method="multi"
)

print(f"Customers Loaded : {len(customers_df)}")

# =========================================================

# LOAD ACCOUNTS

# =========================================================

print("\nLoading accounts...")

accounts_df = pd.read_csv("datasets/accounts.csv")

accounts_df.to_sql(
name="accounts",
con=engine,
schema="banking",
if_exists="append",
index=False,
method="multi"
)

print(f"Accounts Loaded : {len(accounts_df)}")

# =========================================================

# VALIDATION

# =========================================================

with engine.connect() as conn:
    branches_count = pd.read_sql(
    "SELECT COUNT(*) AS cnt FROM banking.branches",
    conn
    )

    customers_count = pd.read_sql(
    "SELECT COUNT(*) AS cnt FROM banking.customers",
    conn
    )

    accounts_count = pd.read_sql(
    "SELECT COUNT(*) AS cnt FROM banking.accounts",
    conn
    )

print("\n" + "=" * 60)
print("DATA LOAD COMPLETED")
print("=" * 60)

print(f"Branches  : {branches_count.iloc[0]['cnt']}")
print(f"Customers : {customers_count.iloc[0]['cnt']}")
print(f"Accounts  : {accounts_count.iloc[0]['cnt']}")

print("\nAll tables loaded successfully.")