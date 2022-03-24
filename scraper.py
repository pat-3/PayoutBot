import pandas as pd
from yahoo_fin import stock_info
import numpy

def CurrentPrice():
    if CurrentPrice:
        print("Current price for ticker: HACK" + " $" + numpy.array2string(stock_info.get_live_price('HACK')))
        print("Current price for ticker: GXC" + " $" +  numpy.array2string(stock_info.get_live_price('GXC')))
        print("Current price for ticker: VOX" + " $" + numpy.array2string(stock_info.get_live_price('VOX')))
        print("Current price for ticker: ITA" + " $" + numpy.array2string(stock_info.get_live_price('ITA')))
        print("Current price for ticker: GLTR" + " $" + numpy.array2string(stock_info.get_live_price('GLTR')))
        print("Current price for ticker: ICLN" + " $" + numpy.array2string(stock_info.get_live_price('ICLN')))
        print("Current price for ticker: AOR" + " $" + numpy.array2string(stock_info.get_live_price('AOR')))
        print("Current price for ticker: GLD" + " $" + numpy.array2string(stock_info.get_live_price('GLD')))
    else:
        print('panic.')
CurrentPrice()