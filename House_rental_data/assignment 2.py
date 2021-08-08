# -*- coding: utf-8 -*-

#loading data
import pandas as pd
df=pd.read_csv("house_rental_data.csv.txt")

#splitting into x
x=df.iloc[:,2:8].values


#Clustering
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=6, init='k-means++',random_state=0)
kmeans.fit(x)
df['Clusters']=kmeans.labels_
sorted_df=df.sort_values(by=['Clusters'])


#within Cluster Sum_of_squares
wcss=[]
for k in range(1,11):
    km=KMeans(n_clusters = k,init="k-means++",random_state=0)
    km.fit(x)
    wcss_i=km.inertia_
    wcss.append(wcss_i)
    print(k,wcss_i)
    
#Elbow method
import matplotlib.pyplot as plt
plt.plot(range(1, 11), wcss)
plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.show()