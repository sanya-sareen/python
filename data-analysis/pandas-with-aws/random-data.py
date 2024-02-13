import pandas as pd
import numpy as np

#Generate sample data

data = {
    'Name': ['Alice','Bob','Charlie','David','Emma'],
    'Age': np.random.randint(20,40, size=5),
    'Salary': np.random.randint(30000,80000, size=5)
}

#Create a dataframe
df = pd.DataFrame(data)

#Perform some data manipulation
df['Bonus'] = df['Salary'] * 0.1

#Display the Dataframe
print("Original dataframe:")
print(df)

# Store the data in an excel file
excel_filename = 'sample_data.xlsx'
df.to_excel(excel_filename, index=False)

print(f"\n Data saved to '{excel_filename}' successfully")















