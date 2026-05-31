-- Create Schema
CREATE SCHEMA IF NOT EXISTS banking;

-- ==========================================
-- CUSTOMERS
-- ==========================================

CREATE TABLE IF NOT EXISTS banking.customers
(
    customer_id BIGINT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    age INT,
    gender VARCHAR(10),
    city VARCHAR(50),
    state VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    phone_number VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ==========================================
-- BRANCHES
-- ==========================================

CREATE TABLE IF NOT EXISTS banking.branches
(
    branch_id BIGINT PRIMARY KEY,
    branch_name VARCHAR(100) NOT NULL,
    city VARCHAR(50),
    state VARCHAR(50),
    ifsc_code VARCHAR(20) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ==========================================
-- ACCOUNTS
-- ==========================================

CREATE TABLE IF NOT EXISTS banking.accounts
(
    account_id BIGINT PRIMARY KEY,
    customer_id BIGINT NOT NULL,
    branch_id BIGINT NOT NULL,
    account_type VARCHAR(20),
    balance NUMERIC(15,2),
    account_status VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_customer
        FOREIGN KEY (customer_id)
        REFERENCES banking.customers(customer_id),

    CONSTRAINT fk_branch
        FOREIGN KEY (branch_id)
        REFERENCES banking.branches(branch_id)
);

-- ==========================================
-- INDEXES
-- ==========================================

CREATE INDEX IF NOT EXISTS idx_accounts_customer
ON banking.accounts(customer_id);

CREATE INDEX IF NOT EXISTS idx_accounts_branch
ON banking.accounts(branch_id);