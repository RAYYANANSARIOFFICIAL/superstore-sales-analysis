
-- ==========================================
-- Project: Superstore Sales Analysis
-- Profit Analysis
-- ==========================================

USE superstore_analysis;

-- 1. Overall Profit
SELECT
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM superstore_cleaned_data;

-- 2. Year-wise Profit
SELECT
    YEAR(STR_TO_DATE(`Order Date`, '%d-%m-%Y')) AS Order_Year,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM superstore_cleaned_data
GROUP BY Order_Year
ORDER BY Order_Year;

-- 3. Region-wise Profit
SELECT
    Region,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM superstore_cleaned_data
GROUP BY Region
ORDER BY Total_Profit DESC;

-- 4. Category-wise Profit
SELECT
    Category,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM superstore_cleaned_data
GROUP BY Category
ORDER BY Total_Profit DESC;

-- 5. Sub-Category-wise Profit
SELECT
    `Sub-Category`,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM superstore_cleaned_data
GROUP BY `Sub-Category`
ORDER BY Total_Profit ASC;

-- 6. Top 10 Products by Profit
SELECT
    `Product Name`,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM superstore_cleaned_data
GROUP BY `Product Name`
ORDER BY Total_Profit DESC
LIMIT 10;

-- 7. Top 10 Customers by Profit
SELECT
    `Customer ID`,
    `Customer Name`,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM superstore_cleaned_data
GROUP BY `Customer ID`, `Customer Name`
ORDER BY Total_Profit DESC
LIMIT 10;
