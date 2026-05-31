from flask import Flask, jsonify
from sqlalchemy import create_engine
from urllib.parse import quote_plus
import pandas as pd
import random
from datetime import datetime

app = Flask(__name__)

# ======================================
# AZURE POSTGRES CONNECTION
# ======================================

password = quote_plus("#Sqladmin")

engine = create_engine(
    f"postgresql+psycopg2://postgress:{password}@banking-postgres-server.postgres.database.azure.com:5432/bankingdb?sslmode=require"
)

# ======================================
# TRANSACTIONS API
# ======================================

@app.route('/transactions')
def transactions():

    query = """
    SELECT
        a.account_id,
        a.customer_id,
        a.branch_id,
        c.customer_name,
        b.branch_name
    FROM banking.accounts a
    JOIN banking.customers c
        ON a.customer_id = c.customer_id
    JOIN banking.branches b
        ON a.branch_id = b.branch_id
    ORDER BY RANDOM()
    LIMIT 1
    """

    df = pd.read_sql(query, engine)

    transaction = {

        "transaction_id":
            random.randint(
                100000000,
                999999999
            ),

        "account_id":
            int(df["account_id"][0]),

        "customer_id":
            int(df["customer_id"][0]),

        "customer_name":
            df["customer_name"][0],

        "branch_id":
            int(df["branch_id"][0]),

        "branch_name":
            df["branch_name"][0],

        "txn_type":
            random.choice([
                "DEBIT",
                "CREDIT"
            ]),

        "amount":
            round(
                random.uniform(
                    100,
                    50000
                ),
                2
            ),

        "txn_mode":
            random.choice([
                "UPI",
                "ATM",
                "CARD",
                "NEFT"
            ]),

        "txn_status":
            "SUCCESS",

        "txn_time":
            datetime.utcnow().isoformat()
    }

    return jsonify(transaction)

# ======================================
# HEALTH CHECK
# ======================================

@app.route('/')
def home():

    return jsonify({
        "status": "running",
        "service": "Banking Transaction API"
    })

# ======================================
# START APP
# ======================================

if __name__ == "__main__":
    app.run(debug=True)