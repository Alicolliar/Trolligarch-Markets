from flask import Flask, render_template, request, make_response
import csv
import functs
app = Flask(__name__)
@app.route('/')
def home():
    page = make_response(render_template('home.html'))
    page.set_cookie("Got my eye on you", "I'm just funning you")
    return page

@app.route('/lookup', methods=['post', 'get'])
def lookup():
        data = []
        if request.method == "POST":
            ticker = request.form.get("ticker")
            tickers = []
            name = []
            price = []
            vol = []
            tickers, name, price, vol = functs.stockLookup(ticker)
            for i in range(len(tickers)):
                if tickers[i] == ticker:
                    data.append(ticker)
                    data.append(name[i])
                    data.append(price[i])
                    data.append(vol[i])

        return render_template('about.html', message=data)

@app.route('/invest', methods=['post', 'get'])
def investPage():
     if request.method == "POST":
         orderFile = open("orders.csv", "w")
         person = request.form.get("purchaser")
         stock = request.form.get("stock")
         vol = request.form.get("volume")
         orders = csv.writer(orderFile)
         tickers = []
         prices = []
         tickers, prices = functs.abridStockLookup("ticker")
         for i in range(len(tickers)):
             if tickers[i] == stock:
                 price = int(prices[i])

         totalCost = (price*vol)
         orderData = [person, stock, vol, str(price), str(totalCost)]
         orders.writerow(orderData)
     return render_template('invest.html')

if __name__ == '__main__':
    app.run(debug=True)
