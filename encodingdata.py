#final step that make sure your data is now handle for data model
import pandas as pd
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')
print(df)


pd.get_dummies(data=df,columns=['SeniorCitizen', 'Partner'])

dummy = pd.get_dummies(data=df,columns=['SeniorCitizen', 'Partner'],drop_first=True)
dummy