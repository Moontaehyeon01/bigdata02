import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor

df = pd.read_csv('life_satisfaction.csv')
# print(len(df))
# print(df.tail(3))
# print(df.info())
# print(df.describe())

X = df[["GDP per capita (USD)"]].values
y = df[["Life satisfaction"]].values

model1 = LinearRegression()
model2 = KNeighborsRegressor(3)

model1.fit(X, y)
model2.fit(X, y)

new_instance = [[31721.30]] #2020 South Korea GDP per capita (USD)
print(f"Life Satisfaction(Linear Regression) : {model1.predict(new_instance)[0][0]}:.1f)")
print(f"Life Satisfaction(KNeighbors Regressor) : {model2.predict(new_instance)[0][0]}")

# print(y)

# df.plot(kind='scatter', grid=True,
#              x="GDP per capita (USD)", y="Life satisfaction")
# plt.axis([23_500, 62_500, 4, 9])
# plt.show()