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
            
            
    def getDish(self, dishName):
        if(self.dishes.count(dishName)):
            return self.dishes.get(dishName)
        else:
            print("Dish not found!")
            return " "
     
    def findAll(items):
        result = list()
        for dish in self.dishes:
            for ingredient in dish:
                for item in items:
                    if(str(ingredient).count(item) > 0):
                        result.append(dish)
                        continue
        return result                        


