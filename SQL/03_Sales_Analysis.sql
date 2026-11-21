
-- ==========================================
-- Project: Superstore Sales Analysis
-- Sales Analysis
-- ==========================================

USE superstore_analysis;

-- 1. Overall Sales
SELECT
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM superstore_cleaned_data;

-- 2. Year-wise Sales
SELECT
    YEAR(STR_TO_DATE(`Order Date`, '%d-%m-%Y')) AS Order_Year,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM superstore_cleaned_data
GROUP BY Order_Year
ORDER BY Order_Year;

-- 3. Region-wise Sales
SELECT
    Region,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM superstore_cleaned_data
GROUP BY Region
ORDER BY Total_Sales DESC;

-- 4. Category-wise Sales
SELECT
    Category,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM superstore_cleaned_data
GROUP BY Category
ORDER BY Total_Sales DESC;

-- 5. Segment-wise Sales
SELECT
    Segment,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM superstore_cleaned_data
GROUP BY Segment
ORDER BY Total_Sales DESC;

-- 6. Ship Mode-wise Sales
SELECT
    `Ship Mode`,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM superstore_cleaned_data
GROUP BY `Ship Mode`
ORDER BY Total_Sales DESC;

-- 7. Top 10 Products by Sales
SELECT
    `Product Name`,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM superstore_cleaned_data
GROUP BY `Product Name`
ORDER BY Total_Sales DESC
LIMIT 10;
