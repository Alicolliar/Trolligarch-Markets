from flask import Flask, render_template, request, send_from_directory, url_for, redirect
import csv
import functs
app = Flask(__name__)

app.config["HISTORIC_SHEETS"] = "backendData/"
app.config["PWNED_SHIFT"] = "YOUR-CEASAR-SHIFT-NUMBER"
@app.route('/backendData/<sheetName>')
def giveHistoric(sheetName):
    return send_from_directory(app.config["HISTORIC_SHEETS"], filename=sheetName)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/rawhistorical')
def rawhistorical():
    return render_template('raw.html')

@app.route('/lookup', methods=['post', 'get'])
def lookup():
        data = []
        if request.method == "POST":
            ticker = request.form.get("ticker")
            tickers = []
            name = []
            price = []
            vol = []
            tickers, name, price, vol = functs.stockLookup()
            for i in range(len(tickers)):
                if tickers[i] == ticker:
                    data.append(ticker)
                    data.append(name[i])
                    data.append(price[i])
                    data.append(vol[i])

        return render_template('about.html', message=data)

@app.route('/invest', methods=['post', 'get'])
def investPage():
     message = ""
     if request.method == "POST":
         orderFile = open("orders.csv", "a")
         person = request.form.get("purchaser")
         stock = request.form.get("stock")
         vol = float(request.form.get("volume"))
         orders = csv.writer(orderFile)
         tickers = []
         names = []
         prices = []
         tickers, names, prices = functs.abridStockLookup()
         for i in range(len(tickers)):
             if tickers[i] == stock:
                 price = float(prices[i])
                 name = names[i]

         totalCost = ((price*vol)+((price*vol)*0.15))
         orderData = [person, stock, vol, str(price), str(totalCost)]
         orders.writerow(orderData)
         message = "Order for " + str(vol) + " of " + name + " placed. Total including tax is £" + str(totalCost) + "."
     return render_template('invest.html', message=message)

@app.route('/login', methods=['post', 'get'])
def loginPage():
    message = ""
    if request.method == 'POST':
        shift = int(app.config["PWNED_SHIFT"])
        uName = request.form.get("user")
        pWord = request.form.get("pwned")
        if uName == "" or pWord == "":
            message = "Please enter a username or password."
        else:
            uNames = []
            dbpWords = []
            dbpWord = ""
            uNames, dbpWords = functs.pwnedLookup(uName)
            for i in range(len(uNames)):
                if uNames[i] == uName:
                    dbpWord = dbpWords[i]

            decpWord = functs.deCodePwneds(dbpWord, shift)
            if pWord  == decpWord:
                return redirect(url_for('adminPortal'))
            else:
                message = "Incorrect username/password"
                return render_template('login.html', message=message)

    return render_template('login.html', message=message)

@app.route('/admin',methods=['post', 'get'])
def adminPortal():
    message=""
    shift = int(app.config["PWNED_SHIFT"])
    if request.method == 'POST':
        if 'nUserMake' in request.form:
            nUser = request.form.get("nUname")
            nPwd = request.form.get("nPwd")
            cUsers = []
            pwneds = []
            cUsers, pwneds = functs.pwnedLookup(nUser)
            if nUser in cUsers:
                message = "User already exists."
                return render_template('admin.html', message=message)
            else:
                hoomanFile = open("static/private/userAccounts/bullshit.csv", "a")
                hoomans = csv.writer(hoomanFile)
                enCodedPwned = functs.enCodePwneds(nPwd, shift)
                nUser = [nUser, enCodedPwned]
                hoomans.writerow(nUser)
                message = "User added successfully."
                return render_template('admin.html', message=message)
        elif "stockAdd" in request.form:
            nName = request.form.get("stockName")
            nSymbol = request.form.get("stockSymbol")
            nIPOPrice = request.form.get("stockPrice")
            nVol = request.form.get("stockVol")
            nStock = [nSymbol,nName,nIPOPrice,nVol]
            tickers = []
            names = []
            prices = []
            tickers, names, prices = functs.abridStockLookup()
            if nName in names:
                message="Company name already listed"
                return render_template('admin.html', message=message)
            elif nSymbol in tickers:
                message = "Company ticker already listed"
                return render_template('admin.html', message=message)
            else:
                stockFile = open("backendData/stocks.csv", "a")
                stockTyper = csv.writer(stockFile)
                stockTyper.writerow(nStock)
                message="Stock"+nName+"IPOd"
                return render_template('admin.html', message=message)

    return render_template('admin.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)
