import csv

def stockLookup():
    stockFile = open("backendData/stocks.csv", "r")
    stocks = csv.reader(stockFile)
    next(stocks)
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

def abridStockLookup():
    stockFile = open("backendData/stocks.csv", "r")
    stocks = csv.reader(stockFile)
    next(stocks)
    tickers = []
    name = []
    price = []
    vol = []
    for row in stocks:
        tickers.append(row[0])
        name.append(row[1])
        price.append(row[2])

    return tickers, name, price

def pwnedLookup(uName):
    hoomanFile = open("static/private/userAccounts/bullshit.csv", "r")
    hoomans = csv.reader(hoomanFile)
    next(hoomans)
    uNames = []
    pwneds = []
    for row in hoomans:
        uNames.append(row[0])
        pwneds.append(row[1])

    return uNames, pwneds

def deCodePwneds(pwned, shift):
    decPwn = ""
    for char in pwned:
        code = int(ord(char))
        code += shift
        nChar = chr(code)
        decPwn = decPwn + nChar

    return decPwn


def enCodePwneds(pwned, shift):
    Pwn = ""
    for char in pwned:
        code = int(ord(char))
        code -= shift
        nChar = chr(code)
        Pwn = Pwn + nChar

    return Pwn
