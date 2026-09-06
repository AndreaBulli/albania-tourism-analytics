import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from pathlib import Path

# Load Data

project_root = Path(__file__).resolve().parent.parent
data_folder = project_root / "data"
file_path = data_folder / "tourism_monthly_analysis.csv"
df = pd.read_csv(file_path)


# Prepare Date

df["Year"] = pd.to_datetime(df["Month"]).dt.year
df["Month_Number"] = pd.to_datetime(df["Month"]).dt.month
df["Month_Name"] = pd.to_datetime(df["Month"]).dt.month_name()


# Tourism Analysis

yearly_arrivals = df[df["Visitor_Type"] == "non-residents"].groupby("Year")["Arrivals"].sum()
overall_stay = df.groupby("Visitor_Type")["Nights_Spent"].sum() / df.groupby("Visitor_Type")["Arrivals"].sum()
arrival_share = df[df["Visitor_Type"] != "Total"].groupby("Visitor_Type")["Arrivals"].sum()
arrival_share = arrival_share / arrival_share.sum()
nights_share = df[df["Visitor_Type"] != "Total"].groupby("Visitor_Type")["Nights_Spent"].sum()
nights_share = nights_share / nights_share.sum()


# Annual Tourism Arrivals

annual_arrivals = df[(df["Visitor_Type"] != "Total") & (df["Year"] < 2026)].groupby(["Year", "Visitor_Type"])["Arrivals"].sum().unstack()
annual_arrivals.plot(kind="bar", title="Annual Tourism Arrivals in Albania")
plt.ylabel("Arrivals (Millions)")
plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{x / 1_000_000:.1f}M"))
plt.xlabel("Year")
plt.xticks(rotation=0)
plt.savefig(project_root / "images" / "annual_tourism_arrivals.png", bbox_inches="tight")
plt.close()


# Monthly Tourism Seasonality

monthly_arrivals = df[(df["Visitor_Type"] == "non-residents") & (df["Year"] < 2026)].groupby("Month_Number")["Arrivals"].mean()
monthly_arrivals.index = pd.to_datetime(monthly_arrivals.index, format="%m").month_name()
plt.figure()
monthly_arrivals.plot(kind="line", marker="o", title="Average Monthly Non-Resident Arrivals")
plt.xlabel("Month")
plt.ylabel("Number of Arrivals")
plt.xticks(range(12), monthly_arrivals.index, rotation=45)
plt.savefig(project_root / "images" / "monthly_tourism_seasonality.png", bbox_inches="tight")
plt.close()


# Average Length of Stay

stay_comparison = overall_stay.drop("Total")
plt.figure()
stay_comparison.plot(kind="bar", title="Average Length of Stay by Visitor Type")
plt.xlabel("Visitor Type")
plt.ylabel("Average Length of Stay (Nights)")
plt.xticks(rotation=0)
plt.savefig(project_root / "images" / "average_length_of_stay.png", bbox_inches="tight")
plt.close()