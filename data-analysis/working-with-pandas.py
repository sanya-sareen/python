import pandas as pd

'''
Pandas-
* Handles large datasets
* Used for aggregation e.g. GroupBy
* Filter data
* Data cleansing
* Data manipulation
* Join and merge datasets
* Time series

Data structures-
* Pandas consist of Series and Dataframes
* Series- index and data, similar to array
* The difference between series and array is that: Series can take different datatyes and have indexes
* Dataframe- row, column and series of data

Series-
* pandas.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)

Dataframes-
* pandas.Dataframe(data=None, index=None, columns=None,...)
* iloc: can select specific rows
* loc
* head and tail
* isin
* ~ reverse
'''


index_list = [0,1,2,3,4]
data_list = [100,200,300,400,500]

series_l = pd.Series(data=data_list, index=index_list)
print(series_l)

# Using tuples in series

month_index = ['Jan','Feb','Mar','Apr']
revenude_data = (2132,4567,8797,9999)

revenue_series = pd.Series(data=revenude_data,index=month_index)
print("\nrevenue series\n",revenue_series)

print('\nrevenue data of Jan and Feb:\n', revenue_series[['Jan','Feb']])

revenue_series = pd.Series(data=revenude_data,index=month_index, dtype='float')
print("\nrevenue series\n",revenue_series)

# Using dictionary in series

dict_1 = {'key1': 'value1','key2':'value2', 'key3': 'value3','key4':'value4'}
dict_series = pd.Series(data=dict_1,index=dict_1)
print("\nUsing Dictionary:\n", dict_series)

# Dataframes

row_labels = [0,1,2,3,4]
column_labels = ['A','B','C']
data = [[1,2,3], [4,5,6],[7,8,9],[10,11,12],[1,4,5]]
df = pd.DataFrame(index=row_labels, data=data, columns=column_labels)
print("\n DataFrames:\n",df)

# with dict, tuples
data_01 = [[1,2,3], {4,5,6}, {7,8,9}, [10,11,12],(3,5,6)]
df1 = pd.DataFrame(index=row_labels, data=data_01, columns=column_labels)
print("\n DataFrames:\n",df1)

# Read csv file
countries_data = pd.read_csv('top_10_countries.csv')
print(countries_data)

print(countries_data.iloc[3])

print("Countriess data fom 3rd row\n",countries_data.iloc[3:])

print("Using loc:",countries_data.loc[2,'Country / Dependency'])

print("\nPrint data starting from US",countries_data.loc[2:,['Country / Dependency','Population']])

print("\nDetails of the Asian Region\n\n",countries_data[countries_data['Region']=='Asia'])

print("\nDetails of the Asian Region having population greater than 30000000\n\n",countries_data[(countries_data['Region']=='Asia') & (countries_data['Population']>300000000)])

print("\nDetails of the Asian Region or Region having population greater than 30000000\n\n",countries_data[(countries_data['Region']=='Asia') | (countries_data['Population']>300000000)])

# head displays first 5 datas and tail displays last 5 data
print("Using Head::\n",countries_data.head())

print("Using Tail::\n",countries_data.tail())

print("Using isin::\n",countries_data[countries_data['Region'].isin(['Asia','Americas'])])

print("Countries which are not in Asia and America::\n\n",countries_data[~countries_data['Region'].isin(['Asia','Americas'])])