import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_california_housing

data = fetch_california_housing(as_frame=True)

df = data.frame

# Histogram
df.hist(figsize=(12,8), edgecolor='black')

plt.suptitle("Histogram")
plt.show()

# Boxplot
plt.figure(figsize=(12,5))

sns.boxplot(data=df)

plt.xticks(rotation=45)

plt.title("Boxplot")
plt.show()
