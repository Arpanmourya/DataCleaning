import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')
print(df)

print('\ndata present in boxplot') 
for i in df.select_dtypes(include='number').columns:
  sns.boxplot(data=df,x=i)
  plt.show() 