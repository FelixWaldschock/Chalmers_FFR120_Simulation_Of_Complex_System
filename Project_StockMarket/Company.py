class Company:
    # this class describes a company, consisting of a name and an amount of stocks
    #

    def __init__(self, name, stocks, numberOfStocks):
        self.name = name
        self.stocks = stocks
        self.numberOfStocks = numberOfStocks

    def __str__(self):
        return f"{self.name} has {self.numberOfStocks} stocks"
    
    def get_name(self):
        return self.name
    
    def get_stocks(self):
        return self.stocks
    
    
