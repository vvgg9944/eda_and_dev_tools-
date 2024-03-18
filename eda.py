
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

abalones=pd.read_csv('/Users/Admin/Downloads/abalone (1).csv')
# print(abalones)

# abalones.info()

print(abalones.duplicated().sum())

# to get abalone's age - add 1.5 to rings

abalones['Rings'] =  abalones['Rings'] + 1.5
print(abalones.head(5))



