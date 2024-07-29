import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load clustered data
ecom_data_clustered = pd.read_csv('ecom_data_clustered.csv')
mall_data_clustered = pd.read_csv('mall_data_clustered.csv')

# Visualize clusters
def visualize_clusters(data, x_feature, y_feature, title):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=data[x_feature], y=data[y_feature], hue=data['Cluster'], palette='viridis')
    plt.title(title)
    plt.show()

# Visualize clusters for e-commerce data
visualize_clusters(ecom_data_clustered, 'Orders', 'Jordan', 'E-Commerce Customer Segments')

# Visualize clusters for mall data
visualize_clusters(mall_data_clustered, 'Annual Income (k$)', 'Spending Score (1-100)', 'Mall Customer Segments')
