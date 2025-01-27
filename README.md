# eCommerce-Transactions

## Project Description
This project focuses on analyzing an eCommerce transactions dataset to perform customer segmentation through clustering techniques. The primary objective is to categorize customers based on their purchasing behaviors, which can facilitate targeted marketing efforts.

## Dataset Information
The analysis utilizes three key datasets:
- **Customers.csv**: This file contains essential customer details, including unique IDs, names, regions, and signup dates.
- **Products.csv**: This dataset provides information about products, including their IDs, names, categories, and prices.
- **Transactions.csv**: This file records transaction details, such as transaction IDs, customer IDs, product IDs, transaction dates, quantities, and total values.

## Completed Tasks
1. **Exploratory Data Analysis (EDA)**:
   - Conducted a thorough EDA to gain insights into the dataset and identify significant trends.
   - Created visualizations to illustrate data patterns and relationships.

2. **Lookalike Model Development**:
   - Developed a lookalike model to suggest similar customers based on their profiles and transaction histories.
   - Employed cosine similarity to determine customer similarities.

3. **Customer Segmentation**:
   - Implemented K-Means clustering to segment customers according to their purchasing behaviors.
   - Evaluated the clustering results using metrics such as the Davies-Bouldin Index and Silhouette Score.

## Requirements
To execute the code, ensure you have the following Python libraries installed:
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

