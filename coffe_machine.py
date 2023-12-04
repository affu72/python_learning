# Print report
# Check resources sufficient
# Process coins
# Check transaction succesful?
#  make coffee  -> update resources
#  refund amount if not sufficient to make selected coffee

requirements = {"water": 600, "coffee": 100, "milk": 200}

MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18, "milk": 45},
        "cost": 100,
    },
    "latte": {
        "ingredients": {
            "water": 100,
            "coffee": 38,
        },
        "cost": 200,
    },
    "cappuccino": {
        "ingredients": {
            "water": 150,
            "coffee": 28,
        },
        "cost": 300,
    },
}


def check_is_res_suff(drink_choice):
    drink = MENU[drink_choice]
    milk = drink["ingredients"]["milk"]
    water = drink["ingredients"]["water"]
    coffee = drink["ingredients"]["coffee"]

    if (
        requirements["milk"] >= milk
        and requirements["water"] >= water
        and requirements["coffee"] >= coffee
    ):
        return True
    else:
        return False


def print_report():
    print("Here is the list of available resources: ")
    for key in requirements:
        print(f"{key}: {requirements[key]} ")


profit = 0
is_on = True
while is_on:
    choice = input("What would you like? (espresso, latte, cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print_report()
    else:
        if check_is_res_suff(choice):
            amount_50 = int(input("Insert 50 rupees notes: "))
            amount_20 = int(input("Insert 20 rupees notes: "))
            amount_10 = int(input("Insert 10 rupees notes: "))

            total_amount = amount_50 * 50 + amount_10 * 10 + amount_20 * 20

            if total_amount >= MENU[choice]["cost"]:
                change = total_amount-MENU[choice]['cost'] if total_amount-MENU[choice]['cost'] >0 else None
                print(f"Yeah! your coffee is ready {'' if change=='None' else {change}}")
