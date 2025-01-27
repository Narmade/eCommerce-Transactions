
# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load the datasets
customers = pd.read_csv('Customers.csv')
transactions = pd.read_csv('Transactions.csv')

# Merge datasets to create a comprehensive customer profile
customer_data = transactions.merge(customers, on='CustomerID')

# Feature Engineering: Create features for clustering
customer_features = customer_data.groupby('CustomerID').agg(
    TotalSpending=('TotalValue', 'sum'),
    AverageTransactionValue=('TotalValue', 'mean'),
    PurchaseFrequency=('TransactionID', 'count')
).reset_index()

# Normalize the features
scaler = StandardScaler()
features_scaled = scaler.fit_transform(customer_features[['TotalSpending', 'AverageTransactionValue', 'PurchaseFrequency']])

# K-Means Clustering
kmeans = KMeans(n_clusters=4, random_state=42)  # Choose 4 clusters
customer_features['Cluster'] = kmeans.fit_predict(features_scaled)

# Visualize the clusters
plt.figure(figsize=(10, 6))
plt.scatter(customer_features['TotalSpending'], customer_features['AverageTransactionValue'], c=customer_features['Cluster'], cmap='viridis', s=100)
plt.title('Customer Segmentation')
plt.xlabel('Total Spending')
plt.ylabel('Average Transaction Value')
plt.colorbar(label='Cluster')
plt.show()

# Save the clustering results
customer_features.to_csv('Customer_Segmentation_Results.csv', index=False)
print("Customer segmentation results saved to 'Customer_Segmentation_Results.csv'.")