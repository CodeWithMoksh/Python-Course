# Greeting to the customer
print("Welcome to our Bhukkad Restaurent")

# Making the List of the menu
menu = {
    "pasta": 40,
    "burger": 50,
    "pizza": 100,
    "maggi": 55,
    "coffee": 20,
    "mocktails": 30,
    "shake": 120,
    "momos": 40
}

# Displaying the menu to the customer
print("Here is our menu: \nPasta: 40, \nBurger: 50, \nPizza: 100, \nMaggi: 55, \nCoffee: 20, \nMocktails: 30, \nShake: 120, \nMomos: 40 ")

# Taking the Order
order_1 = input("What do you want to order sir/madam: ")

# Calculating the Bill
bill = 0

if(order_1.lower() in menu):
    print(f"Okay your {order_1} are getting ready")

    # Adding the value of the order to the bill
    bill += menu[order_1.lower()]

    # Asking for something else wanted
    some_more = input("Do you want something else: ")

    if(some_more.lower() == "yes"):
        order_2 = input("Nice to Hear that what would we that precious dish: ")

        if(order_2.lower() in menu):
            print(f"Noted!!! Your {order_2} is on the way")
            bill += menu[order_2.lower()]
            print(f"Your total bill is {bill}")
        else:
            print(f"Sorry but the dish you are wanting is not available with us. Your final bill is {bill}")

    elif(some_more.lower() == "no"):
        print(f"No problem!! Your order is on the way")
        print(f"The total bill is {bill}")
    
    else:
        print("Sorry we are unable to understand what you are talking about!!")

else:
    print(f"Sorry but the dish you are wanting is not available with us.")
