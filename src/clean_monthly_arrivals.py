import pandas as pd
from pathlib import Path


# Load data

project_root = Path(__file__).resolve().parent.parent
data_folder = project_root / "data"
file_path = data_folder / "m06_2026-tab_1_vizitorë.xlsx"

df = pd.read_excel(file_path, header=4)
df.columns = [str(col).strip() for col in df.columns]


# Clean data

df = df.drop(columns=["Përshkrimi"])
df = df.rename(columns={col: f"20{col[-2:]}-{col[:2]}" for col in df.columns if "-" in col})

df_long = df.melt(id_vars="Description", var_name="Month", value_name="Arrivals")
df_long["Month"] = pd.to_datetime(df_long["Month"], format="%Y-%m")


# Save data

output_path = data_folder / "cleaned_monthly_arrivals.csv"
df_long.to_csv(output_path, index=False)