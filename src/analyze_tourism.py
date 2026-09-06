import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
data_folder = project_root / "data"
file_path = data_folder / "tourism_monthly_analysis.csv"
df = pd.read_csv(file_path)
#print(df.head())
#print(df.info())
#print(df["Visitor_Type"].value_counts())
#print(df.groupby("Visitor_Type")["Arrivals"].sum())
#print(df.groupby("Visitor_Type")["Nights_Spent"].sum())
#print(df.groupby("Visitor_Type")["Average_Length_of_Stay"].mean())
#print(df[df["Visitor_Type"] == "non-residents"].nlargest(5, "Arrivals")[["Month", "Arrivals"]])
#print(df[df["Visitor_Type"] == "residents"].nlargest(5, "Arrivals")[["Month", "Arrivals"]])
df["Year"] = pd.to_datetime(df["Month"]).dt.year
print(df[df["Visitor_Type"] == "non-residents"].groupby("Year")["Arrivals"].sum())

yearly_arrivals = df[df["Visitor_Type"] == "non-residents"].groupby("Year")["Arrivals"].sum()
#print(yearly_arrivals.pct_change() * 100)
#print(df[df["Visitor_Type"] == "non-residents"].groupby("Year")["Nights_Spent"].sum())
overall_stay = df.groupby("Visitor_Type")["Nights_Spent"].sum() / df.groupby("Visitor_Type")["Arrivals"].sum()
#print(overall_stay)
df["Month_Number"] = pd.to_datetime(df["Month"]).dt.month
print(df[df["Visitor_Type"] == "non-residents"].groupby("Month_Number")["Arrivals"].mean())
df["Month_Name"] = pd.to_datetime(df["Month"]).dt.month_name()

print(df[df["Visitor_Type"] == "non-residents"].groupby(["Month_Number", "Month_Name"])["Arrivals"].mean())
#print(df[df["Visitor_Type"] == "non-residents"].nlargest(1, "Arrivals")[["Month", "Arrivals"]])
#print(df[df["Visitor_Type"] == "non-residents"].nsmallest(1, "Arrivals")[["Month", "Arrivals"]])
arrival_share = df[df["Visitor_Type"] != "Total"].groupby("Visitor_Type")["Arrivals"].sum() / df[df["Visitor_Type"] != "Total"]["Arrivals"].sum() * 100
#print(arrival_share)
nights_share = df[df["Visitor_Type"] != "Total"].groupby("Visitor_Type")["Nights_Spent"].sum() / df[df["Visitor_Type"] != "Total"]["Nights_Spent"].sum() * 100
#print(nights_share)
#print(df[df["Visitor_Type"] != "Total"].groupby(["Year", "Visitor_Type"])["Arrivals"].sum())
annual_arrivals = df[(df["Visitor_Type"] != "Total") & (df["Year"] < 2026)].groupby(["Year", "Visitor_Type"])["Arrivals"].sum().unstack()
annual_arrivals.plot(kind="bar", title="Annual Tourism Arrivals in Albania")
plt.ylabel("Arrivals (Millions)")
plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{x / 1_000_000:.1f}M"))
plt.xlabel("Year")
plt.xticks(rotation=0)
plt.savefig(project_root / "images" / "annual_tourism_arrivals.png", bbox_inches="tight")
#plt.show()
monthly_arrivals = df[df["Visitor_Type"] == "non-residents"].groupby("Month_Number")["Arrivals"].mean()
monthly_arrivals.index = pd.to_datetime(monthly_arrivals.index, format="%m").month_name()
plt.figure()
monthly_arrivals.plot(kind="line", marker="o", title="Average Monthly Non Resident Arrivals")
plt.xlabel("Month")
plt.ylabel("Number of Arrivals")
plt.xticks(range(1, 13), monthly_arrivals.index, rotation=45)
plt.savefig(project_root / "images" / "monthly_tourism_seasonality.png", bbox_inches="tight")
#plt.show()
stay_comparison = overall_stay.drop("Total")
plt.figure()
stay_comparison.plot(kind="bar", title="Average Length of Stay by Visitor Type")
plt.xlabel("Visitor Type")
plt.ylabel("Average Length of Stay (Nights)")
plt.xticks(rotation=0)
plt.savefig(project_root / "images" / "average_length_of_stay.png", bbox_inches="tight")
#plt.show()
