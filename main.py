import difflib


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0
def resources_checker():
    # resource_values = input("Type 'report' to check the current resource values: ").lower()
    if users_pick == "report":
       print(f"Water: {resources["water"]}ml")
       print(f"Milk: {resources["milk"]}ml")
       print(f"Coffee: {resources["coffee"]}g")
       print(f"Money: ${profit}")
    # elif users_pick == "report":
    #     print(f"Water: {resources["water"]}ml")
    #     print(f"Milk: {resources["milk"]}ml")
    #     print(f"Coffee: {resources["coffee"]}g")
    #     print(f"Money: ${profit}")



# print(resources_checker())

def is_resource_sufficient(order_ingredients):
    is_enough = True
    for items in order_ingredients:
        if order_ingredients[items] >= resources[items]:
            print(f"Sorry there is not enough {items}.")
            is_enough = False
    return is_enough

def process_coins():
    print("Please insert coins")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
   if money_received >= drink_cost:
       change = round(money_received - drink_cost, 2)
       print(f"Here is your change of ${change}")
       global profit
       profit += drink_cost
       return True
   else:
       print("sorry that is not enough money. Money refunded")
       return False

def make_coffee(drink_name, order_ingredients):
    for items in order_ingredients:
        resources[items] -= order_ingredients[items]
    print(f"Here is your {drink_name}")









is_on = True


valid_orders = {"latte", "cappuccino", "espresso", "report"}
while is_on:
    users_pick = input("What would you like? (Espresso/Latte/Cappuccino): ").lower()
    if users_pick not in valid_orders:
        closet_match = difflib.get_close_matches(users_pick, valid_orders, n=1)
        if closet_match:
            print(f"Did you mean {closet_match[0].capitalize()}? Please check your spelling")
            users_pick = input("What would you like? (Espresso/Latte/Cappuccino): ").lower()
    if users_pick == "report":
        print(resources_checker())
    if users_pick not in valid_orders:
        print("Sorry, This is a Coffee Machine. You can only order an Espresso, a Latte or a Cappuccino")
    else:
        print(f"you have chosen {users_pick.capitalize()}")
    if users_pick == "off":
        is_on = False
    else:
        drink = MENU[users_pick]
        print(drink)
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(users_pick, drink["ingredients"])






