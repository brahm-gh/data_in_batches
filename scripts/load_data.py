import pandas as pd
from pymongo import MongoClient
import os

# Load the CSV data
csv_path = os.path.join("data", "T1.csv")
df = pd.read_csv(csv_path)

# Convert Date/Time to ISO format
df["Date/Time"] = pd.to_datetime(df["Date/Time"], format="%d %m %Y %H:%M")

# Connect to MongoDB
client = MongoClient("mongodb://mongo:27017/")
db = client["sensor_db"]
collection = db["wind_turbine_data"]

# Insert data in batches
batch_size = 1000
for start in range(0, len(df), batch_size):
    end = start + batch_size
    batch = df.iloc[start:end].to_dict(orient="records")
    collection.insert_many(batch)

print("Data loaded successfully.")
