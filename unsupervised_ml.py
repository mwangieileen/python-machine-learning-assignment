#importing libraries
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np

#preparing customer data:x=customers and their spending
customers=[
    [1000,2],
    [1500,3],
    [2000,2],
    [5000,6],
    [6000,7],
    [5500,5],
    [12000,12],
    [15000,14],
    [13000,11],
    [3000,4]
]

#scaling
scaler=StandardScaler()
scaled_customers=scaler.fit_transform(customers)

#creating model
model=KMeans(n_clusters=3,random_state=42,n_init=10)

#training model
model.fit(scaled_customers)

#displaying clusters assigned to each customer as per example output-mantains initial cluster labels ie 0-2 not 1-3
groups=model.predict(scaled_customers)

for i in range(len(customers)):
    print("Customer",i+1,"belongs to Cluster",groups[i])

#displaying clusters as human readable:
groups=model.predict(scaled_customers)

for i in range(len(customers)):
    print("Customer",i+1,"belongs to Cluster",groups[i]+1)

#visualization on matplot
customers=np.array(customers)
plt.scatter(customers[:,0],customers[:,1],c=groups,cmap="rainbow")
plt.xlabel("Monthly Spending (KES)")
plt.ylabel("Monthly Visits")
plt.title("Customer Groups")
#show what group different colors represent on the legend
for i in set (groups):
    plt.scatter([],[],color=plt.cm.rainbow(i/max(set(groups))),label="Group "+str(i+1))
plt.legend()
plt.show()
