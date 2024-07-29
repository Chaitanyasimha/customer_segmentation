import pandas as pd
from sklearn.metrics import silhouette_score

# Load clustered data
ecom_data_clustered = pd.read_csv('ecom_data_clustered.csv')
mall_data_clustered = pd.read_csv('mall_data_clustered.csv')

# Calculate and print the Silhouette Score
def calculate_silhouette_score(data, labels):
    score = silhouette_score(data, labels)
    print(f'Silhouette Score: {score}')

# Calculate silhouette score for e-commerce data
calculate_silhouette_score(ecom_data_clustered.drop(['Cust_ID', 'Cluster'], axis=1), ecom_data_clustered['Cluster'])

# Calculate silhouette score for mall data
calculate_silhouette_score(mall_data_clustered.drop(['CustomerID', 'Cluster'], axis=1), mall_data_clustered['Cluster'])
