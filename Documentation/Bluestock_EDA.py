###### OUTLIER DETECTION #######
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("sql_import_clean_data.csv")

print(df.head())
print(df.shape)
print(df.info())

# Outlier Detection Using IQR #

for col in ['Sales','Profit','Quantity']:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    
    IQR = Q3 - Q1
    
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    
    outliers = df[
        (df[col]<lower) | (df[col]>upper)
    ]
    
    print(col,"Outliers:",len(outliers))
    
    
########## Correlation Analysis #############

correlation = df[
    ['Sales', 'Quantity', 'Discount', 'Profit']
].corr()

print(correlation)

# Correlation Heatmap
import seaborn as sns

sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Sales Data Correlation')
plt.tight_layout()
plt.savefig('Correlation_Heatmap.png')
plt.show()


########## Trend Analysis & Monthly Sales ##########

df['Order_Date'] = pd.to_datetime(df['Order_Date'])

monthly_sales = (
    df.groupby(df['Order_Date'].dt.to_period('M'))['Sales']
    .sum()
)

print(monthly_sales)

monthly_sales.plot(kind='line', figsize=(10, 5))

plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.tight_layout()

plt.savefig('Monthly_Sales_Trend.png')
plt.show()


print(df[['Sales', 'Profit', 'Quantity', 'Discount']].describe())

print("Negative Sales:", (df['Sales'] < 0).sum())
print("Negative Quantity:", (df['Quantity'] < 0).sum())
print("Invalid Discount:", (~df['Discount'].between(0, 1)).sum())


################## BUSINESS INSIGHTS REPORT############

# Business Insights Report

print("\n--- BUSINESS INSIGHTS ---")

print("Total Sales:", df['Sales'].sum())
print("Total Profit:", df['Profit'].sum())

print("\nTop Region:")
print(df.groupby('Region')['Sales'].sum().idxmax())

print("\nTop Category:")
print(df.groupby('Category')['Profit'].sum().idxmax())

print("\nTop 5 Products:")
print(df.groupby('Product_Name')['Sales']
      .sum().nlargest(5))