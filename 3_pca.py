import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA

iris = load_iris()

X = iris.data
y = iris.target

pca = PCA(n_components=2)

X_pca = pca.fit_transform(X)

print(X_pca)

plt.scatter(X_pca[:,0], X_pca[:,1], c=y)

plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")

plt.title("PCA of Iris Dataset")

plt.show()
