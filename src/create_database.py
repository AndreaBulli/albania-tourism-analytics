import pandas as pd
import sqlite3
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
data_folder = project_root / "data"

csv_path = data_folder / "tourism_monthly_analysis.csv"
df = pd.read_csv(csv_path)

database_path = project_root / "tourism_analysis.db"
conn = sqlite3.connect(database_path)

df.to_sql("tourism_monthly_analysis", conn, if_exists="replace", index=False)

conn.close()

print("Database created successfully.")