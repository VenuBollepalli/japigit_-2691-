import sys

import pandas as pd

from alpha_vantage.timeseries import TimeSeries # Alpha_vantage_wrapper


API_KEY = 'Y1I6SB2H2IS15SJM'

def getStockdata(symbol):

    try:

        print("Gathering info....")

        timeSeries = TimeSeries(key=API_KEY, output_format='pandas')

        data, meta_data = timeSeries.get_intraday(symbol=symbol, interval='5min')

        return str(data.tail(1).iloc[0]['4. close'])

    except:

        return "not found"

def main():

    outFile = open('japi.out', 'w')

    while 1:

        userInput = input("Enter Stock Symbol or QUIT to quit: ").upper()

        if userInput != "QUIT":

            serverData = 'The current price of {} is {}\n'.format(userInput, getStockdata(userInput))

            print(serverData)

            outFile.write(serverData)

        else:

            sys.exit("\nThank you for the data!\n")

main()