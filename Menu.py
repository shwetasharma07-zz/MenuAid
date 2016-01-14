from Menu_Analyzer import *

class Menu:
    
    ### would return the Str representation of the names of the Dishes in a menu Text file.
    def getDishNamesListFromTxt(menuTextStr):
        return menuTextStr.split(",")

    ### reads a .txt file and returns a String.
    def getStrFromTextFile(filePath):
        textFile = open(filePath)
        menuString = textFile.read()
        #print(menuString)
        return menuString
    
    def getDishNamesListFromString(menuString):
        listOfNames = menuString.split(",")
        return listOfNames


    def __init__(self, filePath):
        print("Menu constructor\n")
        self.filePath = str(filePath)
        self.menuString = Menu.getStrFromTextFile(self.filePath)
        #listOfDishNames = processMenuImage(menuTextFilePath)
        self.listOfDishNames = Menu.getDishNamesListFromString(self.menuString)
        self.dishes = createDishList(self.listOfDishNames)
        
        
    def __str__(self):
        return str(self.dishes);

    def __repr__(self):
        return str(self.dishes);
    
    def printIngredients(self):
        for dish in self.dishes:
            print(dish.dishName)
            print(dish.ingredients)
            
            
    def getDish(self, name):
        name = str(name)
        for dish in self.dishes:
            if(dish.dishName.strip().lower() == name.strip().lower()):
                return dish
        print("Dish not found!")
        return -1
     
                   


