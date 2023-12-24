import numpy as np #The Numpy numerical computing library
import pandas as pd #The Pandas data science library
import requests #The requests library for HTTP requests in Python
import xlsxwriter
import math

IEX_CLOUD_API_TOKEN="sk_817db7056d6345f2a66b01aab716bc17"
stocks = pd.read_csv('sp_500_stocks.csv')
# print(stocks)

symbol='AAPL'
# https://api.iex.cloud/v1/data/core/quote/aapl?token=YOUR_TOKEN
# api_url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote?token={IEX_CLOUD_API_TOKEN}'
api_url = 'https://api.iex.cloud/v1/data/core/quote/aapl?token=sk_817db7056d6345f2a66b01aab716bc17'
data = requests.get(api_url).json()
# print(data)
# print(data[0]['latestPrice'])
# print(data[0]['marketCap'])

my_columns = ['Ticker', 'Price','Market Capitalization', 'Number Of Shares to Buy']
final_dataframe = pd.DataFrame(columns = my_columns)
# print(final_dataframe)


# final_dataframe = final_dataframe.append(
#                                         pd.Series(['AAPL',
#                                                    data[0]['latestPrice'],
#                                                    data[0]['marketCap'],
#                                                    'N/A'],
#                                                   index = my_columns),
#                                         ignore_index = True)
# final_dataframe

# print(final_dataframe)


# for stock in stocks['Ticker'][:5]:
#     api_url = f'https://api.iex.cloud/v1/data/core/quote/{stock}?token=sk_817db7056d6345f2a66b01aab716bc17'
#     data = requests.get(api_url).json()
#     # print(data)
#     final_dataframe = final_dataframe.append(
#         pd.Series([stock,
#         data[0]['latestPrice'],
#         data[0]['marketCap'],
#         'N/A'],
#         index = my_columns),
#         ignore_index = True)
#
#   # print(stock)
#
# print(final_dataframe)


def chunks(lst, n):
    """Yield successive n-sized chunks from list"""
    for i in range(0, len(lst),n):
        yield  lst[i:i+n]

symbol_groups = list(chunks(stocks['Ticker'],100))
# print(symbol_groups)
symbol_strings = []
for i in range(0, len(symbol_groups)):
    symbol_strings.append(','.join(symbol_groups[i]))
    # print(symbol_groups[i])

for symbol_string in symbol_strings:

    batch_api_call_url = f'https://api.iex.cloud/v1/data/core/quote/{symbol_string}?token=sk_817db7056d6345f2a66b01aab716bc17'
    data = requests.get(batch_api_call_url).json()

    for symbol in symbol_string.split(','):
        final_dataframe = final_dataframe.append(
            pd.Series([symbol,
                   data[0]['latestPrice'],
                   data[0]['marketCap'],
                   'N/A'],
                  index=my_columns),
                  ignore_index=True)

# print(final_dataframe)

# calculate the number of shares to buy

portfolio_size = input('Enter the value of your portfolio:')

try:
    val = float(portfolio_size)
except ValueError:
    print("That's not a number! \n Please try again:")
    portfolio_size = input("Enter the value of your portfolio:")
    val = float(portfolio_size)

position_size = val/len(final_dataframe.index)
# print(position_size)
#
# number_of_apple_shares = position_size/500
# print(number_of_apple_shares)

for i in range(0, len(final_dataframe['Ticker'])-1):
    # print(i)
    final_dataframe.loc[i,'Number of shares to Buy'] = math.floor(position_size/final_dataframe['Price'][i])

# print(final_dataframe)

writer = pd.ExcelWriter('recommended_trades.xlsx', engine='xlsxwriter')
final_dataframe.to_excel(writer, sheet_name='Recommended Trades', index = False)

background_color = '#0a0a23'
font_color = '#ffffff'

string_format = writer.book.add_format(
        {
            'font_color': font_color,
            'bg_color': background_color,
            'border': 1
        }
    )

dollar_format = writer.book.add_format(
        {
            'num_format':'$0.00',
            'font_color': font_color,
            'bg_color': background_color,
            'border': 1
        }
    )

integer_format = writer.book.add_format(
        {
            'num_format':'0',
            'font_color': font_color,
            'bg_color': background_color,
            'border': 1
        }
    )

column_formats = {
                    'A': ['Ticker', string_format],
                    'B': ['Price', dollar_format],
                    'C': ['Market Capitalization', dollar_format],
                    'D': ['Number of Shares to Buy', integer_format]
                    }

for column in column_formats.keys():
    writer.sheets['Recommended Trades'].set_column(f'{column}:{column}', 20, column_formats[column][1])
    writer.sheets['Recommended Trades'].write(f'{column}1', column_formats[column][0], string_format)

writer.save()