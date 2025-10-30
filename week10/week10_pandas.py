import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

wh = pd.read_csv('wh.csv')
# print(wh.head())
# print(wh.info())
print(wh.describe())

sns.scatterplot(x='Weight', y='Height', data=wh)
plt.show()