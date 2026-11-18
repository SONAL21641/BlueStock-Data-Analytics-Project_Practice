
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("sql_import_clean_data.csv")

print(df.head())
print(df.shape)
print(df.info())

##############Region-wise Sales Chart##############

region_sales = df.groupby('Region')['Sales'].sum()

region_sales.plot(kind='bar', figsize=(8, 5))

plt.title('Region-wise Sales Analysis')
plt.xlabel('Region')
plt.ylabel('Total Sales')

plt.tight_layout()
plt.savefig('Region_Wise_Sales.png')
plt.show()