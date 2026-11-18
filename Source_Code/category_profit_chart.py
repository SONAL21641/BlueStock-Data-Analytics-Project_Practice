import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("sql_import_clean_data.csv")

print(df.head())
print(df.shape)
print(df.info())


######################Category-wise Profit Chart###############

category_profit = df.groupby('Category')['Profit'].sum()

category_profit.plot(kind='bar', figsize=(8, 5))

plt.title('Category-wise Profit Analysis')
plt.xlabel('Category')
plt.ylabel('Total Profit')

plt.tight_layout()
plt.savefig('Category_Wise_Profit.png')
plt.show()