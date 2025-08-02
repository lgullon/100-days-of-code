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

def print_resources(money_saved):
    """ Prints the amount of each resource in the coffee machine: water, milk, coffee, and money """
    return (f"Water: {resources["water"]}ml\n"
            f"Milk: {resources["milk"]}\n"
            f"Coffee: {resources["coffee"]}\n"
            f"Money: ${money_saved} \n")

def check_ingredients(ordered):
    drink = MENU[ordered]
    needed_ingredients = drink["ingredients"]
    enough = True
    for ingredient in needed_ingredients:
        if resources[ingredient] < needed_ingredients[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            enough = False
    return enough

def use_ingredients(ordered):
    global resources
    drink = MENU[ordered]
    needed_ingredients = drink["ingredients"]
    for ingredient in needed_ingredients:
        resources[ingredient] -= needed_ingredients[ingredient]



money = 0
order_again = True
while order_again:
    # prompt user
    order = input("What would you like? (espresso/latte/cappuccino): ")

    # to turn off coffee machine
    if order == 'off':
        break

    # print the report
    if order == 'report':
        print(print_resources(money))
        continue

    # check sufficient resources
    able = check_ingredients(order)
    if not able:
        continue

    cost = MENU[order]["cost"]
    print(f"Please insert ${cost} in coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    total_paid = (quarters * .25) + (dimes * .1) + (nickles * .05) + (pennies * .01)

    if total_paid > cost:
        change = total_paid - cost
        print(f"You entered ${total_paid}. Here is ${round(change, 2)} in change!")
    elif cost < total_paid:
        print("Sorry that's not enough money. Money refunded.")
        continue


    money += cost
    use_ingredients(order)

    print(f"Here is your {order}. Enjoy!\n")
