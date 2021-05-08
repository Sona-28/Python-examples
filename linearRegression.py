import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
d=(1,2),(2,5),(3,9),(4,12),(5,21),(6,35)
print(d)
x=d
y=d
from sklearn.linear_model import LinearRegression
lin=LinearRegression()
lin.fit(x,y)
plt.scatter(x, y, color='blue')
plt.plot(x,lin.predict(x),color='red')
plt.title('Linear Regression')
plt.xlabel("Temparature")
plt.ylabel("Pressure")
plt.show()