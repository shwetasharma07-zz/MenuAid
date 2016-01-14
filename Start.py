from Menu import *
from Menu_Analyzer import *

print("\nProgram Start\n")

menuADT = Menu('menuTextFile.txt')




def processInstructionString(instr):
    if(instr.count(":")!=1):
        print("Please use correct instruction format! (instruction : items)")
        return ("none", "none")
    result = instr.split(":")
    result[0] = result[0].replace(" ", "").lower()
    result[1] = result[1].strip().lower()
    result[1] = result[1].split(",")
    for item in result[1]:
        item = item.lower().strip()
    return result


# The instruction is a list. The first element, instr[0] represents the command, 
#while the second part, instr[1], is also a list, and represents the items related to the instruction.
def processInstruction(instr):
    print("Instruction:\t"+str(instr))
    #return a list of all the dish objects with containing the given items (either names or ingredients)
    
    if(instr[0]=="findall"):
        result = list()
        for dish in menuADT.dishes:
            for element in instr[1]:
                if(dish.contains(str(element))):
                    result.append(dish)
        print(result)
        return result     
        
    elif(instr[0]=="ingredients"):
        for dishName in instr[1]:
            result = menuADT.getDish(dishName)
            if(result==-1):
                print("Dish not found!")
                return
        print(menuADT.getDish(dishName).ingredients)
    
    elif(instr[0]=="removeall"):
        result = menuADT.dishes
        for dish in menuADT.dishes:
            for element in instr[1]:
                if(dish.contains(str(element))):
                    result.remove(dish)
        print(result)
        return result

    elif(instr[0]=="recipefor"):
        for nameOfRecipe in instr[1]:
            print(getIngredientsFromName(nameOfRecipe))
        
    elif(instr[0]=="add"):
        for nameOfRecipe in instr[1]:
            print(getIngredientsFromName(nameOfRecipe))           
            for dishName in instr[1]:
                newDish = Dish(dishName, getIngredientList(dishName))
                menuADT.dishes.append(newDish)

print("The Recognized dishes in this menu are: \t" + str(menuADT.dishes))
instruction = input("Please enter an instruction.\n")
while(instruction != "exit"):

    print(str(menuADT.dishes))
    processInstruction(processInstructionString(instruction))
        
    
    print("The Recognized dishes in this menu are: \t" + str(menuADT.dishes))
    instruction = input("Please enter an instruction.\n")
print("\n\n\nProgram END")
    
        
