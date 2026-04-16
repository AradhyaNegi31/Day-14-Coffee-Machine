import data
from data import Resources


machine_on = True

while machine_on:
    user_choice = input("What would you like to have sir?\n1. Latte\n2. Caippuccino\n3. Espresso\n(OR)\n Would you like to check resources?: ")
    
    if user_choice.lower() == "resources":
        print("Milk: {Resources[milk]} ml")
        print("Coffee: {Resources[coffee]} gm")
        print("Water: {Resources[water]} ml")

    elif user_choice.lower() == "off":
        machine_on = False
        print("Thanks for trying out the machine SWICHING OFF")

    elif user_choice in data.Menue:
        drink = data.Menue[user_choice]
        can_make = True
        for item in drink["ingredient"]:
            if drink["ingredient"][item] > Resources[item]:
                print(f"Sorry there is not enough {item} currently.")
                can_make = False

        if can_make:
            print("Please insert coins.")
            quarters = int(input("How many quarters?: ")) * 0.25
            dimes = int(input("How many dimes?: ")) * 0.10
            nickels = int(input("How many nickels?: ")) * 0.05
            pennies = int(input("How many pennies?: ")) * 0.01

            total_inserted = quarters + dimes + nickels + pennies

            if total_inserted >= drink["cost"]:
                change = round(total_inserted - drink["cost"], 2)
                print(f"Here is ${change} in change.")
                print(f"Here is your {user_choice}. Enjoy your drink")

                for item in drink["ingredient"]:
                    Resources[item] -= drink["ingredient"][item]

            else:
                print("Sorry that's not enough money. Money refunded.")
    elif user_choice == "update":
        milk = int(input("Enter milk to add in inventory: "))
        water = int(input("Enter water to add in inventory: "))
        coffee = int(input("Enter coffee to add in inventory: "))
        Resources[water] += water
        Resources[milk] += milk
        Resources[coffee] += coffee

    else:
        print("Invalid choice. Please select espresso, latte, or cappuccino.")

        
