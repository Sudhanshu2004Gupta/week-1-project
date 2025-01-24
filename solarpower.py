import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df=pd.read_csv('solarprediction.csv')
print(df.columns)
print(df.head)
plt.figure(figsize=(10,6))
plt.title('chart')
sns.histplot(df['generated_power_kw'], bins=30,kde=True)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()



