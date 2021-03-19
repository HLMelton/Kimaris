import yfinance as yf

def get_current_price(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return todays_data['Close'][0]

print('Enter the your ticker:')
user_ticker = input()
print(get_current_price(str(user_ticker)))
print(yf.Ticker(user_ticker).info)