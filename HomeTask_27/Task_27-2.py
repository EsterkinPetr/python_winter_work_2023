class Item:
    def __init__(self, name, price, quantity):
        self.name = name.capitalize()
        self.price = price
        self.quantity = quantity
        self.total = self.price * self.quantity


a = Item('pen', 100, 5)
print(a.name)
print(a.total)




