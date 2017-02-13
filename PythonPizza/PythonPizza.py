#Project: CIS 177 WEEK 4 PROJECT
#Project Location: projects\cis177\PythonPizza
#File: pythonpizza.py
#Purpose: Take a customer's order for pizza, first ask for the size
#         Then ask for the pizza toppings, and generate a price
#Revision: 1.0 / 13 FEB 2017
#Created: 13 FEB 2017
#Author: Rick Miller <rick@rickthegeek.com>

# This is a dict to hold the toppings list. As the customer adds items to his pizza,
# we will remove the chosen toppings from the dict.
availableToppings = {'cheese' : 1.00, 'pepperoni' : .50, 'sausage' : .50, 'avocado' : 1.00, 'onion' : .25, 'peppers' : .25}
pizzaPrice = 0.00 # Running total of the price of the pizza

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
print(sizeCode)
