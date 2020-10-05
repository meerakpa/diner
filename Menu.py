# Menu.py
# DESCRIPTION:
# represents the restaurant's menu containing 4 diff categories of menu items that diners can order from

# import MenuItem class from the .py file
from MenuItem import MenuItem

class Menu(object):
    # static variable --> does NOT change
    # list containing 4 str of diff type of menu items
    MENU_ITEM_TYPES= ["Drink", "Appetizer", "Entree", "Dessert"]

    # parameter: str representing name of the csv file that contains info about menu items from restaurant's menu
    # return: none
    def __init__(self, fileName= "menu.csv"):
        # already set default b/c no user input and it is the same file
        self.fileName = fileName

        # dictionary containing all menu items from the menu
        # keys are str representing types of the menu item
        # values are list of MenuItem objects
        # make an empty dictionary
        self.menuItemDictionary = {}

        # loop through the MENU_ITEM_TYPES to get the keys as the type
        # food object lists will be added as values to the appropriate keys
        for foodType in Menu.MENU_ITEM_TYPES:
            self.menuItemDictionary[foodType] = []

        fileObj = open(fileName, "r")
        for line in fileObj:
            line = line.strip()
            menuList = line.split(",")
            # want to have the format of --> type: rest of 3 attributes
            # rest of 3 attributes need to create a MenuItem object first
            menuItemObj = menuList[0],menuList[2],menuList[3]
            self.menuItemDictionary[menuList[1]].append(menuItemObj)
            # self.menuItemDictionary[menuList[1]] = menuList[0],menuList[2],menuList[3]
        fileObj.close()

    # fxn: getMenuItem
    # parameter 1: str representing type of menu item (one of four in MENU_ITEM_TYPES)
    # parameter 2: int representing index position of a certain menu item
    # return: MenuItem object from dictionary
    # side effect: none
    # get correct MenuItem from dictionary using its type and index position in the list of items
    def getMenuItem(self, menuItemType, menuPosition):
        correctItemObj = self.menuItemDictionary[menuItemType][menuPosition]

        return correctItemObj

    # fxn: printMenuItemsByType
    # parameter: str representing type of menu item (one of four listed in MENU_ITEM_TYPES)
    # return: none
    # side effect: print
    # displays header w/ type of menu items followed by numbered list of all menu items of that type
    def printMenuItemsByType(self, menuItemType):
        allItemObj = self.menuItemDictionary[menuItemType]
        upperMenuItemType = menuItemType.upper()
        print("\n----- " + upperMenuItemType + " -----")
        for num in range(len(allItemObj)):
            allItemObj = self.menuItemDictionary[menuItemType][num]
            itemName = allItemObj[0]
            itemMenuType = menuItemType
            itemPrice = allItemObj[1]
            itemDesc = allItemObj[2]
            fullItem = MenuItem(itemName,itemMenuType,itemPrice,itemDesc)
            # make sure all ints are str
            print(str(num), ")", fullItem)

    # fxn: getNumMenuItemsByType
    # parameter: str representing type of menu item (one of four listed in MENU_ITEM_TYPES)
    # return: int representing num of MenuItems of the input type
    # side effect: none
    # provides the len of the value for the key in dictionary
    def getNumMenuItemsByType(self, menuItemType):
        lenOfItemType = len(self.menuItemDictionary[menuItemType])
        return lenOfItemType
