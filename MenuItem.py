# MenuItem.py
# Description:
# represents single item that a diner can order from the restaurant's menu

class MenuItem(object):
    # parameter 1: str representing name of MenuItem
    # parameter 2: str representing type of item
    # parameter 3: float representing price of item
    # parameter 4: str containing description of item
    # return value: none
    def __init__(self, name, itemType, price, description):
        # instance attributes
        self.name = name
        self.type = itemType
        self.price = price
        self.description = description

    # need a getter fxn for name
    def getName(self):
        return self.name

    # need a getter fxn for type
    def getType(self):
        return self.type

    # need a getter fxn for price
    def getPrice(self):
        return self.price

    # need a getter fxn for description
    def getDescription(self):
        return self.description

    # parameters: none
    # return: str
    # constructs message containing all 4 attributes
    def __str__(self):
        msg = self.name + " (" + self.type + "): $" + str(self.price)
        msg += "\n\t" + self.description
        return msg
