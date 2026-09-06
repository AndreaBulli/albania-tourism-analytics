SELECT
    Visitor_Type,
    SUM(Arrivals) AS Total_Arrivals
FROM tourism_monthly_analysis
WHERE Visitor_Type != 'Total'
GROUP BY Visitor_Type
ORDER BY Total_Arrivals DESC;

SELECT
    Visitor_Type,
    SUM(Nights_Spent) AS Total_Nights_Spent
FROM tourism_monthly_analysis
WHERE Visitor_Type != 'Total'
GROUP BY Visitor_Type
ORDER BY Total_Nights_Spent DESC;

SELECT
    Visitor_Type,
    ROUND(SUM(Nights_Spent) * 1.0 / SUM(Arrivals), 2) AS Average_Length_of_Stay
FROM tourism_monthly_analysis
WHERE Visitor_Type != 'Total'
GROUP BY Visitor_Type
ORDER BY Average_Length_of_Stay DESC;

SELECT
    Month,
    Arrivals
FROM tourism_monthly_analysis
WHERE Visitor_Type = 'non-residents'
ORDER BY Arrivals DESC
LIMIT 1;

SELECT
    SUBSTR(Month, 1, 4) AS Year,
    SUM(Arrivals) AS Total_Arrivals
FROM tourism_monthly_analysis
WHERE Visitor_Type = 'non-residents'
GROUP BY Year
ORDER BY Year;

WITH yearly_arrivals AS (
    SELECT
        SUBSTR(Month, 1, 4) AS Year,
        SUM(Arrivals) AS Total_Arrivals
    FROM tourism_monthly_analysis
    WHERE Visitor_Type = 'non-residents'
    GROUP BY Year
)
SELECT
    Year,
    Total_Arrivals,
    LAG(Total_Arrivals) OVER (ORDER BY Year) AS Previous_Year_Arrivals
FROM yearly_arrivals
ORDER BY Year;