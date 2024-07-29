import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load preprocessed data
ecom_data_normalized = pd.read_csv('ecom_data_normalized.csv')
mall_data_normalized = pd.read_csv('mall_data_normalized.csv')

def visualize_data(df, column, title):
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], kde=True, bins=30)
    plt.title(title)
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()

# Visualize e-commerce data
visualize_data(ecom_data_normalized, 'Orders', 'Distribution of Orders in E-Commerce Data')
visualize_data(ecom_data_normalized, 'Jordan', 'Distribution of Jordan Purchases in E-Commerce Data')

# Visualize mall data
visualize_data(mall_data_normalized, 'Age', 'Distribution of Age in Mall Customers Data')
visualize_data(mall_data_normalized, 'Annual Income (k$)', 'Distribution of Annual Income in Mall Customers Data')
visualize_data(mall_data_normalized, 'Spending Score (1-100)', 'Distribution of Spending Score in Mall Customers Data')
