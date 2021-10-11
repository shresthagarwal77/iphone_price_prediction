import pandas
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
data = pandas.read_csv('iphone_price.csv')
# plt.scatter(data['version'], data['price'])
# plt.show() #just to show chart
model = LinearRegression()
model.fit(data[['version']], data[['price']])
print(model.predict([[30]]))
