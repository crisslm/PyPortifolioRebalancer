#SINGLE ASSET THAT WILL BE ASSIGNED TO A CLIENTE
class Asset:
    #Possible categories: Stocks, REITs, Bonds
    def __init__(self, ticket, category, price, quantity):
        self.ticket = ticket
        self.category = category
        self.price = price
        self.quantity = quantity

    def total_asset_value(self):
        return self.price * self.quantity

    def get_category(self):
        return self.category

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity
