"""
Project: Sales Analysis Dashboard
Dataset: Sample - Superstore
Author: Deena

Description:
This project analyzes sales, profit, customers, products,
regions, and overall business performance using Python.
"""

# ==========================
# Import Libraries
# ==========================

import pandas as pd
import matplotlib.pyplot as plt
import os

# ==========================
# Current Working Directory
# ==========================

print("Current Working Directory:")
print(os.getcwd())

# ==========================
# Load Dataset
# ==========================

df = pd.read_excel("dataset/Sample - Superstore.xlsx")

# ==========================
# Dataset Information
# ==========================

print("\n===== Dataset Shape =====")
print(df.shape)

print("\n===== Column Names =====")
print(df.columns)

print("\n===== Dataset Information =====")
df.info()

# ==========================
# Data Quality Check
# ==========================

print("\n===== Missing Values =====")
print(df.isnull().sum())

print("\n===== Duplicate Rows =====")
print(df.duplicated().sum())

# ==========================
# Convert Date Columns
# ==========================

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

print("\n===== Updated Data Types =====")
print(df[["Order Date", "Ship Date"]].dtypes)

# ==========================
# Create Date Features
# ==========================

df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month_name()
df["Month Number"] = df["Order Date"].dt.month
df["Quarter"] = df["Order Date"].dt.quarter

print("\n===== Date Features =====")
print(df[["Order Date", "Year", "Month", "Month Number", "Quarter"]].head())

# ==========================
# Key Performance Indicators (KPIs)
# ==========================

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
total_customers = df["Customer ID"].nunique()
total_products = df["Product ID"].nunique()

print("\n===== Key Performance Indicators =====")
print(f"Total Sales      : ${total_sales:,.2f}")
print(f"Total Profit     : ${total_profit:,.2f}")
print(f"Total Orders     : {total_orders}")
print(f"Total Customers  : {total_customers}")
print(f"Total Products   : {total_products}")

# ==========================
# Sales by Region
# ==========================

