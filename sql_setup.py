import sqlite3
import pandas as pd


BASE_PATH = r"C:\Users\kavi vala\Desktop\superstore dashbord"
df = pd.read_csv(f"{BASE_PATH}\\data\\Superstore_Management_System_Generated.csv")


conn = sqlite3.connect(f"{BASE_PATH}\\database\\superstore.db")
df.to_sql("orders", conn, if_exists="replace", index=False)
conn.close()
print("✅ SQL Database Created")