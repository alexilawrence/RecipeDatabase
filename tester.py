'''with open('Steak_Ingredients.txt', 'r') as f:
    ingredients = f.read()
    quantities = []
    components = []
    for i in ingredients.split(sep='\n'):
        splitted = i.split(sep="|")
        quantities.append(splitted[0].strip())
        components.append(splitted[1].strip())
        
    print(quantities)
    print(components)'''
    
a = "hello to all of you! \t You look very nice."

import secrets

print(secrets.token_hex())