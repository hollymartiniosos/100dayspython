
"""
Types of hot flavorus:  
espresso    $1.5  50 ml water   18g coffee
latte       $2.5  200ml water   24g coffee   150ml milk
cappuccino  $3.0  250ml water   24g coffee   100ml milk

Starting resources:

water  300ml
milk   200ml
coffee 100g

Coins types:

Penny   1 cent      0.01
Nickel  5 cents     0.05
Dime    10 cents    0.10
Quarter 25 cents    0.25

"""
from art import coffee_emoji

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

machine_on = True
print("Welcome to the Coffee Machine!")

while machine_on == True:
    coffee_of_choice = input('What would you like? espresso/latte/cappuccino  ')

    if coffee_of_choice == "off":
        machine_on = False
    elif coffee_of_choice == "report":
        print(f' The current ingredients available: \n water: {resources["water"]} \n milk: {resources["milk"]}  \n coffee: {resources["coffee"]} \n money: ${profit}')    
# Szuka wszystkich danych o wybranej kawie   
    else: 
        make_coffee = True
        all_data = MENU[coffee_of_choice]   
    # print(all_data)

# Wybiera tylko składniki potrzebne do zrobienia kawy i ceny kawy   
        ingred = all_data["ingredients"]
        price = all_data["cost"]
    # print(ingred)   

        
#Sprawdzenie czy wszystkich składników wystarczy
        if int(resources["water"])  < int(ingred["water"]):
            print("Sorry there is no enough water.")
            make_coffee = False
        elif int(resources["milk"]) < int(ingred["milk"]):
            print("Sorry there is no enough milk.")
            make_coffee = False

        elif int(resources["water"]) < int(ingred["water"]):
            print("Sorry there is no enough coffee.")
            make_coffee = False    
        else:
            print("There is enough ingredients to make your coffee.")
        

        # Wrzucanie monet
        if make_coffee:
            print("Please insert coins.")    
            quarters = int(input("How many quarters?: ")) 
            dimes = int(input("How many dimes?: ")) 
            nickles = int(input("how many nickles?: ")) 
            pennies = int(input("how many pennies?: ")) 

#Liczenie ile pieniędzy zostało wrzuconych
            money_inserted = quarters * 0.25 + dimes * 0.10 + nickles *0.05 + pennies *0.01

# Sprawdzenie czy wystarczy pieniędzy na wybraną kawę
            if money_inserted >= price:
                change = round(money_inserted - price, 2)
                print(f'Here is your change ${change} and {coffee_of_choice}. Enjoy! {coffee_emoji} ')

                resources["water"] = int(resources["water"]) - int(ingred["water"])
      
                resources["milk"] = int(resources["milk"]) - int(ingred["milk"])
          
                resources["coffee"]  = int(resources["coffee"]) - int(ingred["coffee"])
                profit += price

            else:
                print(f'You insterted ${money_inserted}, {coffee_of_choice} costs ${price}. Skąpy kutasie!')    
    




        









    

 




   






