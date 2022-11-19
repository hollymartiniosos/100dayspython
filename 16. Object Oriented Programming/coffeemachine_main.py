from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_on = True
print("Welcome to the Coffee Machine!")

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while machine_on:
    coffee_of_choice = input(f'What would you like? {menu.get_items()} ')
    
    if coffee_of_choice == "off":
        machine_on = False
    elif coffee_of_choice == "report":
        coffee_maker.report()
        money_machine.report()    
# Szuka wszystkich danych o wybranej kawie   
    else: 
        drink = menu.find_drink(coffee_of_choice)  
    

# Wybiera tylko składniki potrzebne do zrobienia kawy i ceny kawy   
     
 
        # Wrzucanie monet i sprawdzanie czy wystarczy na zrobienie kawy

        if coffee_maker.is_resource_sufficient(drink):  
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
            

 