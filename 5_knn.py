
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

X = np.random.rand(100,1)

y = []

for i in range(50):

    if X[i] <= 0.5:
        y.append(1)

    else:
        y.append(2)

X_train = X[:50]
y_train = y

X_test = X[50:]

knn = KNeighborsClassifier(n_neighbors=3)

knn.fit(X_train, y_train)

pred = knn.predict(X_test)

print(pred)
