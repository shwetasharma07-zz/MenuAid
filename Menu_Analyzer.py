import json
import requests

####### Shweta! --> Head over to the end of the document for the main program and the options. I suggest you collapse all also. ###################

headers = {'accept': 'application/json'}
apiKey = "3eSo7F2R4Z7ID4E6vT7u79S4c8qRLFk7"

## simple class that represents an ingredient in a dish.
class Ingredient:
    
    def __init__(self, itemDict):
        
        #print("creating new object")
        self.name = str(itemDict['Name'])
        

    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name

##collection of ingredients. A Menu is a collection of Dish objects.
class Dish:

    def __init__(self, dishName, ingredients):
        self.dishName = str(dishName)
        self.ingredients = ingredients

    def __str__(self):
        if(self.ingredients==-1):
            return "\n"+self.dishName + ":\n" + "NO RECIPE FOUND"+"\n"
        return "\n"+self.dishName + ":\n" + str(self.ingredients)+"\n"

    def __repr__(self):
        if(self.ingredients==-1):
            return "\n"+self.dishName + ":\n" + "NO RECIPE FOUND"+"\n"
        return "\n"+self.dishName + ":\n" + str(self.ingredients)+"\n"



## returns a list of ingredients given a RecipeID
def getIngredientsFromRecipeID(dishID):
    
        
    #url url used to look up the ingredients given a dishID.
    url = "http://api.bigoven.com/recipe/" + str(dishID) + "?api_key=" + apiKey

    
    #print("INGREDIENT SEARCH URL:\t"+url)
    
    #gets a JSON response from the given URL.
    response = requests.get(url, headers=headers)
    
    #(optional) get the header type
    #print("HEADER TYPE:\t"+response.headers['content-type'])
    
    
    #make a dictionnary from the json response.
    data = response.json()
    
    #create an empty list
    ingredientList = list()

    # Since the Ingredients are actually dictionnaries, we must iterate over each element of the dictionnary.
    for entry in data['Ingredients']:
        newIngredient = Ingredient(entry)
        ingredientList.append(newIngredient)
        

    #print("INGREDIENTS for dish with RecipeID "+str(dishID)+" are : \t"+ str(ingredientList))

    return ingredientList

def getDishIdFromName(dishName):
    
    #Used to find the RecipeID of a given Dish name.
    url = "http://api.bigoven.com/recipes?pg=1&rpp=25&title_kw="+ dishName.lower() + "&api_key="+apiKey
    
    #print("dish SEARCH URL:\t"+url)

    #gets a JSON response from the given URL.
    response = requests.get(url, headers=headers)
    
    #(optional) get the header type
    #print("HEADER TYPE:\t"+response.headers['content-type'])
    
    
    #make a json object from the response.
    data = response.json()

    #return -1 if there are no search results for the given dish name.
    if(data['ResultCount']==0):
        #print("There are no dishes with that name")
        return -1;


    #print(data)
    #print("RECIPE ID RESULT FOR STR "+dishName+": \t"+str(data['Results'][0]['RecipeID']))

    return data['Results'][0]['RecipeID']


## returns the ingredients required for this recipe
def getIngredientList(dishName):

    id = getDishIdFromName(dishName)
    if(id == -1):
        print("Cannot find a Recipe for "+ dishName+" in BigOven's database")
        ingredients = -1
    else:
        ingredients = getIngredientsFromRecipeID(id)
        #print(ingredients)
    return ingredients


#comment out to use User Input.

#dishName = input("Please enter a Recipe Name: ")
#getList(dishName)

def createDishList(listOfDishNames):

    #for now its a list. TODO: make it the right data structure.
    Menu = list()

    for dishName in listOfDishNames:
        newDish = Dish(dishName, getIngredientList(dishName))
        Menu.append(newDish)
    return Menu;





   

