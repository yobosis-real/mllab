import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

X = np.array([[1],[2],[3],[4],[5]])

y = np.array([1,2,3,6,9])

lr = LinearRegression()

lr.fit(X, y)

poly = PolynomialFeatures(degree=2)

X_poly = poly.fit_transform(X)

pr = LinearRegression()

pr.fit(X_poly, y)

y1 = lr.predict(X)

y2 = pr.predict(X_poly)

plt.scatter(X, y)

plt.plot(X, y1)

plt.plot(X, y2)

plt.title("Linear and Polynomial Regression")

plt.show()
