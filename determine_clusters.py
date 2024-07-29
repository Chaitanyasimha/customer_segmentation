import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

# Load preprocessed data
ecom_data_normalized = pd.read_csv('ecom_data_normalized.csv')
mall_data_normalized = pd.read_csv('mall_data_normalized.csv')

# Find the optimal number of clusters using the Elbow Method
def find_optimal_clusters(data, max_k):
    iters = range(1, max_k + 1)
    sse = []
    for k in iters:
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(data)
        sse.append(kmeans.inertia_)
    plt.figure(figsize=(10, 6))
    plt.plot(iters, sse, marker='o')
    plt.xlabel('Number of clusters')
    plt.ylabel('SSE')
    plt.title('Elbow Method For Optimal k')
    plt.show()

# Find the optimal number of clusters using Silhouette Score
def find_optimal_clusters_silhouette(data, max_k):
    iters = range(2, max_k + 1)
    silhouettes = []
    for k in iters:
        kmeans = KMeans(n_clusters=k, random_state=42)
        labels = kmeans.fit_predict(data)
        silhouettes.append(silhouette_score(data, labels))
    plt.figure(figsize=(10, 6))
    plt.plot(iters, silhouettes, marker='o')
    plt.xlabel('Number of clusters')
    plt.ylabel('Silhouette Score')
    plt.title('Silhouette Score For Optimal k')
    plt.show()

# Determine the optimal number of clusters for e-commerce data
find_optimal_clusters(ecom_data_normalized.drop('Cust_ID', axis=1), 10)
find_optimal_clusters_silhouette(ecom_data_normalized.drop('Cust_ID', axis=1), 10)

# Determine the optimal number of clusters for mall data
find_optimal_clusters(mall_data_normalized.drop('CustomerID', axis=1), 10)
find_optimal_clusters_silhouette(mall_data_normalized.drop('CustomerID', axis=1), 10)
