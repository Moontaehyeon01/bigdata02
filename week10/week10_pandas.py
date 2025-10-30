import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

german = pd.read_csv('german.csv')
# print(german.info())
# print(german.tail())
# print(german.head())
# print(german['Age'].describe())
print(pd.cut(german['Age'], bins=8).reset_index().groupby('Age').count())