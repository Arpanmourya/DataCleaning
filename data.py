import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')
print(df)
print('\nColumns\n',df.columns)
print('\nData Shape: \n',df.shape)
print('\nData information: \n',df.info)
print('\nData describe: \n',df.describe())
print('\nPercentage of null value in data: \n',df.isnull().sum()/df.shape[0]*100)
print('\nDuplicate number in data: \n',df.duplicated().sum())
print('\nDelete 0r remove duplicate numbers : \n',df.drop_duplicates(inplace=True))

print('\nUnique value count of every column: ')
for i in df.select_dtypes(include='object').columns:
  print(df[i].value_counts())
  print('****'*10)

print('\nData present by histogram: ') 
for i in df.select_dtypes(include='number').columns:
  plt.figure(figsize=(10,8))
  sns.histplot(data=df,x=i)
  plt.show() 

