from Menu_Analyser import *

class Menu:
    
    

   
    ### would return the Str representation of the names of the Dishes in a menu Text file.
    def getDishNamesListFromTxt(menuTextStr):
        return menuTextStr

    ### reads a .txt file and returns a String.
    def getStrFromTextFile(filePath):
        textFile = ropen(filePath, 'w')
        menuString = textFile.read()
        print(menuString)


    def __init__(self, menuTextFilePath):
        print("Menu constructor with a text-file menu as argument.")

        #listOfDishNames = processMenuImage(menuTextFilePath)
        print(menuTextFilePath)

        

        listOfDishNames = self.getDishNamesListFromTxt(menuTextFilePath)


        self.dishes = createDishList(listOfDishNames)






