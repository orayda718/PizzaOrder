# Name: Orayda Shagifa
# Description: Pizza Ordering System, Program takes user's pizza order, calculates the price of each pizza, tax, and total, then prints receipt
# Date: 10.26.2022

from pizzaReceipt import generateReceipt
pizzaOrder = []     # entire order list
pizza = ()          # pizza tuple, will store size and toppings
toppings = []       # toppings list
TOPPINGS = ('ONION', 'TOMATO', 'GREEN PEPPER', 'MUSHROOM', 'OLIVE', 'SPINACH', 'BROCCOLI', 'PINEAPPLE', 'HOT PEPPER', 'PEPPERONI', 'HAM', 'BACON', 'GROUND BEEF', 'CHICKEN', 'SAUSAGE')

order1 = input("Do you want to order a pizza? ")


# loops until user is done ordering pizzas
while order1.upper() != "NO" and order1.upper() != "Q" and order1.upper() != "":

    del pizza   # clears pizza tuple
    toppings.clear()    # clears topping choices

    size = input("Choose a size:  S, M, L, or XL: ")      # pizza size

    while size.upper() != 'S' and size.upper() != 'M' and size.upper() != 'L' and size.upper() != 'XL':     # checks if size is inputted correctly
        size = input("Choose a size:  S, M, L, or XL: ")  # replaces with correct size input

    print('Type in one of our toppings to add it to your pizza. To see the list of toppings, enter "LIST". '
          'When you are done adding toppings, enter "X"')
    toppingInput = input("")      # pizza topping

    while toppingInput.upper() != "X":  # asks for pizza topping until user enters 'x'

        if toppingInput.upper() == "LIST":
            print(TOPPINGS)     # prints list of toppings

        elif toppingInput.upper() in TOPPINGS:  # checks if input is valid/in the list of toppings
            print("Added", toppingInput.upper(), "to your pizza")
            toppings.append(toppingInput.upper())   # adds the valid topping to the topping list

        else:
            print("Invalid topping")    # input is not one of the topping choices or 'list', topping isn't added to order

        print('Type in one of our toppings to add it to your pizza. To see the list of toppings, enter "LIST". '
              'When you are done adding toppings, enter "X"')
        toppingInput = input("")

    pizza = (size.upper(), toppings.copy())    # creates pizza tuple
    pizzaOrder.append(pizza)    # appends the pizza to the pizza order list

    order1 = input("Do you want to continue ordering? ")    # asks user if they want to order another pizza

generateReceipt(pizzaOrder)     # calls function to print receipt from the pizzaReceipt.py file
