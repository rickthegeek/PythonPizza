#Project: CIS 177 WEEK 4 PROJECT
#Project Location: projects\cis177\PythonPizza
#File: pythonpizza.py
#Purpose: Take a customer's order for pizza, first ask for the size
#         Then ask for the pizza toppings, and generate a price
#Revision: 1.0 / 13 FEB 2017
#Created: 13 FEB 2017
#Author: Rick Miller <rick@rickthegeek.com>

# This is a dict to hold the toppings list. As the customer adds items to his pizza,
# we will add the price of the chosen toppings from the dict.
availableToppings = {'C - cheese' : 1.00, 'R - pepperoni' : .50, 'S - sausage' : .50, 'A - avocado' : 1.00, 'O - onion' : .25, 'P - peppers' : .25}
pizzaPrice = 0.00 # Running total of the price of the pizza
toppingCode = '' # This will hold the user's topping choice
numToppings = 0 # This will hold the number of toppings the user wants
toppingPrice = 0.00 # This will hold the total topping cost (quantity times price)

# First, introduce ourlselves to the user and let the user choose their pizza
print('Welcome to Python Pizza!')
print('First, tell me what size of pizza you want.\n\n')
print('S - Small pizza:    $6.00')
print('M - Medium pizza:   $8.00')
print('L - Large pizza:   $10.00\n\n')
sizeCode = input('So, what will it be? ')
# We only care about the first character, 'L', 'M', or 'S', so let's drop the rest of the string
sizeCode = sizeCode[0]
# and convert to lower case, to make comparisions easier....
sizeCode = str.lower(sizeCode)
# now, if user chose a small or a large, we will add that to the price, or if user enters anything else
# the user will get a medium
if (sizeCode == 'l') or (sizeCode == 's'):
    if sizeCode == 'l':
        print('Great! one large pie comin\' up!\nThat will be ten bucks!\n')
        pizzaPrice = 10.00
    else:
        print('Okay, a small pizza just for you!\nSix dollars so far...\n')
        pizzaPrice = 6.00
else:
    sizeCode = 'm' # user either entered 'm' or something else, which we change here to be 'm'
    print('One medium pizza... \nFor you, just $8')
    pizzaPrice = 8.00
numToppings = int(input('How many toppings would you like? ')) # find out how many toppings the user wants
while numToppings > 0: # loop through for each topping choice, as long as there is at least one choice left
    print('\nPizza total price so far: $%3.2f' % pizzaPrice)
    print(numToppings, 'topping choices left to go\n')
    print('Available Toppings:\n') # display the menu
    for toppingString in availableToppings:
        print(toppingString, ':\t\t$%3.2f ' % availableToppings[toppingString]) # prompt user for a topping choice
    toppingCode = input('\nChoose a topping: ')
    toppingCode = toppingCode[0] # again, only need the first letter
    toppingCode = str.lower(toppingCode) # convert to lower case
    if toppingCode in ['c', 'r', 's', 'a', 'o', 'p']: # check if the user entered a valid choice
        for toppingLookup in availableToppings:
            if str.lower(toppingLookup[0]) == toppingCode:
                print(toppingLookup, ' : \t$%3.2f' % availableToppings[toppingLookup], 'each.') # print the user's choice
                toppingQuantity = float(input('\nHow many of this topping do you want? ')) # ask how many of the topping the user wants
                toppingPrice = availableToppings[toppingLookup] * toppingQuantity
                pizzaPrice += toppingPrice # add the topping price to the pizza total
        numToppings -= 1 # deduct one topping if a valid choice was made
    else: # not a valid topping choice
        print('\nSorry, not a valid topping, try again') # tell the user it's an invalid choice then let them try again
print('Final pizza order total: $%3.2f' % pizzaPrice)

    


