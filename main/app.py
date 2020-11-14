# coding=utf-8

from flask import Flask
from service import StockService

app = Flask(__name__)
stockService = StockService.StockService()


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/getStock/<string:stock_number>')
def getStock(stock_number):
    return stockService.get(stock_number)


if __name__ == '__main__':
    app.run()
