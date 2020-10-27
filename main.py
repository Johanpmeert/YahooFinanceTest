# This is a sample Python script to get stock quotes

import yfinance

print("Stock quote getter in Python")

stocklist = ['TSLA','ABI.BR','ASML.AS','NOKIA.PA','GOOGL.MI','GSK.L']

for stock in stocklist:
    stockdata = yfinance.Ticker(stock)
    print(f"\n{stockdata.ticker} = {stockdata.info['shortName']}")
    print(f"Stock price = {stockdata.info['previousClose']} {stockdata.info['currency']}")
