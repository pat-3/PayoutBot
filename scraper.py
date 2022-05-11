import pandas as pd
from yahoo_fin import stock_info
import numpy
import schedule
import time


StockTicker1 = 'HACK'
StockTicker2 = 'GXC'
StockTicker3 = 'VOX'
StockTicker4 = 'ITA'
StockTicker5 = 'GLTR'
StockTicker6 = 'ICLN'
StockTicker7 = 'AOR'
StockTicker8 = 'GLD'
StockTicker9 = 'JXI'
StockTicker10 = 'AAPL'

#Gets the current dollar value for the stock and assigns it to a variable
Stock1 = numpy.array2string(stock_info.get_live_price(StockTicker1))
Stock2 = numpy.array2string(stock_info.get_live_price(StockTicker2))
Stock3 = numpy.array2string(stock_info.get_live_price(StockTicker3))
Stock4 = numpy.array2string(stock_info.get_live_price(StockTicker4))
Stock5 = numpy.array2string(stock_info.get_live_price(StockTicker5))
Stock6 = numpy.array2string(stock_info.get_live_price(StockTicker6))
Stock7 = numpy.array2string(stock_info.get_live_price(StockTicker7))
Stock8 = numpy.array2string(stock_info.get_live_price(StockTicker8))
Stock9 = numpy.array2string(stock_info.get_live_price(StockTicker9))
Stock10 = numpy.array2string(stock_info.get_live_price(StockTicker10))


#Function for getting current price
def CurrentPrice():
    if CurrentPrice:
        #Outputs the value of the the stock variable and puts in terminal so its usable
        print("Current price of "+ str(StockTicker1) +" : $" + str(Stock1))
        print("Current price of "+ str(StockTicker2) +" : $" + str(Stock2))
        print("Current price of "+ str(StockTicker3) +" : $" + str(Stock3))
        print("Current price of "+ str(StockTicker4) +" : $" + str(Stock4))
        print("Current price of "+ str(StockTicker5) +" : $" + str(Stock5))
        print("Current price of "+ str(StockTicker6) +" : $" + str(Stock6))
        print("Current price of "+ str(StockTicker7) +" : $" + str(Stock7))
        print("Current price of "+ str(StockTicker8) +" : $" + str(Stock8))
        print("Current price of "+ str(StockTicker9) +" : $" + str(Stock9))
        print("Current price of "+ str(StockTicker10) +" : $" + str(Stock10))
    else:
        print('panic.')
CurrentPrice()


#Takes the task and *should* automate it to run at 9:00 AM, 1:00 PM, and 4:30 PM each weekday
schedule.every().monday.at("9:00").do(CurrentPrice)
schedule.every().monday.at("13:00").do(CurrentPrice)
schedule.every().monday.at("15:30").do(CurrentPrice)
schedule.every().tuesday.at("9:00").do(CurrentPrice)
schedule.every().tuesday.at("13:00").do(CurrentPrice)
schedule.every().tuesday.at("15:30").do(CurrentPrice)
schedule.every().wednesday.at("9:00").do(CurrentPrice)
schedule.every().wednesday.at("13:00").do(CurrentPrice)
schedule.every().wednesday.at("15:30").do(CurrentPrice)
schedule.every().thursday.at("9:00").do(CurrentPrice)
schedule.every().thursday.at("13:00").do(CurrentPrice)
schedule.every().thursday.at("15:30").do(CurrentPrice)
schedule.every().friday.at("9:00").do(CurrentPrice)
schedule.every().friday.at("13:00").do(CurrentPrice)
schedule.every().friday.at("15:30").do(CurrentPrice)

#Extra stuff for the scheduler function, ignore
while True:
    schedule.run.pending()
    time.sleep(1)
