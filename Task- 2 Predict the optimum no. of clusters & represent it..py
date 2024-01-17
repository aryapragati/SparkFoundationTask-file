#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Load the data from the CSV file
df = pd.read_csv("Iris.csv")

# Extracting features for clustering
features = df.iloc[:, 1:5]

# Standardize the features
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Applying K-means with different numbers of clusters
inertia = []
for n_clusters in range(1, 11):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(features_scaled)
    inertia.append(kmeans.inertia_)

# Plotting the Elbow Method to find the optimum number of clusters
plt.plot(range(1, 11), inertia, marker='o')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia (Within-cluster Sum of Squares)')
plt.title('Elbow Method for Optimal Clusters')
plt.show()


# In[3]:


# Assuming the optimal number of clusters is 3
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(features_scaled)

# Add cluster labels to the original DataFrame
df['Cluster'] = kmeans.labels_

# Reduce dimensionality for visualization (optional)
pca = PCA(n_components=2)
features_pca = pca.fit_transform(features_scaled)

# Plotting the clusters
plt.scatter(features_pca[:, 0], features_pca[:, 1], c=df['Cluster'], cmap='viridis', edgecolor='k', s=50)
plt.title('K-means Clustering (Optimal: 3 clusters)')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()


# In[ ]:




