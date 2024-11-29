import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics.cluster import adjusted_mutual_info_score

data = pd.read_csv('/content/Iris.csv')
data.head()


numerical_features = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm'] 
X = data[numerical_features]

scalar = StandardScaler()
data_scaled = scalar.fit_transform(X) 
pd.DataFrame(data_scaled, columns=numerical_features) 

xtrain,xtest = train_test_split(data_scaled,test_size=0.25,random_state=42)
# inertias = []

# for  i in range(1, 20):
#   kmean = KMeans(n_clusters=i, random_state=42)
#   kmean.fit(data_scaled)
#   inertias.append(kmean.inertia_)

# plt.plot(range(1, 20), inertias, marker='o')
# plt.xlabel('Number of Clusters')
# plt.ylabel('Inertia')
# plt.title('Elbow Method')
# plt.show()


kmean = KMeans(3,init='k-means++')
kmean.fit(data_scaled)
pred = kmean.predict(data_scaled)
# labels = kmean.labels_
# adjusted_mutual_info_score(pred,labels)
frame = pd.DataFrame(data_scaled)

frame['cluster'] = pred
frame['cluster'].value_counts()
