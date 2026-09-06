# Albania Tourism Analytics

## Project Overview

This project analyzes tourism trends in Albania using official monthly tourism data from the Albanian Institute of Statistics (INSTAT).

The analysis focuses on visitor arrivals, nights spent, seasonal tourism patterns, and average length of stay for resident and non resident visitors. Python and Pandas were used to clean, transform, and analyze the data, while SQLite and SQL were used for additional querying and analysis. Matplotlib was used to create visualizations highlighting major tourism trends.

## Data Source

The data used in this project comes from the Albanian Institute of Statistics (INSTAT), Albania's official statistical agency.

The dataset contains monthly tourism statistics covering January 2021 through June 2026.

The analysis includes:

- Total visitor arrivals
- Resident visitor arrivals
- Non resident visitor arrivals
- Total nights spent
- Nights spent by residents
- Nights spent by non-residents

Source: INSTAT Tourism Statistics

## Tools & Technologies

- Python
- Pandas
- Matplotlib
- SQLite
- SQL
- PyCharm
- Git & GitHub

## Data Cleaning and Preparation

The original INSTAT tourism data was provided in Excel format and required several cleaning and transformation steps before analysis.

Using Python and Pandas, I:

- Loaded and inspected the original Excel datasets
- Cleaned and standardized column names
- Reshaped monthly data from wide to long format using `melt()`
- Standardized resident and non resident visitor categories
- Converted monthly values into a consistent date format
- Merged visitor arrival and nights spent datasets
- Calculated average length of stay
- Exported a final analysis ready CSV dataset
- Loaded the processed dataset into a SQLite database for SQL analysis

The final combined dataset contains 198 records covering monthly tourism activity from January 2021 through June 2026.

## Analysis

The project examines several aspects of Albania's tourism activity, including:

- Total arrivals by visitor type
- Total nights spent by visitor type
- Average length of stay
- Annual tourism growth
- Monthly tourism seasonality
- Peak tourism months
- Resident vs. non resident tourism patterns

SQL was also used to reproduce and validate several findings from the Python analysis.

## Key Findings

### Non Resident Tourism Growth

Non resident visitor arrivals increased substantially between 2021 and 2025:

- 2021: 685,081
- 2022: 886,515
- 2023: 1,409,327
- 2024: 2,185,093
- 2025: 3,039,712

The 2026 data covers only January through June and is therefore not directly comparable with the completed calendar years of previous data.

### Visitor Composition

Across the full dataset:

- Non residents accounted for approximately 66.15% of visitor arrivals.
- Residents accounted for approximately 33.85% of visitor arrivals.
- Non residents accounted for approximately 69.35% of total nights spent.
- Residents accounted for approximately 30.65% of total nights spent.

### Average Length of Stay

Average length of stay was calculated using total nights spent divided by total arrivals:

- Non-residents: approximately 2.48 nights
- Residents: approximately 2.14 nights

Non resident visitors therefore stayed longer on average than resident visitors.

### Tourism Seasonality

The monthly analysis shows a strong seasonal tourism pattern, with visitor activity increasing significantly during the summer months.

The highest single month for non-resident arrivals in the dataset was August 2025, with 650,108 arrivals.

## Visualizations

### Annual Tourism Arrivals

![Annual Tourism Arrivals](images/annual_tourism_arrivals.png)

This visualization compares annual resident and non resident visitor arrivals. Only complete calendar years from 2021 through 2025 are included to avoid comparing full years with partial 2026 data.

### Monthly Tourism Seasonality

![Monthly Tourism Seasonality](images/monthly_tourism_seasonality.png)

This visualization shows the average monthly pattern of non resident arrivals and highlights the strong increase in tourism activity during the summer season.

### Average Length of Stay

![Average Length of Stay](images/average_length_of_stay.png)

This visualization compares the average length of stay for resident and non-resident visitors.

## SQL Analysis

The processed tourism dataset was loaded into a SQLite database for additional analysis.

SQL queries were used to analyze:

- Total arrivals by visitor type
- Total nights spent by visitor type
- Average length of stay
- Peak non-resident tourism month
- Annual non-resident arrivals
- Previous-year arrival comparisons using the `LAG()` window function

The SQL queries are available in:

`sql/analysis_queries.sql`

## Project Structure

```text
albania-tourism-analytics/
│
├── data/
│   ├── cleaned_monthly_arrivals.csv
│   ├── cleaned_monthly_nights_spent.csv
│   └── tourism_monthly_analysis.csv
│
├── images/
│   ├── annual_tourism_arrivals.png
│   ├── monthly_tourism_seasonality.png
│   └── average_length_of_stay.png
│
├── sql/
│   └── analysis_queries.sql
│
├── src/
│   ├── analyze_tourism.py
│   ├── clean_monthly_arrivals.py
│   ├── combine_data.py
│   ├── create_database.py
│   └── explore_data.py
│
├── tourism_analysis.db
├── README.md
└── requirements.txt