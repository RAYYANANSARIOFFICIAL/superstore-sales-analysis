#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("All libraries imported successfully!")


# In[4]:


df = pd.read_csv("Superstore_Cleaned_Data.csv", encoding="utf-8-sig")

print("Dataset loaded successfully!")
print("Rows and Columns:", df.shape)

df.head()


# In[5]:


print("Dataset Information:")
df.info()

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nColumn Names:")
print(df.columns.tolist())


# In[6]:


df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)
df["Ship Date"] = pd.to_datetime(df["Ship Date"], dayfirst=True)

print("Date columns converted successfully!")

print(df[["Order Date", "Ship Date"]].dtypes)

df[["Order Date", "Ship Date"]].head()


# In[7]:


df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month
df["Month Name"] = df["Order Date"].dt.month_name()

print("New date columns created successfully!")

df[["Order Date", "Year", "Month", "Month Name"]].head()


# In[8]:


yearly_analysis = df.groupby("Year").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
).round(2)

print("Year-wise Sales and Profit Analysis:")
yearly_analysis


# In[9]:


region_analysis = df.groupby("Region").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
).round(2).sort_values(by="Total_Sales", ascending=False)

print("Region-wise Sales and Profit Analysis:")
region_analysis


# In[10]:


category_analysis = df.groupby("Category").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
).round(2).sort_values(by="Total_Sales", ascending=False)

print("Category-wise Sales and Profit Analysis:")
category_analysis


# In[12]:


plt.figure(figsize=(8, 5))

sns.barplot(
    x=category_analysis.index,
    y=category_analysis["Total_Sales"]
)

plt.title("Category-wise Sales Analysis")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()


# In[13]:


plt.figure(figsize=(8, 5))

sns.barplot(
    x=category_analysis.index,
    y=category_analysis["Total_Profit"]
)

plt.title("Category-wise Profit Analysis")
plt.xlabel("Category")
plt.ylabel("Total Profit")
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()


# In[14]:


monthly_analysis = df.groupby("Month").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
).round(2)

print("Month-wise Sales and Profit Analysis:")
monthly_analysis


# In[15]:


plt.figure(figsize=(10, 5))

plt.plot(
    monthly_analysis.index,
    monthly_analysis["Total_Sales"],
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(range(1, 13))
plt.grid(True)
plt.tight_layout()
plt.show()


# In[16]:


subcategory_analysis = df.groupby("Sub-Category").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
).round(2).sort_values(by="Total_Sales", ascending=False)

print("Sub-Category Sales and Profit Analysis:")
subcategory_analysis


# In[17]:


plt.figure(figsize=(12, 6))

sns.barplot(
    x=subcategory_analysis.index,
    y=subcategory_analysis["Total_Profit"]
)

plt.title("Sub-Category Profit Analysis")
plt.xlabel("Sub-Category")
plt.ylabel("Total Profit")
plt.xticks(rotation=45)
plt.axhline(0, color="black", linewidth=1)
plt.tight_layout()
plt.show()


# In[18]:


segment_analysis = df.groupby("Segment").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Total_Orders=("Order ID", "nunique")
).round(2).sort_values(by="Total_Sales", ascending=False)

print("Segment-wise Sales and Profit Analysis:")
segment_analysis


# In[19]:


plt.figure(figsize=(8, 5))

sns.barplot(
    x=segment_analysis.index,
    y=segment_analysis["Total_Sales"]
)

plt.title("Segment-wise Sales Analysis")
plt.xlabel("Customer Segment")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()


# In[20]:


shipmode_analysis = df.groupby("Ship Mode").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Total_Orders=("Order ID", "nunique")
).round(2).sort_values(by="Total_Sales", ascending=False)

print("Ship Mode Sales and Profit Analysis:")
shipmode_analysis


# In[21]:


plt.figure(figsize=(9, 5))

sns.barplot(
    x=shipmode_analysis.index,
    y=shipmode_analysis["Total_Sales"]
)

plt.title("Ship Mode-wise Sales Analysis")
plt.xlabel("Ship Mode")
plt.ylabel("Total Sales")
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()


# In[22]:


top_products = df.groupby("Product Name").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
).round(2).sort_values(
    by="Total_Sales", ascending=False
).head(10)

print("Top 10 Products by Sales:")
top_products


# In[23]:


plt.figure(figsize=(12, 6))

sns.barplot(
    x=top_products["Total_Sales"],
    y=top_products.index
)

plt.title("Top 10 Products by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Product Name")
plt.tight_layout()
plt.show()


# In[24]:


top_customers = df.groupby("Customer Name").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
).round(2).sort_values(
    by="Total_Sales", ascending=False
).head(10)

print("Top 10 Customers by Sales:")
top_customers


# In[25]:


plt.figure(figsize=(10, 6))

sns.barplot(
    x=top_customers["Total_Sales"],
    y=top_customers.index
)

plt.title("Top 10 Customers by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Customer Name")
plt.tight_layout()
plt.show()


# In[26]:


discount_analysis = df.groupby("Discount").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
).round(2)

print("Discount vs Profit Analysis:")
discount_analysis


# In[ ]:





# In[27]:


plt.figure(figsize=(9, 5))

plt.scatter(
    discount_analysis.index,
    discount_analysis["Total_Profit"],
    s=80
)

plt.title("Discount vs Total Profit")
plt.xlabel("Discount")
plt.ylabel("Total Profit")
plt.axhline(0, color="black")
plt.grid(True)
plt.tight_layout()
plt.show()


# In[28]:


correlation = df[[
    "Sales",
    "Profit",
    "Quantity",
    "Discount"
]].corr().round(2)

print("Correlation Analysis:")
correlation


# In[29]:


plt.figure(figsize=(8, 5))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5
)

plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()


# In[ ]:




