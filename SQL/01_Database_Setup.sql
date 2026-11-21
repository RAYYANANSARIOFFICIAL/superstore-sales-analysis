
-- ==========================================
-- Project: Superstore Sales Analysis
-- Database Setup
-- ==========================================

CREATE DATABASE IF NOT EXISTS superstore_analysis;

USE superstore_analysis;

-- View available tables
SHOW TABLES;

-- Check total records
SELECT COUNT(*) AS Total_Records
FROM superstore_cleaned_data;
