import self as self
import yfinance as yf

class Stock:
    def __init__(stock, balance, value):
        ##Need to fix some of the variables below and fix some of the integrations with the price fetcher.
        self.balance = balance
        self.value = value
        self.symbol = symbol

    def potshares(balance,value):
        share_num = balance / value
        if balance < value or balance == 0:
            print("Not enough funds")
        else:
            print("You can buy "+str(int(share_num))+" shares")

    def get_current_price(symbol):
        ticker = yf.Ticker(symbol)
        todays_data = ticker.history(period='1d')
        return todays_data['Close'][0]



Apple = Stock
Apple.potshares(15, 5)

