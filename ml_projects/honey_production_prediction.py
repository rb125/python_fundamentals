import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

df = pd.read_csv("https://content.codecademy.com/programs/data-science-path/linear_regression/honeyproduction.csv")

#Get a feel of the data
print(df.head())

#Group total production and year, our columns of interest 
prod_per_year = df.groupby(['year']).totalprod.mean().reset_index()

X = prod_per_year['year']
X = X.values.reshape(-1,1)
print(X)
y = prod_per_year['totalprod']

#Run linear regression to find best fit m and b values to predict total production values from known year of production values.
line_fit = LinearRegression()
line_fit.fit(X,y)
slope = line_fit.coef_
intercept = line_fit.intercept_
print("Slope : {slope}".format(slope = slope))
print("Intercept: {intercept}".format(intercept=intercept))
y_predict = line_fit.predict(X)

plt.scatter(X, y)
plt.plot(X, y_predict, 'r')
plt.show()
plt.clf()

#Now lets extend the year value to extrapolate our model and predict total production for a future year. Both, X and y values are now unknown. We built a model with known values for both X and y. We then predicted y values to test how accurate our prediction was for known year values. We finally use the same model to predict production value for a year in the future (which was not part of our test data.)
X_future = np.array(range(2013,2051))
#Before reshape
print(X_future)
X_future = X_future.reshape(-1,1)
#After reshape 
print(X_future)
future_predict = line_fit.predict(X_future)
plt.plot(X_future, future_predict)
plt.show()



