import csv

def stockLookup(ticker):
    stockFile = open("stocks.csv", "r")
    stocks = csv.reader(stockFile)
    name = []
    tickers = []
    price = []
    vol = []
    for row in stocks:
        tickers.append(row[0])
        name.append(row[1])
        price.append(row[2])
        vol.append(row[3])

    return tickers, name, price, vol

def abridStockLookup(ticker):
    stockFile = open("stocks.csv", "r")
    stocks = csv.reader(stockFile)
    tickers = []
    price = []
    vol = []
    for row in stocks:
        tickers.append(row[0])
        price.append(row[2])

    return tickers, price
