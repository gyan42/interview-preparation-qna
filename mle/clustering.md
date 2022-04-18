# Clustering

## KMeans

**How to choose K?**
    - Elbow Curve Method
        - Find average distance from centroid for each cluster for given K value and see where the distance falls and use that as the value
    - Silhouette score : from sklearn.metrics import silhouette_score [-1(bad) to 1 (good)]
        - The silhouette value measures how similar a point is to its own cluster (cohesion) compared to other clusters (separation).
```python
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans
sil = []
kmax = 10

# dissimilarity would not be defined for a single cluster, thus, minimum number of clusters should be 2
for k in range(2, kmax+1):
  kmeans = KMeans(n_clusters = k).fit(x)
  labels = kmeans.labels_
  sil.append(silhouette_score(x, labels, metric = 'euclidean'))
```
- https://www.analyticsvidhya.com/blog/2021/05/k-mean-getting-the-optimal-number-of-clusters/
- 
