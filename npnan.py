import pandas as pd
import numpy as np
data={
    'Age':[25,30,np.nan,35,np.nan],
    'Salary':[50000,54000,50000,np.nan,62000],
    'Gender':['Male','Female',np.nan,'Female','male'],
    'Department':['IS',np.nan,'CS','EC','EEE']
}
# by using np.nan the column will be empty
df=pd.DataFrame(data)
df.to_csv('sample.csv',index=False)
df.to_json('sample.json',orient='records')
df.isnull()
print("\nCount of Missing Values in Each column: \n",df.isnull().sum())
df_dropped=df.dropna()
print("\nDataFrame after Dropping Rows with missing Values:\n",df_dropped)
#df['Age'].fillna(df['Age'].mean(),inplace=True)
#df.fillna({'Age': df['Age'].mean()}, inplace=True)
df['Age'] = df['Age'].fillna(df['Age'].mean())
print("\nDataFrame after filling 'Age' with Mean:\n",df)
