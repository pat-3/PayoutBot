import pandas as pd
from yahoo_fin import stock_info
import numpy
import schedule
import time

#Gets the current dollar value for the stock and assigns it to a variable
Stock1 = numpy.array2string(stock_info.get_live_price('HACK'))
Stock2 = numpy.array2string(stock_info.get_live_price('GXC'))
Stock3 = numpy.array2string(stock_info.get_live_price('VOX'))
Stock4 = numpy.array2string(stock_info.get_live_price('ITA'))
Stock5 = numpy.array2string(stock_info.get_live_price('GLTR'))
Stock6 = numpy.array2string(stock_info.get_live_price('ICLN'))
Stock7 = numpy.array2string(stock_info.get_live_price('AOR'))
Stock8 = numpy.array2string(stock_info.get_live_price('GLD'))


#Function for getting current price
def CurrentPrice():
    if CurrentPrice:
        #Outputs the value of the the stock variable and puts in terminal so its usable
        print("Current price of HACK: $" + str(Stock1))
        print("Current price of ticker GXC: $" +  str(Stock2))
        print("Current price of ticker VOX: $" + str(Stock3))
        print("Current price of ticker ITA: $" + str(Stock4))
        print("Current price of ticker GLTR: $" + str(Stock5))
        print("Current price of ticker ICLN: $" + str(Stock6))
        print("Current price of ticker AOR: $" + str(Stock7))
        print("Current price of ticker GLD: $" + str(Stock8))
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
