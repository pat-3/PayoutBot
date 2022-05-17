import pandas as pd
from sympy import NumberSymbol
from yahoo_fin import stock_info
import numpy
import schedule
import time

StockTicker = ['HACK', 'GXC', 'VOX', 'ITA', 'GLTR', 'ICLN', 'AOR', 'GLD', 'JXI', 'AAPL']
stocks = []

#Gets the current dollar value for the stock and assigns it to a variable
for i in range(len(StockTicker)):
    stocks.append(numpy.array2string(stock_info.get_live_price(StockTicker[i])))

#Function for getting current price
def CurrentPrice():
    if CurrentPrice:
        for i in range(len(stocks)):
            print('Current price of ' + str(StockTicker[i]) +' : $' + str(stocks[i]))
        #Outputs the value of the the stock variable and puts in terminal so its usable
    else:
        print('panic.')
CurrentPrice()
