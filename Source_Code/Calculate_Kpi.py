import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("sql_import_clean_data.csv")


#################### CALCULATE KPI ####################

total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
total_orders = df['Order_ID'].nunique()
total_customers = df['Customer_ID'].nunique()
total_quantity = df['Quantity'].sum()
average_sales = df['Sales'].mean()


print("Total Sales:", round(total_sales, 2))
print("Total Profit:", round(total_profit, 2))
print("Total Orders:", total_orders)
print("Total Customers:", total_customers)
print("Total Quantity:", total_quantity)
print("Average Sales:", round(average_sales, 2))
