import time
import os
import pandas as pd
import hashlib
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError


DB_HOST = os.environ.get('DB_HOST', 'db')
DB_USER = os.environ.get('DB_USER', 'user')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'password')
DB_NAME = os.environ.get('DB_NAME', 'telecom')

# Wait for DB to be ready
max_tries = 10
for i in range(max_tries):
    try:
        engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}")
        # Try connecting
        with engine.connect() as conn:
            print("Database is ready!")
        break
    except OperationalError:
        print(f"Database not ready, retrying ({i+1}/{max_tries})...")
        time.sleep(5)
else:
    print("Database connection failed after several attempts.")
    exit(1)

# Read the CSV file
df = pd.read_csv('/data/customer_churn_data.csv')

# Load to staging table
df.to_sql('staging_churn', engine, if_exists='replace', index=False)

# --- Transformation logic ---

df.fillna({
    'TotalCharges': 0.0,
    'InternetService': 'Unknown',
    'MonthlyCharges': 0.0,
    'ContractType': 'One-Year',
    'Age': 0,
    'Gender': 'Unknown',
    'Tenure': 0,
    'TechSupport': 'Unknown',
    'Churn': 'Unknown'    
}, inplace=True)

# Anonymize PII 
if 'CustomerID' in df.columns:
    df['CustomerID'] = df['CustomerID'].apply(lambda x: hashlib.sha256(str(x).encode()).hexdigest())

df.to_sql('reporting_churn', engine, if_exists='replace', index=False)

print("Cron Job successfully completed!")
