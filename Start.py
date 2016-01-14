from Menu import *
from Menu_Analyzer import *

print("\nProgram Start\n")

menuADT = Menu('menuTextFile.txt')
print("The Recognized dishes in this menu are: \t" + str(menuADT.dishes))


def processInstructionString(instr):
    print(instr)
    result = instr.split(":")
    result[1] = result[1].split(",")
    print(result)
    return result


# The instruction is a list. The first element, instr[0] represents the command, 
#while the second part, instr[1], is also a list, and represents the items related to the instruction.
def processInstruction(instr):
    if(instr[0]=="findAll"):
        menuADT.findAll(instr[1])
    elif(instr[0]=="ingredients"):
        for dishes in instr[1]:
            print(menuADT.getDish(instr[1]).ingredients)




instruction = input("Please enter an instruction.\n")
while(instruction != "exit"):
    
    processInstruction(processInstructionString(instruction))
    instruction = input("Please enter an instruction.\n")
    
    
print("\n\n\nProgram END")
    
        
