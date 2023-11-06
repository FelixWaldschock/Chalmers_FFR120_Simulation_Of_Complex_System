class Stock:
    # this class describes a stock in a stock market
    # it has a price and a name and a history of prices

    def __init__(self, name, price, analystRating):
        self.name = name
        self.price = price
        self.history = [price]
        self.analystRating = analystRating

    def __str__(self):
        return f"{self.name} costs {self.price}"
    
    def update_price(self, new_price):
        self.price = new_price
        self.history.append(new_price)

    def get_price(self):
        return self.price
    
    def get_history(self):
        return self.history
    
    def get_name(self):
        return self.name