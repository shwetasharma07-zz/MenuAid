## categories

meat = (
    'beef',
    'chicken',
    'turkey',
    'lamb',
    'pork',
    'sausage'
)

fruit = (
    'apple',
    'pear',
    'orange'
)

lactose = (
    'milk',
    'cream',
    'cheese',
    'yogurt'
)


categories = {meat,fruit,lactose}

dictionary = dict()
#for category in categories:
#    dictionary.update(dict.fromkeys(category,))
dictionary = dict.fromkeys(meat,'meat')
dictionary.update(dict.fromkeys(fruit, 'fruit'))
dictionary.update(dict.fromkeys(lactose, 'lactose'))
#dictionary.update(dict.fromkeys(fruit, 'fruit'))



def match(ingredient , category):
    print (ingredient)
    ingredient = " ".join((ingredient.replace("  ","")).split(" "))
    print (ingredient)
    for words in ingredient:
        if(dictionary.get(ingredient,ingredient)==category):
            return 1
    return 0


def simplifyMenu(menuString):
    result = ",".join(menuString).split(",")
    result = " and ".join(result).split(" and ")
    result = "with".join(result).split("with")
    result = "with".join(result).split("with")
    for entry in result:
        entry = entry.strip()  
    return result



if(match(" apple sunday  ","fruit")):
    print("match!")
else:
    print("no match!")