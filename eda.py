
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

abalones=pd.read_csv('/Users/Admin/Downloads/abalone (1).csv')
# print(abalones)

# abalones.info()

# print(abalones.duplicated().sum())

# to get abalone's age - add 1.5 to rings

abalones['Rings'] =  abalones['Rings'] + 1.5
# print(abalones.head(5))

print(abalones.isnull().sum().sum())
# 248 NaN values
# check if Nan values are in categorical column:
# print(abalones.isna().any())

#fill nan values with mean
mean_diameter = abalones['Diameter'].mean()
mean_ww = abalones['Whole weight'].mean()
mean_sw = abalones['Shell weight'].mean()
values = {'Diameter': mean_diameter, 'Whole weight': mean_ww, 'Shell weight': mean_sw}
abalones.fillna(value=values, inplace=True)

# print(abalones.isna().any())

plt.figure(figsize=(4,3))

plt.hist(abalones.Rings)
plt.show()