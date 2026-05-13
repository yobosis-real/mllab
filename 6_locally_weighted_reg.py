import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X = np.array([[1],[2],[3],[4],[5]])

y = np.array([1,3,2,5,4])

model = LinearRegression()

model.fit(X, y)

pred = model.predict(X)

plt.scatter(X, y)

plt.plot(X, pred)

plt.title("Locally Weighted Regression")

plt.show()
