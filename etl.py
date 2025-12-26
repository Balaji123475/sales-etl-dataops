import pandas as pd
from datetime import datetime
import os

def extract():
    data = {
        "item": ["apple", "banana", "apple", "mango"],
        "qty": [10, 5, 7, 3],
        "price": [50, 20, 50, 60]
    }
    df = pd.DataFrame(data)
    return df

def transform(df):
    df["revenue"] = df["qty"] * df["price"]
    df["load_date"] = datetime.now()
    return df

def load(df, output_path="/app/output/sales_data.parquet"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_parquet(output_path, index=False)
    print(f"✅ Data written to {output_path}")

def run_etl():
    df = extract()
    df = transform(df)
    load(df)

if __name__ == "__main__":
    run_etl()
# hi i am balaji
