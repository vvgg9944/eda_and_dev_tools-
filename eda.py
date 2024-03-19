
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

abalones=pd.read_csv('/Users/Admin/Downloads/abalone (1).csv')
# print(abalones)

# to get abalone's age - add 1.5 to rings

abalones['Rings'] =  abalones['Rings'] + 1.5

# print(abalones.shape)
# shape of the dataset is 4178 rows\9 columns

# print(abalones.isnull().sum().sum())
# 248 NaN values
# check if Nan values are in categorical column:
# print(abalones.isna().any())
#fill nan values with mean
mean_diameter = abalones['Diameter'].mean()
mean_ww = abalones['Whole weight'].mean()
mean_sw = abalones['Shell weight'].mean()
values = {'Diameter': mean_diameter, 'Whole weight': mean_ww, 'Shell weight': mean_sw}
abalones.fillna(value=values, inplace=True)


plt.figure(figsize=(4,3))

plt.hist(abalones.Rings)
# plt.show()

# correlation

from ydata_profiling import ProfileReport

# print(abalones.shape)

from matplotlib import pyplot as plt
import seaborn as sns

from eda import abalones

print(abalones.columns)

# for c in abalones.columns:
#     plt.figure(figsize=(4, 3))
#     plt.title(c)
#     plt.hist(abalones[c])
#     plt.show()

# sex - what is f?; length, diameterнемного смещено вправо, height - log normal, whole, shuked, viscera, shell  weight skewed right
# rings almost normal

# for c in abalones.columns:
#     plt.figure(figsize=(4, 3))
#     plt.title(c)
#     plt.scatter(abalones[c], abalones.Rings)
#     plt.show()
# # all weights are not linear
#

# abalones_1 = abalones.drop(['Sex'], axis=1)
# corr = abalones_1.corr()
#
# sns.heatmap(corr, cmap="Blues", annot=True)
# plt.show()

# most correlated - diameter-length, whole-shucked, rings is more correlated with shell weight

# only one categorical feature - sex

# print(abalones.loc[abalones['Sex'] == 'f'])

# print(abalones.groupby("Sex")["Shell weight"].mean())
# for i in abalones["Sex"].unique():
#     print(abalones[])

# F    0.301320
# I    0.129950
# M    0.279464
# f    0.251488
# change f with M by shell weight

abalones.replace('f', 'M', inplace=True)
# print(abalones['Sex'].unique())

# ANOVA

from scipy.stats import f_oneway

CategoryGroupLists = abalones.groupby('Sex')['Rings'].apply(list)
AnovaResults = f_oneway(*CategoryGroupLists)
print('P-Value for Anova is: ', AnovaResults[1])

if AnovaResults[1] >= 0.05:
    print('Features are NOT correlated')
else:
    print('Features are correlated')

# P-Value for Anova is:  1.8224764694716266e-185
# Features are correlated

