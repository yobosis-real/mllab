# Import libraries
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_california_housing

data = fetch_california_housing(as_frame=True)

df = data.frame

corr = df.corr()

print(corr)

plt.figure(figsize=(10,8))

sns.heatmap(corr, annot=True)

plt.title("Correlation Heatmap")

plt.show()

sns.pairplot(df[['MedInc', 'HouseAge', 'AveRooms']])

plt.show()
