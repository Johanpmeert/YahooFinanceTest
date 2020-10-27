# This is a sample Python script to get stock quotes

import yfinance

print("Stock quote getter in Python")

stock = yfinance.Ticker('TSLA')
print(f"\n{stock.ticker} = {stock.info['shortName']}")
print(f"Stock price = {stock.info['previousClose']} {stock.info['currency']}")

stock = yfinance.Ticker('ABI.BR')
print(f"\n{stock.ticker} = {stock.info['shortName']}")
print(f"Stock price = {stock.info['previousClose']} {stock.info['currency']}")

stock = yfinance.Ticker('ASML.AS')
print(f"\n{stock.ticker} = {stock.info['shortName']}")
print(f"Stock price = {stock.info['previousClose']} {stock.info['currency']}")

stock = yfinance.Ticker('NOKIA.PA')
print(f"\n{stock.ticker} = {stock.info['shortName']}")
print(f"Stock price = {stock.info['previousClose']} {stock.info['currency']}")

stock = yfinance.Ticker('GOOGL.MI')
print(f"\n{stock.ticker} = {stock.info['shortName']}")
print(f"Stock price = {stock.info['previousClose']} {stock.info['currency']}")

stock = yfinance.Ticker('GSK.L')
print(f"\n{stock.ticker} = {stock.info['shortName']}")
print(f"Stock price = {stock.info['previousClose']} {stock.info['currency']}")