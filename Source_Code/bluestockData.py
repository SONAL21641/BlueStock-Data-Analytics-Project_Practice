import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("sql_import_clean_data.csv")

print(df.head())
print(df.shape)
print(df.info())


# CHECK DUPLICATE RECORDS

print("Duplicates:",df.duplicated().sum())

# REMOVE DUPLICATES

df= df.drop_duplicates()

# FILL MISSING CITY VALUES

df['City'] = df['City'].fillna('Unknown')

# CONVERT DATES

df['Order_Date'] =pd.to_datetime(
    df['Order_Date'],format='%d-%b-%y'
)

df['Ship_Date'] = pd.to_datetime(
    df['Ship_Date'],format='%d-%b-%y'
)

#CHECK MISSING VALUES AGAIN

print(df.isnull().sum())

print("Data cleaning Completed!")

################### Save Cleaned Dataset####################

df.to_csv('Cleaned_Bluestock_Sales.csv', index=False)

print("Cleaned Dataset Saved Successfully!")


################  BASIC STATISTICS #############

print("\nBasic Statistics")

print(df.describe())


########### MISSING VALUES ###########

print("\nMissing Values")
print(df.isnull().sum())


########### DUPLICATES RECORDS##########

print("Duplicate Records:", df.duplicated().sum())