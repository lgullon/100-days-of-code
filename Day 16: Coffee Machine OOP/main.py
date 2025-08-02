from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

continue_ordering = True
while continue_ordering:
    # prompt user
    order = input(f"What would you like? ({menu.get_items()}): ")

    # turn off coffee machine
    if order == "off":
        print("Shutting down . . . ")
        break

    # print report
    if order == "report":
        coffee_maker.report()
        money_machine.report()
        continue

    # check resources are sufficient
    drink = menu.find_drink(order)
    sufficient = coffee_maker.is_resource_sufficient(drink)
    if not sufficient:
        continue

    # process coins
    money_machine.make_payment(drink.cost)

    # make a coffee
    coffee_maker.make_coffee(drink)
