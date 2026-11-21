
-- ==========================================
-- Project: Superstore Sales Analysis
-- Data Exploration
-- ==========================================

USE superstore_analysis;

-- 1. View first 10 records
SELECT *
FROM superstore_cleaned_data
LIMIT 10;

-- 2. Check total records
SELECT COUNT(*) AS Total_Records
FROM superstore_cleaned_data;

-- 3. Count unique orders, customers and products
SELECT
    COUNT(DISTINCT `Order ID`) AS Total_Orders,
    COUNT(DISTINCT `Customer ID`) AS Total_Customers,
    COUNT(DISTINCT `Product ID`) AS Total_Products
FROM superstore_cleaned_data;

-- 4. Check minimum and maximum sales
SELECT
    MIN(Sales) AS Minimum_Sales,
    MAX(Sales) AS Maximum_Sales
FROM superstore_cleaned_data;

-- 5. Check minimum and maximum profit
SELECT
    MIN(Profit) AS Minimum_Profit,
    MAX(Profit) AS Maximum_Profit
FROM superstore_cleaned_data;
