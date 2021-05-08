import csv
import matplotlib.pyplot as plt

import pandas as pd
d1 = pd.read_csv("C:\\Users\\LENOVO\\OneDrive\\Documents\\test.csv")
print(d1)


print(d1.shape)

print(d1.describe())

print(d1.head(5))

print(d1.tail(5))