import numpy as nm
import matplotlib.pyplot as plt
import pandas as pd
dataset = pd.read_csv("C:\\Users\\LENOVO\\OneDrive\\Documents\\Mall_Customers.csv")
x = dataset.iloc[:,[3,4]].values
from sklearn.cluster import KMeans
wcss_list = []
for i in range(1,11):
    kmeans=KMeans(n_clusters=i,init="k-means++",random_state=42)
    kmeans.fit(x)
    wcss_list.append(kmeans.inertia_)
plt.plot(range(1,11),wcss_list)
plt.title("The Elbow Method")
plt.xlabel("No of Clusters(k)")
plt.ylabel("wcss_list")
plt.show()
kmeans=KMeans(n_clusters=5,init="k-means++",random_state=42)
y_predict=kmeans.fit_predict(x)
plt.scatter(x[y_predict==0,0],x[y_predict==0,1],s=100,c="blue",label='cluster1')
plt.scatter(x[y_predict==1,0],x[y_predict==1,1],s=100,c="magenta",label='cluster2')
plt.scatter(x[y_predict==2,0],x[y_predict==2,1],s=100,c="red",label='cluster3')
plt.scatter(x[y_predict==3,0],x[y_predict==3,1],s=100,c="green",label='cluster4')
plt.scatter(x[y_predict==4,0],x[y_predict==4,1],s=100,c="cyan",label='cluster5')
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=100,c="yellow",label="centroid")
plt.title("Cluster of Customers")
plt.xlabel("Annual Income")
plt.ylabel("Spending Score(1-100)")
plt.legend()
plt.show()