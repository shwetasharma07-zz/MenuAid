
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


fruit = (
    'apple',
    'pear',
    'orange'
)




dictionary = dict()
dictionary = dict.fromkeys(meat,'meat')
dictionary.update(dict.fromkeys(fruit, 'fruit'))




def simplify(ingredient):
    return dictionary.get(ingredient, "NOT FOUND")



print(simplify('pear'))
