# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Datasets
customers = pd.read_csv('Customers.csv')
products = pd.read_csv('Products.csv')
transactions = pd.read_csv('Transactions.csv')

# Data Overview
print("Customers Data:")
print(customers.head())
print(customers.info())

print("\nProducts Data:")
print(products.head())
print(products.info())

print("\nTransactions Data:")
print(transactions.head())
print(transactions.info())

# Check for missing values
print("\nMissing Values:")
print(customers.isnull().sum())
print(products.isnull().sum())
print(transactions.isnull().sum())

# Basic Data Visualization
# Total Sales by Region
sales_by_region = transactions.merge(customers, on='CustomerID').groupby('Region')['TotalValue'].sum().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(x='Region', y='TotalValue', data=sales_by_region)
plt.title('Total Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales (USD)')
plt.xticks(rotation=45)
plt.show()

# Distribution of Product Prices
plt.figure(figsize=(10, 6))
sns.histplot(products['Price'], bins=30, kde=True)
plt.title('Distribution of Product Prices')
plt.xlabel('Price (USD)')
plt.ylabel('Frequency')
plt.show()

# Total Transactions Over Time
transactions['TransactionDate'] = pd.to_datetime(transactions['TransactionDate'])
transactions.set_index('TransactionDate', inplace=True)
transactions.resample('M').size().plot(figsize=(12, 6))
plt.title('Total Transactions Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Transactions')
plt.show()

