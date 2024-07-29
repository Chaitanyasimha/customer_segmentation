import pandas as pd
from sklearn.cluster import KMeans

# Load preprocessed data
ecom_data_normalized = pd.read_csv('ecom_data_normalized.csv')
mall_data_normalized = pd.read_csv('mall_data_normalized.csv')

# Apply K-Means clustering with the identified number of clusters
def apply_kmeans(data, n_clusters):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit_predict(data)
    return clusters, kmeans

# Assuming optimal clusters are found to be 5 for both datasets
optimal_clusters_ecom = 5
optimal_clusters_mall = 5

# Apply K-Means clustering
ecom_clusters, ecom_kmeans = apply_kmeans(ecom_data_normalized.drop('Cust_ID', axis=1), optimal_clusters_ecom)
mall_clusters, mall_kmeans = apply_kmeans(mall_data_normalized.drop('CustomerID', axis=1), optimal_clusters_mall)

# Add cluster labels to the data
ecom_data_normalized['Cluster'] = ecom_clusters
mall_data_normalized['Cluster'] = mall_clusters

# Save clustered data
ecom_data_normalized.to_csv('ecom_data_clustered.csv', index=False)
mall_data_normalized.to_csv('mall_data_clustered.csv', index=False)
