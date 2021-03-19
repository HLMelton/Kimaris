import self as self

class Stock:
    def __init__(stock, balance, value):
        self.balance = balance
        self.value = value

    def shares(balance,value):
        sharenum = balance / value
        if balance < value or balance == 0:
            print("Not enough funds")
        else:
            print("You can buy "+str(int(sharenum))+" shares")
            ##Look its been awhile since Ive worked with Python and this is my intro back


Apple = Stock
Apple.shares(15, 5)

