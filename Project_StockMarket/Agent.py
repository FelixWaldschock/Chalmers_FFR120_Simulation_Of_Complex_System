class Agent:
    # this class describes the agent of a stock market
    # it has a portfolio of stocks and liquiity

    def __init__(self, name, cash, stocks):
        self.name = name
        self.cash = cash
        self.stocks = stocks
    
    def __str__(self):
        return f"{self.name} has {self.cash} cash and {self.stocks} stocks"
    
    def buy(self, stock, amount):
        self.cash -= stock.price * amount
        self.stocks[stock] += amount

    def sell(self, stock, amount):
        self.cash += stock.price * amount
        self.stocks[stock] -= amount

    def net_worth(self):
        return self.cash + sum([stock.price * amount for stock, amount in self.stocks.items()])
    
    def get_stock_amount(self, stock):
        return self.stocks[stock]