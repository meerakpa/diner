# Diner.py
# DESCRIPTION:
# represents one of the diners at the restaurant and keeps track of their status and meal

# import MenuItem class
from MenuItem import MenuItem


# create a new class
class Diner(object):
    # static variable for this class
    STATUSES = ["seated","ordering","eating","paying","leaving"]

    # parameter: str of diner's name
    # return: none
    # set diner attributes to input value
    # set diner's order attribute to an empty list --> no ordered items yet
    # set status attribute to 0 --> seated status
    def __init__(self, dinerName):
        self.name = dinerName
        self.Order = []
        self.Status = 0

    # need a getter fxn for name
    def getName(self):
        return self.name

    # need a getter fxn for Order
    def getOrder(self):
        return self.Order

    # need a getter fxn for Status
    def getStatus(self):
        return self.Status

    # fxn: updateStatus
    # parameter: none
    # return: none
    # side effect: manipulate the variable
    # inc diner's status by 1
    def updateStatus(self):
        self.Status += 1

    # fxn: addToOrder
    # parameter: menuItem object
    # return: none
    # side effect: none
    # add menu item to end of list of menu items
    def addToOrder(self, menuItemObjs):
        self.Order.append(menuItemObjs)

    # fxn: printOrder
    # parameter: none
    # return: none
    # side effect: print
    # displays message containing all menu items the diner ordered
    def printOrder(self):
        print("\n", self.name, "ordered:")
        counter = 0
        for item in self.Order:
            if counter == 0:
                itemMenuType = "Drink"
                counter += 1
            if counter == 1:
                itemMenuType = "Appetizer"
                counter += 1
            if counter == 2:
                itemMenuType = "Entree"
                counter += 1
            if counter == 3:
                itemMenuType = "Dessert"
                counter = 0
            itemName = item[0]
            itemPrice = item[1]
            itemDesc = item[2]
            fullItem = MenuItem(itemName, itemMenuType, itemPrice, itemDesc)
            print("-", fullItem)


    # fxn: calculateMealCost
    # parameter: none
    # return: float representing total cost of the diner's mean
    # side effect: none
    # total up the cost of each of the menu items the diner ordered
    def calculateMealCost(self):
        # for loop to go through every item in the self.orders
        floatTotal = 0.0
        for item in self.Order:
            # item[1] = price
            floatTotal = floatTotal + float(item[1])
        return floatTotal

    # parameter: none
    # return: str
    # construct msg containing diner's name and status
    def __str__(self):
        # need to tab the status msg
        dinerStatusStr = print("\tDiner " + self.name + " is currently " + Diner.STATUSES[self.Status] + ".")
        return dinerStatusStr
