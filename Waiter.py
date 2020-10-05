# Waiter.py
# Description:
# represent the restaurant's waiter
# waiter maintaining a list of diners they're currently taking care of and progress them through diff stages
# there is a cycle the waiter continuously drives through

# import the Diner and Menu class
from Diner import Diner
from Menu import Menu

class Waiter(object):
    # parameter: Menu object
    # return: none
    # assign input parameter to corresponding attribute
    # initialize the list of diners to an empty list
    def __init__(self, restaurantMenu):
        # contains all menu items offered
        # input parameter
        # initialize parameter
        self.menu = restaurantMenu

        # assign diner attribute to an empty list
        self.diners = []

    # fxn: addDiner
    # parameter: a Diner object
    # return: none
    # side effect: add to the list
    # add the new Diner object to their waiter's list of diners
    def addDiner(self, dinerObj):
        self.diners.append(dinerObj)

    # fxn: getNumDiners
    # parameter: none
    # return: an int representing the num of diners the waiter is currently keeping track of
    # side effect: none
    # can read the self.diners object
    def getNumDiners(self):
        # len of the list is the num of diners kept track of rn
        numOfDiners = len(self.diners)
        return numOfDiners

    # fxn: printDinerStatuses
    # parameter: none
    # return: none
    # side effect: print all the diners the waiter is keeping track of, grouped by their statuses
    # loop through each of the possible dining statuses a Diner might have
    def printDinerStatuses(self):
        for stage in Diner.STATUSES:
            print("Diners who are " + stage + ":")
            for person in self.diners:
                # make them both ints so can compare otherwise one is int and other is str
                if person.getStatus() == Diner.STATUSES.index(stage):
                    person.__str__()

    # fxn: takeOrders
    # parameter: none
    # return: none
    # side effect: none
    # loop through the list of diners and check if the diner's status is "ordering"
    # for each diner that is ordering, loop through the diff menu types
    def takeOrders(self):
        for person in self.diners:
            # Diner.STATUSES[1] is the "ordering"
            if person.getStatus() == 1:
                # loop through all the menu types
                for menuTypes in Menu.MENU_ITEM_TYPES:
                    self.menu.printMenuItemsByType(menuTypes)
                    itemOrdered = input(person.getName() + ", please select a " + menuTypes + " menu item number.\n> ")
                    # error checking --> for if it is a #
                    # if not valid then will stay in this loop
                    while not itemOrdered.isdigit():
                        itemOrdered = input(person.getName() + ", please select a " + menuTypes + " menu item number.\n> ")
                    itemOrdered = int(itemOrdered)
                    while itemOrdered == " ":
                        itemOrdered = input(person.getName() + ", please select a " + menuTypes + " menu item number.\n> ")
                    itemOrdered = int(itemOrdered)
                    # error checking --> if it is within a range
                    # need to figure out len of the menuType and see if the number is associated
                    while itemOrdered not in range(0,self.menu.getNumMenuItemsByType(menuTypes)):
                        itemOrdered = input(person.getName() + ", please select a " + menuTypes + " menu item number.\n> ")
                        while itemOrdered.isalpha():
                            itemOrdered = input(person.getName() + ", please select a " + menuTypes + " menu item number.\n> ")
                        itemOrdered = int(itemOrdered)
                    # out of error checking while loops
                    # get the actual object w/ type and index value
                    finalItem = self.menu.getMenuItem(menuTypes, itemOrdered)
                    person.addToOrder(finalItem)
                # print the full order
                person.printOrder()
        # outside of for loop meaning it went through all diff types

    # fxn: ringUpDiners
    # parameter: none
    # return: none
    # side effect: calculating the diner's meal cost and printing it out in a msg to diner
    # loop through the list of diners and check if the diner's status is "paying"
    def ringUpDiners(self):
        for person in self.diners:
            # Diner.STATUSES[3] is the "paying"
            if person.getStatus() == 3:
                # need to calculate the total cost
                totalAmnt = person.calculateMealCost()
                # change totalAmnt to str b/c it's a float
                print(person.getName() + ", your meal cost $" + str(totalAmnt))

    # fxn: removeDoneDiners
    # parameters: none
    # return: none
    # side effect: print a msg thanking the diner for each one that is leaving
    # loop through the list of diners backwards; use a range-based for loop
    # for each diner that is leaving, remove the diner from the list
    def removeDoneDiners(self):
        for num in range(len(self.diners) - 1, -1, -1):
            person = self.diners[num]
            # Diner.STATUSES[4] is the "leaving"
            if person.getStatus() == 4:
                # print the thank you message
                print(person.getName() + " , thank you for dining with us! Come again soon!")
                # delete person from the list
                self.diners.remove(person)

    # fxn: advanceDiners
    # parameter: none
    # return: none
    # side effect: calls on the other methods
    # call the printDinerStatuses, takeOrders, ringUpDiners, removeDiners
    # update each diner's status
    def advanceDiners(self):
        # for loop to go through the diners and update status
        for people in self.diners:
            # update each diner's status
            people.updateStatus()
        # call all methods
        self.printDinerStatuses()
        self.takeOrders()
        self.ringUpDiners()
        self.removeDoneDiners()