sales_by_region = (
    df.groupby("Region")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

print("\n===== Sales by Region =====")
print(sales_by_region)

# ==========================
# Sales by Region Chart
# ==========================

plt.figure(figsize=(8, 5))

sales_by_region.plot(kind="bar")

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")

plt.tight_layout()

plt.savefig("charts/region_sales.png")

plt.show()
plt.close()

# ==========================
# Profit by Region
# ==========================

profit_by_region = (
    df.groupby("Region")["Profit"]
      .sum()
      .sort_values(ascending=False)
)

print("\n===== Profit by Region =====")
print(profit_by_region)

# ==========================
# Profit by Region Chart
# ==========================

plt.figure(figsize=(8, 5))

profit_by_region.plot(kind="bar")

plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Profit")

plt.tight_layout()

plt.savefig("charts/region_profit.png")

plt.show()
plt.close()

# ==========================
# Sales by Category
# ==========================

sales_by_category = (
    df.groupby("Category")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

print("\n===== Sales by Category =====")
print(sales_by_category)

# ==========================
# Sales by Category Chart
# ==========================

plt.figure(figsize=(8, 5))

sales_by_category.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.tight_layout()

plt.savefig("charts/category_sales.png")

plt.show()
plt.close()

# ==========================
# Profit by Category
# ==========================

profit_by_category = (
    df.groupby("Category")["Profit"]
      .sum()
      .sort_values(ascending=False)
)

print("\n===== Profit by Category =====")
print(profit_by_category)

# ==========================
# Profit by Category Chart
# ==========================

plt.figure(figsize=(8, 5))

profit_by_category.plot(kind="bar")

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")

plt.tight_layout()

plt.savefig("charts/category_profit.png")

plt.show()
plt.close()

# ==========================
# Top 10 Customers by Sales
# ==========================

top_customers = (
    df.groupby("Customer Name")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print("\n===== Top 10 Customers by Sales =====")
print(top_customers)

# ==========================
# Top 10 Customers by Sales Chart
# ==========================

plt.figure(figsize=(10, 6))

top_customers.plot(kind="bar")

plt.title("Top 10 Customers by Sales")
plt.xlabel("Customer Name")
plt.ylabel("Sales")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.savefig("charts/top10_customers_sales.png")

plt.show()
plt.close()

# ==========================
# Top 10 Customers by Profit
# ==========================

top_customers_profit = (
    df.groupby("Customer Name")["Profit"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print("\n===== Top 10 Customers by Profit =====")
print(top_customers_profit)

# ==========================
# Top 10 Customers by Profit Chart
# ==========================

plt.figure(figsize=(10, 6))

top_customers_profit.plot(kind="bar")

plt.title("Top 10 Customers by Profit")
plt.xlabel("Customer Name")
plt.ylabel("Profit")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.savefig("charts/top10_customers_profit.png")

plt.show()
plt.close()

# ==========================
# Top 10 Products by Sales
# ==========================

top_products_sales = (
    df.groupby("Product Name")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print("\n===== Top 10 Products by Sales =====")
print(top_products_sales)

# ==========================
# Top 10 Products by Sales Chart
# ==========================

plt.figure(figsize=(12, 6))

top_products_sales.plot(kind="bar")

plt.title("Top 10 Products by Sales")
plt.xlabel("Product Name")
plt.ylabel("Sales")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.savefig("charts/top10_products_sales.png")

plt.show()
plt.close()

# ==========================
# Top 10 Products by Profit
# ==========================

top_products_profit = (
    df.groupby("Product Name")["Profit"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print("\n===== Top 10 Products by Profit =====")
print(top_products_profit)

# ==========================
# Top 10 Products by Profit Chart
# ==========================

plt.figure(figsize=(12, 6))

top_products_profit.plot(kind="bar")

plt.title("Top 10 Products by Profit")
plt.xlabel("Product Name")
plt.ylabel("Profit")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.savefig("charts/top10_products_profit.png")

plt.show()
plt.close()

# ==========================
# Monthly Sales Trend
# ==========================

monthly_sales = (
    df.groupby(["Year", "Month Number", "Month"])["Sales"]
      .sum()
      .reset_index()
      .sort_values(["Year", "Month Number"])
)

print("\n===== Monthly Sales Trend =====")
print(monthly_sales)

# ==========================
# Monthly Sales Trend Chart
# ==========================

plt.figure(figsize=(12, 6))

plt.plot(
    monthly_sales.index,
    monthly_sales["Sales"],
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.xticks(
    monthly_sales.index,
    monthly_sales["Month"] + " " + monthly_sales["Year"].astype(str),
    rotation=45,
    ha="right"
)

plt.tight_layout()

plt.savefig("charts/monthly_sales_trend.png")

plt.show()
plt.close()

# ==========================
# Monthly Profit Trend
# ==========================

monthly_profit = (
    df.groupby(["Year", "Month Number", "Month"])["Profit"]
      .sum()
      .reset_index()
      .sort_values(["Year", "Month Number"])
)

print("\n===== Monthly Profit Trend =====")
print(monthly_profit)

# ==========================
# Monthly Profit Trend Chart
# ==========================

plt.figure(figsize=(12, 6))

plt.plot(
    monthly_profit.index,
    monthly_profit["Profit"],
    marker="o"
)

plt.title("Monthly Profit Trend")
plt.xlabel("Month")
plt.ylabel("Profit")

plt.xticks(
    monthly_profit.index,
    monthly_profit["Month"] + " " + monthly_profit["Year"].astype(str),
    rotation=45,
    ha="right"
)

plt.tight_layout()

plt.savefig("charts/monthly_profit_trend.png")

plt.show()
plt.close()

# ==========================
# Top 10 States by Sales
# ==========================

top_states_sales = (
    df.groupby("State")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print("\n===== Top 10 States by Sales =====")
print(top_states_sales)

# ==========================
# Top 10 States by Sales Chart
# ==========================

plt.figure(figsize=(12, 6))

top_states_sales.plot(kind="bar")

plt.title("Top 10 States by Sales")
plt.xlabel("State")
plt.ylabel("Sales")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.savefig("charts/top10_states_sales.png")

plt.show()
plt.close()

# ==========================
# Top 10 States by Profit
# ==========================

top_states_profit = (
    df.groupby("State")["Profit"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print("\n===== Top 10 States by Profit =====")
print(top_states_profit)

# ==========================
# Top 10 States by Profit Chart
# ==========================

plt.figure(figsize=(12, 6))

top_states_profit.plot(kind="bar")

plt.title("Top 10 States by Profit")
plt.xlabel("State")
plt.ylabel("Profit")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.savefig("charts/top10_states_profit.png")

plt.show()
plt.close()

# ==========================
# Top 10 Cities by Sales
# ==========================

top_cities_sales = (
    df.groupby("City")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print("\n===== Top 10 Cities by Sales =====")
print(top_cities_sales)

# ==========================
# Top 10 Cities by Sales Chart
# ==========================

plt.figure(figsize=(12, 6))

top_cities_sales.plot(kind="bar")

plt.title("Top 10 Cities by Sales")
plt.xlabel("City")
plt.ylabel("Sales")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.savefig("charts/top10_cities_sales.png")

plt.show()
plt.close()

# ==========================
# Top 10 Cities by Profit
# ==========================

top_cities_profit = (
    df.groupby("City")["Profit"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print("\n===== Top 10 Cities by Profit =====")
print(top_cities_profit)

# ==========================
# Top 10 Cities by Profit Chart
# ==========================

plt.figure(figsize=(12, 6))

top_cities_profit.plot(kind="bar")

plt.title("Top 10 Cities by Profit")
plt.xlabel("City")
plt.ylabel("Profit")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.savefig("charts/top10_cities_profit.png")

plt.show()
plt.close()

# ==========================
# Sales by Segment
# ==========================

sales_by_segment = (
    df.groupby("Segment")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

print("\n===== Sales by Segment =====")
print(sales_by_segment)

# ==========================
# Sales by Segment Chart
# ==========================

plt.figure(figsize=(8, 5))

sales_by_segment.plot(kind="bar")

plt.title("Sales by Segment")
plt.xlabel("Segment")
plt.ylabel("Sales")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig("charts/sales_by_segment.png")

plt.show()
plt.close()

# ==========================
# Profit by Segment
# ==========================

profit_by_segment = (
    df.groupby("Segment")["Profit"]
      .sum()
      .sort_values(ascending=False)
)

print("\n===== Profit by Segment =====")
print(profit_by_segment)

# ==========================
# Profit by Segment Chart
# ==========================

plt.figure(figsize=(8, 5))

profit_by_segment.plot(kind="bar")

plt.title("Profit by Segment")
plt.xlabel("Segment")
plt.ylabel("Profit")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig("charts/profit_by_segment.png")

plt.show()
plt.close()

# ==========================
# Customer Count by Segment
# ==========================

customer_count_segment = (
    df.groupby("Segment")["Customer ID"]
      .nunique()
      .sort_values(ascending=False)
)

print("\n===== Customer Count by Segment =====")
print(customer_count_segment)

# ==========================
# Customer Count by Segment Chart
# ==========================

plt.figure(figsize=(8, 5))

customer_count_segment.plot(kind="bar")

plt.title("Customer Count by Segment")
plt.xlabel("Segment")
plt.ylabel("Number of Customers")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig("charts/customer_count_segment.png")

plt.show()
plt.close()

# ==========================
# Sales by Ship Mode
# ==========================

sales_by_ship_mode = (
    df.groupby("Ship Mode")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

print("\n===== Sales by Ship Mode =====")
print(sales_by_ship_mode)

# ==========================
# Sales by Ship Mode Chart
# ==========================

plt.figure(figsize=(8, 5))

sales_by_ship_mode.plot(kind="bar")

plt.title("Sales by Ship Mode")
plt.xlabel("Ship Mode")
plt.ylabel("Sales")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig("charts/sales_by_ship_mode.png")

plt.show()
plt.close()

# ==========================
# Profit by Ship Mode
# ==========================

profit_by_ship_mode = (
    df.groupby("Ship Mode")["Profit"]
      .sum()
      .sort_values(ascending=False)
)

print("\n===== Profit by Ship Mode =====")
print(profit_by_ship_mode)

# ==========================
# Profit by Ship Mode Chart
# ==========================

plt.figure(figsize=(8, 5))

profit_by_ship_mode.plot(kind="bar")

plt.title("Profit by Ship Mode")
plt.xlabel("Ship Mode")
plt.ylabel("Profit")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig("charts/profit_by_ship_mode.png")

plt.show()
plt.close()

# ==========================
# Orders by Ship Mode
# ==========================

orders_by_ship_mode = (
    df.groupby("Ship Mode")["Order ID"]
      .nunique()
      .sort_values(ascending=False)
)

print("\n===== Orders by Ship Mode =====")
print(orders_by_ship_mode)

# ==========================
# Orders by Ship Mode Chart
# ==========================

plt.figure(figsize=(8,5))

orders_by_ship_mode.plot(kind="bar")

plt.title("Orders by Ship Mode")
plt.xlabel("Ship Mode")
plt.ylabel("Number of Orders")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig("charts/orders_by_ship_mode.png")

plt.show()
plt.close()

# ==========================
# Average Shipping Time
# ==========================

df["Shipping Days"] = (
    df["Ship Date"] - df["Order Date"]
).dt.days

shipping_time = (
    df.groupby("Ship Mode")["Shipping Days"]
      .mean()
      .sort_values(ascending=False)
)

print("\n===== Average Shipping Time =====")
print(shipping_time)

# ==========================
# Average Shipping Time Chart
# ==========================

plt.figure(figsize=(8,5))

shipping_time.plot(kind="bar")

plt.title("Average Shipping Time")
plt.xlabel("Ship Mode")
plt.ylabel("Average Days")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig("charts/average_shipping_time.png")

plt.show()
plt.close()

# ==========================
# Average Discount by Category
# ==========================

discount_category = (
    df.groupby("Category")["Discount"]
      .mean()
      .sort_values(ascending=False)
)

print("\n===== Average Discount by Category =====")
print(discount_category)

# ==========================
# Average Discount by Category Chart
# ==========================

plt.figure(figsize=(8,5))

discount_category.plot(kind="bar")

plt.title("Average Discount by Category")
plt.xlabel("Category")
plt.ylabel("Average Discount")

plt.tight_layout()

plt.savefig("charts/discount_by_category.png")

plt.show()
plt.close()

# ==========================
# Discount vs Profit
# ==========================

plt.figure(figsize=(8,6))

plt.scatter(
    df["Discount"],
    df["Profit"]
)

plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")

plt.tight_layout()

plt.savefig("charts/discount_vs_profit.png")

plt.show()
plt.close()

# ==========================
# Discount vs Sales
# ==========================

plt.figure(figsize=(8,6))

plt.scatter(
    df["Discount"],
    df["Sales"]
)

plt.title("Discount vs Sales")
plt.xlabel("Discount")
plt.ylabel("Sales")

plt.tight_layout()

plt.savefig("charts/discount_vs_sales.png")

plt.show()
plt.close()

# ==========================
# Top 10 Sub-Categories by Sales
# ==========================

top_subcategory_sales = (
    df.groupby("Sub-Category")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print("\n===== Top 10 Sub-Categories by Sales =====")
print(top_subcategory_sales)

# ==========================
# Top 10 Sub-Categories by Sales Chart
# ==========================

plt.figure(figsize=(12,6))

top_subcategory_sales.plot(kind="bar")

plt.title("Top 10 Sub-Categories by Sales")
plt.xlabel("Sub-Category")
plt.ylabel("Sales")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.savefig("charts/top10_subcategory_sales.png")

plt.show()
plt.close()

# ==========================
# Top 10 Sub-Categories by Profit
# ==========================

top_subcategory_profit = (
    df.groupby("Sub-Category")["Profit"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print("\n===== Top 10 Sub-Categories by Profit =====")
print(top_subcategory_profit)

# ==========================
# Top 10 Sub-Categories by Profit Chart
# ==========================

plt.figure(figsize=(12,6))

top_subcategory_profit.plot(kind="bar")

plt.title("Top 10 Sub-Categories by Profit")
plt.xlabel("Sub-Category")
plt.ylabel("Profit")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.savefig("charts/top10_subcategory_profit.png")

plt.show()
plt.close()

# ==========================
# Bottom 10 States by Profit
# ==========================

bottom_states_profit = (
    df.groupby("State")["Profit"]
      .sum()
      .sort_values(ascending=True)
      .head(10)
)

print("\n===== Bottom 10 States by Profit =====")
print(bottom_states_profit)

# ==========================
# Bottom 10 States by Profit Chart
# ==========================

plt.figure(figsize=(10, 6))

bottom_states_profit.plot(kind="bar", color="tomato")

plt.title("Bottom 10 States by Profit")
plt.xlabel("State")
plt.ylabel("Profit")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.savefig("charts/bottom10_states_profit.png")

plt.show()
plt.close()

# ==========================
# Top 10 Products by Quantity Sold
# ==========================

top_products_quantity = (
    df.groupby("Product Name")["Quantity"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print("\n===== Top 10 Products by Quantity Sold =====")
print(top_products_quantity)

# ==========================
# Top 10 Products by Quantity Chart
# ==========================

plt.figure(figsize=(12,6))

top_products_quantity.plot(kind="bar")

plt.title("Top 10 Products by Quantity Sold")
plt.xlabel("Product Name")
plt.ylabel("Quantity Sold")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.savefig("charts/top10_products_quantity.png")

plt.show()
plt.close()

# ==========================
# Quantity Sold by Category
# ==========================

quantity_by_category = (
    df.groupby("Category")["Quantity"]
      .sum()
      .sort_values(ascending=False)
)

print("\n===== Quantity Sold by Category =====")
print(quantity_by_category)

# ==========================
# Quantity by Category Chart
# ==========================

plt.figure(figsize=(8,5))

quantity_by_category.plot(kind="bar")

plt.title("Quantity Sold by Category")
plt.xlabel("Category")
plt.ylabel("Quantity")

plt.tight_layout()

plt.savefig("charts/quantity_by_category.png")

plt.show()
plt.close()

# ==========================
# Correlation Matrix
# ==========================

correlation = df[["Sales", "Profit", "Quantity", "Discount"]].corr()

print("\n===== Correlation Matrix =====")
print(correlation)

# ==========================
# Correlation Heatmap
# ==========================

plt.figure(figsize=(6,5))

plt.imshow(correlation, cmap="coolwarm")

plt.colorbar()

plt.xticks(range(len(correlation.columns)), correlation.columns)

plt.yticks(range(len(correlation.columns)), correlation.columns)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig("charts/correlation_heatmap.png")

plt.show()
plt.close()

# ==========================
# Sales vs Profit
# ==========================

plt.figure(figsize=(8,6))

plt.scatter(df["Sales"], df["Profit"])

plt.title("Sales vs Profit")

plt.xlabel("Sales")

plt.ylabel("Profit")

plt.tight_layout()

plt.savefig("charts/sales_vs_profit.png")

plt.show()
plt.close()

# ==========================
# Export Clean Dataset
# ==========================

df.to_csv("reports/clean_superstore_data.csv", index=False)


# ==========================
# KPI Summary
# ==========================

kpi_summary = pd.DataFrame({
    "Metric": [
        "Total Sales",
        "Total Profit",
        "Total Orders",
        "Total Customers",
        "Total Products"
    ],
    "Value": [
        total_sales,
        total_profit,
        total_orders,
        total_customers,
        total_products
    ]
})

print(kpi_summary)

kpi_summary.to_csv("reports/kpi_summary.csv", index=False)

print("\nKPI Summary exported successfully!")

# ==========================
# Export Correlation Matrix
# ==========================

correlation.to_csv("reports/correlation_matrix.csv")


# ==========================
# Export Excel Report
# ==========================

with pd.ExcelWriter("reports/sales_analysis_report.xlsx") as writer:

    kpi_summary.to_excel(
        writer,
        sheet_name="KPIs",
        index=False
    )

    monthly_sales.to_excel(
        writer,
        sheet_name="Monthly Sales",
        index=False
    )

    monthly_profit.to_excel(
        writer,
        sheet_name="Monthly Profit",
        index=False
    )

    correlation.to_excel(
        writer,
        sheet_name="Correlation"
    )

# ==========================
# Business Insights
# ==========================

print("\n" + "=" * 50)
print("BUSINESS INSIGHTS")
print("=" * 50)

print(f"Highest Sales Region       : {sales_by_region.idxmax()}")
print(f"Highest Profit Region      : {profit_by_region.idxmax()}")

print(f"Highest Sales Category     : {sales_by_category.idxmax()}")
print(f"Highest Profit Category    : {profit_by_category.idxmax()}")

print(f"Top Customer (Sales)       : {top_customers.idxmax()}")
print(f"Top Customer (Profit)      : {top_customers_profit.idxmax()}")

print(f"Top Product (Sales)        : {top_products_sales.idxmax()}")
print(f"Top Product (Profit)       : {top_products_profit.idxmax()}")

print(f"Top State (Sales)          : {top_states_sales.idxmax()}")
print(f"Top State (Profit)         : {top_states_profit.idxmax()}")

print(f"Most Used Ship Mode        : {orders_by_ship_mode.idxmax()}")

print("=" * 50)