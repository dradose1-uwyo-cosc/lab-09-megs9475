# Meghan Longua
# UWYO COSC 1010
# Submission Date: 11/13/2024
# Lab 09
# Lab Section: 15
# Sources, people worked with, help given to: Abby Ferguson
# Your
# Comments
# Here

# Classes
# For this assignment, you will be creating two classes:
# One for Pizza
# One for a Pizzeria


# You will be creating a Pizza class. It should have the following attributes:
# - Size
# - Sauce
# - Toppings, which should be a list
# You need to create one method that corresponds with each of the above attributes
# which returns the corresponding attribute, just the value.
# For the size and toppings attributes, you will need to have a method to set them.
# - For Size, ensure it is an int > 10 (inches)
#   - If it is not, default to a 10" pizza (you can store ten). These checks should occur in init as well.
# - For toppings, you will need to add the toppings.
#   - This method needs to be able to handle multiple values.
#   - Append all elements to the list.
# Create a method that returns the amount of toppings.
# In your __init__() method, you should take in size and sauce as parameters.
# - Sauce should have a default value of red.
# - Size will not have a default value; use the parameter with the same safety checks defined above (you can use the set method).
# Within __init__(), you will need to:
# - Assign the parameter for size to a size attribute.
# - Assign the parameter for sauce to the attribute.
# - Create the toppings attribute, starting off as a list only holding cheese.


# You will be creating a Pizzeria class with the following attributes:
# - orders, the number of orders placed. Should start at 0.
# - price_per_topping, a static value for the price per topping of 0.30.
# - price_per_inch, a static value of 0.60 to denote how much the pizza cost per inch of diameter.
# - pizzas, a list of all the pizzas with the last ordered being the last in the list.
# You will need the following methods:
# - __init__()
#   - This one does not need to take in any extra parameters.
#   - It should create and set the attributes defined above.
# - placeOrder():
#   - This method will allow a customer to order a pizza.
#     - Which will increment the number of orders.
#   - It will need to create a pizza object.
#   - You will need to prompt the user for:
#     - the size
#     - the sauce, tell the user if nothing is entered it will default to red sauce (check for an empty string).
#     - all the toppings the user wants, ending prompting on an empty string.
#     - Implementation of this is left to you; you can, for example:
#       - have a while loop and append new entries to a list
#       - have the user separate all toppings by a space and turn that into a list.
#   - Upon completion, create the pizza object and store it in the list.
# - getPrice()
#   - You will need to determine the price of the pizza.
#   - This will be (pizza.getSize() * price_per_inch) + pizza.getAmountOfToppings() * price_per_topping.
#   - You will have to retrieve the pizza from the pizza list.
# - getReceipt()
#   - Creates a receipt of the current pizza.
#   - Show the sauce, size, and toppings.
#   - Show the price for the size.
#   - The price for the toppings.
#   - The total price.
# - getNumberOfOrders()
#   - This will simply return the number of orders.


# - Declare your pizzeria object.
# - Enter a while loop to ask if the user wants to order a pizza.
# - Exit on the word `exit`.
# - Call the placeOrder() method with your class instance.
# - After the order is placed, call the getReceipt() method.
# - Repeat the loop as needed.
# - AFTER the loop, print how many orders were placed.


# Example output:
"""
Would you like to place an order? exit to exit
yes
Please enter the size of pizza, as a whole number. The smallest size is 10
20
What kind of sauce would you like?
Leave blank for red sauce
garlic
Please enter the toppings you would like, leave blank when done
pepperoni
bacon

You ordered a 20" pizza with garlic sauce and the following toppings:
                                                                  cheese
                                                                  pepperoni
                                                                  bacon
You ordered a 20" pizza for 12.0
You had 3 topping(s) for $0.8999999999999999
Your total price is $12.9

Would you like to place an order? exit to exit
"""


class Pizza:
    def __init__(self, size, sauce="red"):
        self.size = size if size >= 10 else 10
        self.sauce = sauce
        self.toppings = ["cheese"] 
    
    def check_size(self, size):
        self.size = size if size >= 10 else 10

    def pizza_size(self):
        return self.size
    
    def pizza_sauce(self):
        return self.sauce

    def extra_toppings(self, *toppings):
        self.toppings.append(toppings)
    
    def pizza_toppings(self):
        return self.toppings
    
    def amount_of_toppings(self):
        return len(self.toppings)

class Pizzeria:

    def __init__(self):
        self.orders = 0
        self.pizzas = []

    price_per_topping = 0.30
    price_per_inch = 0.60
    
    def placeOrder(self):
        try:
            size = int(input("Please enter the size of pizza you would like; it must be at least 10 inches: "))
        except ValueError:
            size = 10 
        
        sauce = input("Enter the sauce you would like or red sauce will be automatically added: ")
        if not sauce:
            sauce = "red"
        
        toppings = input("Enter the toppings you would like (make sure to put a space between each one): ").split()
        
        pizza = Pizza(size, sauce)
        if toppings:
            pizza.extra_toppings(*toppings)
        self.pizzas.append(pizza)
        self.orders += 1
    
    def getPrice(self, pizza):
        size_price = pizza.pizza_size() * Pizzeria.price_per_inch
        topping_price = pizza.amount_of_toppings() * Pizzeria.price_per_topping
        return size_price + topping_price
    
    def getReceipt(self, pizza):
        size_price = pizza.pizza_size() * Pizzeria.price_per_inch
        topping_price = pizza.amount_of_toppings() * Pizzeria.price_per_topping
        total_price = size_price + topping_price
        
        print("***Receipt***")
        print(f"Sauce: {pizza.pizza_sauce()}")
        print(f"Size: {pizza.pizza_size()} inches")
        print(f"Toppings: {', '.join(pizza.pizza_toppings())}")
        print(f"Price for size: ${size_price:.2f}")
        print(f"Price for toppings: ${topping_price:.2f}")
        print(f"Total price: ${total_price:.2f}")
    
    def getNumberOfOrders(self):
        return self.orders

def pizzeria_object():
    pizzeria = Pizzeria()
    
    while True:
        action = input("Do you want to order a pizza? Enter 'yes' or 'exit' to exit: ").lower()
        if action == 'exit':
            break
        elif action == 'yes':
            pizzeria.placeOrder()
            pizza = pizzeria.pizzas[-1]  
            pizzeria.getReceipt(pizza)
        else:
            print("Invalid input, please enter 'yes' to order or 'exit' to exit")
    
    print(f"Total number of orders: {pizzeria.getNumberOfOrders()}")

