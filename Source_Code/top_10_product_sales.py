import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("sql_import_clean_data.csv")

print(df.head())
print(df.shape)
print(df.info())

############## Top 10 Products by Sales##############

top_products = (
    df.groupby('Product_Name')['Sales']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

top_products.plot(kind='bar', figsize=(10, 5))

plt.title('Top 10 Products by Sales')
plt.xlabel('Product Name')
plt.ylabel('Total Sales')
plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.savefig('Top_10_Products.png')
plt.show()


################### Save Cleaned Dataset####################

df.to_csv('Cleaned_Bluestock_Sales.csv', index=False)

print("Cleaned Dataset Saved Successfully!")