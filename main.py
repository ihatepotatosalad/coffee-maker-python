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

def make_coffee():

    def call_report():
        print(f'water left: {machine_water}')
        print(f'milk left: {machine_milk}')
        print(f'coffee left: {machine_coffee}')
        print(f'money made: {machine_money}')

    # money
    quarter=.25
    dime = .10
    nickel=.05
    penny=.01
    in_session = True
    
    machine_water = resources["water"]
    machine_milk = resources["milk"]
    machine_coffee = resources["coffee"]
    machine_money=0
    while in_session:
        user_choice=''
        while user_choice not in MENU: 
            user_choice = input('What would you like? (espresso/latte/cappuccino): ')
            if user_choice == 'report':
                call_report()
            
            
                
        quarter_choice = int(input('how mamy quarters: '))
        dime_choice = int(input('how mamy dime: '))
        nickel_choice = int(input('how mamy nickel: '))
        penny_choice = int(input('how mamy pennies: '))

        total_coins = float(quarter*quarter_choice) + float(dime*dime_choice)+float(nickel*nickel_choice)+float(penny*penny_choice)
        purchase_compelete=True
        if not total_coins  >= MENU[user_choice]["cost"]:
                print('you dont have enough money, money refended')
                purchase_compelete=False
        elif not machine_water >= MENU[user_choice]["ingredients"]["water"]:
            purchase_compelete=False
            print('Add more water')
        elif not machine_coffee >= MENU[user_choice]["ingredients"]["coffee"]:
            purchase_compelete=False
            print('Add more coffee')
        elif 'milk' in MENU[user_choice]["ingredients"]:
            if not machine_milk >= MENU[user_choice]["ingredients"]["milk"]:
                purchase_compelete=False
                print('Add more milk')
        if purchase_compelete:
            print('purchase complete')
            change= round(total_coins - MENU[user_choice]['cost'],2)
            machine_water -= MENU[user_choice]['ingredients']['water']
            if 'milk' in MENU[user_choice]["ingredients"]:
                machine_milk -= MENU[user_choice]['ingredients']['milk']
            machine_coffee -= MENU[user_choice]['ingredients']['coffee']
            machine_money += MENU[user_choice]['cost']
            print(f'Change: {change}')


make_coffee()


