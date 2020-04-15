from flask import Flask, render_template, request, make_response
import csv
app = Flask(__name__)
@app.route('/')
def home():
    page = make_response(render_template('home.html'))
    page.set_cookie("Got my eye on you", "I'm just funning you")
    return page

@app.route('/lookup', methods=['post', 'get'])
def lookup():
        data = []
        if request.method == "post":
            stockFile = open("stocks.csv", "r")
            stocks = csv.reader(stockFile)
            ticker = request.form.get(ticker)
            for row in stocks:
                tickers.append(row[0])
                name.append(row[1])
                price.append(row[2])
                vol.append(row[3])

            for i in range(len(tickers)):
                if tickers[i] == ticker:
                    data.append(ticker)
                    data.append(name[i])
                    data.append(price[i])
                    data.append(vol[i])
            if data == False:
                data.append("Invalid Stock")

        return render_template('about.html', message=data)

@app.route('/invest', methods=['post', 'get'])
def investPage():
     if request.method == 'post':
         stockFile = open("stocks.csv", "r")
         orderFile = open("orders.csv", "w")
         person = request.form.get("purchaser")
         stock = request.form.get("stock")
         vol = request.form.get("volume")
         stocks = csv.reader(stockFile)
         orders = csv.writer(orderFile)
         for rows in stocks:
             if row[0] == stock:
                 price = row[2]

         totalCost = (price*vol)+((price*vol)*0.15)
         orderData = [person, stock, vol, price, totalCost]
         orders.writewrows(orderData)
     return render_template('invest.html')

if __name__ == '__main__':
    app.run(debug=True)
