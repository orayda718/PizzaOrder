# Name: Orayda Shagifa
# Description: Pizza Ordering System, Program takes user's pizza order, calculates the price of each pizza, tax, and total, then prints receipt
#Date: 10.26.2022

# function to print out the entire receipt
def generateReceipt(pizzaOrder):
    pizzaCost = 0       # base cost of pizza
    totalCost = 0       # total cost of pizza
    toppingCost = 0     # cost of toppings

    if len(pizzaOrder) == 0:     # checks if pizza tuple is empty
        print("You did not order anything")     # executes if user enters no or q

    else:
        print("Your order:")
        for i in range(len(pizzaOrder)):
            if pizzaOrder[i][0] == 'S':     # small pizza price
                pizzaCost = 7.99
                if len(pizzaOrder[i][1]) > 3:   # small pizza extra topping price
                    toppingCost = 0.50
                else:
                    toppingCost = 0     # resets topping cost
            elif pizzaOrder[i][0] == 'M':     # medium pizza price
                pizzaCost = 9.99
                if len(pizzaOrder[i][1]) > 3:   # medium pizza extra topping price
                    toppingCost = 0.75
                else:
                    toppingCost = 0
            elif pizzaOrder[i][0] == 'L':     # large pizza price
                pizzaCost = 11.99
                if len(pizzaOrder[i][1]) > 3:   # large pizza extra topping price
                    toppingCost = 1.00
                else:
                    toppingCost = 0
            elif pizzaOrder[i][0] == 'XL':     # extra large pizza price
                pizzaCost = 13.99
                if len(pizzaOrder[i][1]) > 3:   # extra large pizza extra topping price
                    toppingCost = 1.25
                else:
                    toppingCost = 0

            print("Pizza %d: %s 				  %.2f" % ((i + 1), pizzaOrder[i][0], pizzaCost))   # prints pizza size and base cost

            for x in range(len(pizzaOrder[i][1])):  # prints toppings
                print("-", pizzaOrder[i][1][x])
            if toppingCost != 0:    # prints extra toppings
                for y in (range(len(pizzaOrder[i][1]) - 3)):
                    print("Extra Topping (%s)		   %.2f" % (pizzaOrder[i][0], toppingCost))

            toppingCost *= (len(pizzaOrder[i][1]) - 3)  # calculates topping cost
            totalCost += toppingCost + pizzaCost    # calculates total cost before tax

        tax = round((totalCost * 0.13), 2)  # calculates tax
        totalCost += tax    # calculates total cost with tax

        print("Tax:					   %.2f" % tax)     # prints tax
        print("Total:					  %.2f" % totalCost)    # prints total cost
