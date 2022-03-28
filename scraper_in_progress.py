import pandas as pd
from yahoo_fin import stock_info
import numpy
import schedule
import time

#Gets the current evaluation for the stock and assigns it to a variable
def CurrentValue():
    Stock1 = print(numpy.array2string(stock_info.get_live_price('HACK')))
    Stock2 = print(numpy.array2string(stock_info.get_live_price('GXC')))
    Stock3 = print(numpy.array2string(stock_info.get_live_price('VOX')))
    Stock4 = print(numpy.array2string(stock_info.get_live_price('ITA')))
    Stock5 = print(numpy.array2string(stock_info.get_live_price('GLTR')))
    Stock6 = print(numpy.array2string(stock_info.get_live_price('ICLN')))
    Stock7 = print(numpy.array2string(stock_info.get_live_price('AOR')))
    Stock8 = print(numpy.array2string(stock_info.get_live_price('GLD')))
CurrentValue()


#Function for getting current price
def CurrentPrice():
    if CurrentPrice:
        #Gets current price from yahoo_fin and outputs it in terminal, just change the ticker and ticker name
        print("Current price of: HACK $" + Stock1)
        print("Current price of ticker: GXC" + " $" +  {Stock2})
        print("Current price of ticker: VOX" + " $" + {Stock3})
        print("Current price of ticker: ITA" + " $" + {Stock4})
        print("Current price of ticker: GLTR" + " $" + {Stock5})
        print("Current price of ticker: ICLN" + " $" + {Stock6})
        print("Current price of ticker: AOR" + " $" + {Stock7})
        print("Current price of ticker: GLD" + " $" + {Stock8})
    else:
        print('panic.')
CurrentPrice()

#Add function that takes
# def CurrentValue():
#     if Stock1():
#         print(Stock1)

#Takes the task and *should* automate it to run at 9:00 AM, 1:00 PM, and 4:30 PM each weekday
schedule.every().weekday.at("9:00").do(CurrentPrice)
schedule.every().weekday.at("13:00").do(CurrentPrice)
schedule.every().weekday.at("15:30").do(CurrentPrice)

#Extra stuff for the scheduler function, ignore
while True:
    schedule.run.pending()
    time.sleep(1)
