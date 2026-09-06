import pandas as pd
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
data_folder = project_root / "data"
arrivals = pd.read_csv(data_folder / "cleaned_monthly_arrivals.csv")
nights = pd.read_csv(data_folder / "cleaned_monthly_nights_spent.csv")

print(arrivals.head())
print(nights.head())

arrivals["Visitor_Type"] = arrivals["Description"].str.replace("Arrivals of ", "").str.replace("Total arrivals", "Total")
nights["Visitor_Type"] = nights["Description"].str.replace("Nights spent of ", "").str.replace("Total nights spent", "Total")
nights["Visitor_Type"] = nights["Visitor_Type"].str.replace(r"^Nights spent\s+of\s+", "", regex=True)
arrivals["Description"] = arrivals["Description"].str.replace("Arrivals of ", "").str.replace("Total arrivals", "Total")
nights["Description"] = nights["Description"].str.replace("Nights spent of ", "").str.replace("Total nights spent", "Total")
nights["Description"] = nights["Description"].str.replace(r"^Nights spent\s+of\s+", "", regex=True)
combined = pd.merge(arrivals, nights, on=["Description", "Month", "Visitor_Type"], how="inner")
combined["Average_Length_of_Stay"] = combined["Nights_Spent"] / combined["Arrivals"]
output_path = data_folder / "tourism_monthly_analysis.csv"
combined.to_csv(output_path, index=False)
print(combined.columns.tolist())
print(combined.head(10))
#print(combined["Visitor_Type"].unique())
#print(arrivals["Visitor_Type"].unique())
#print(nights["Visitor_Type"].unique())
#print(combined["Visitor_Type"].unique())

#print(arrivals["Description"].unique())
#print(nights["Description"].unique())