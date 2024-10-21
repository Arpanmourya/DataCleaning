import pandas as pdff
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')
print(df)

for i in ['customerID', 'gender', 'SeniorCitizen', 'Partner', 'Dependents',
          'tenure', 'PhoneService', 'MultipleLines', 'InternetService',
          'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
          'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
          'PaymentMethod', 'TotalCharges', 'Churn']:
    sns.scatterplot(data=df, x=i, y= 'MonthlyCharges')
    plt.show()