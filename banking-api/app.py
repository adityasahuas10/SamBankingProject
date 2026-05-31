from flask import Flask, jsonify
from sqlalchemy import create_engine
from urllib.parse import quote_plus
import pandas as pd
import random
import os
from datetime import datetime

app = Flask(__name__)

# =========================================================
# DATABASE CONFIGURATION
# =========================================================

DB_HOST = os.environ.get(
    "DB_HOST",
    "banking-postgres-server.postgres.database.azure.com"
)

DB_NAME = os.environ.get(
    "DB_NAME",
    "bankingdb"
)

DB_USER = os.environ.get(
    "DB_USER",
    "postgress"
)

DB_PASSWORD = os.environ.get(
    "DB_PASSWORD",
    "#Sqladmin"
)

password = quote_plus(DB_PASSWORD)

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{password}@{DB_HOST}:5432/{DB_NAME}?sslmode=require"
)

# =========================================================
# HOME API
# =========================================================

@app.route("/")
def home():

    return jsonify({
        "status": "running",
        "project": "Azure Banking API",
        "available_endpoints": [
            "/health",
            "/transactions"
        ]
    })

# =========================================================
# HEALTH API
# =========================================================

@app.route("/health")
def health():

    try:

        query = """
        SELECT COUNT(*) AS total_accounts
        FROM banking.accounts
        """

        df = pd.read_sql(query, engine)

        return jsonify({
            "status": "healthy",
            "database": "connected",
            "total_accounts": int(df["total_accounts"][0])
        })

    except Exception as e:

        return jsonify({
            "status": "unhealthy",
            "error": str(e)
        }), 500

# =========================================================
# TRANSACTIONS API
# =========================================================

@app.route("/transactions")
def transactions():

    try:

        query = """
        SELECT
            a.account_id,
            a.customer_id,
            a.branch_id,
            a.account_type,
            a.balance,
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

        txn_type = random.choice([
            "DEBIT",
            "CREDIT"
        ])

        amount = round(
            random.uniform(
                100,
                50000
            ),
            2
        )

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
                str(df["customer_name"][0]),

            "branch_id":
                int(df["branch_id"][0]),

            "branch_name":
                str(df["branch_name"][0]),

            "account_type":
                str(df["account_type"][0]),

            "current_balance":
                float(df["balance"][0]),

            "transaction_type":
                txn_type,

            "transaction_mode":
                random.choice([
                    "UPI",
                    "ATM",
                    "CARD",
                    "NEFT",
                    "IMPS"
                ]),

            "amount":
                amount,

            "status":
                random.choice([
                    "SUCCESS",
                    "SUCCESS",
                    "SUCCESS",
                    "FAILED"
                ]),

            "transaction_time":
                datetime.utcnow().isoformat()
        }

        return jsonify(transaction)

    except Exception as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

# =========================================================
# APPLICATION ENTRY POINT
# =========================================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )