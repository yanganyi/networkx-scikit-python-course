# Task 1.3 - Ecommerce
# 1.3.1 is the original task
#  - implement 3 commands - buy, checkout and exit
#  - the buy command prompts for item name and quantity
#  - products, prices and quantity are predetermined, refer below
# 1.3.2 includes:
#  - taxation on the price
#  - "view" command for store inventory and price
#  - "remove" command to remove items from cart
#  - search command to find items in store (advanced: fuzzy search algorithm)
# 1.3.3 removes the need to maintain both pricing and inventory table (further building on 1.3.2)

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# used for different goodbye greetings depending on whether they bought anything
bought=False

storage={
    "Bread":    [0.42,69],
    "Milk":     [1.69,42],
    "Cheese":   [6.94,10]
}

cart={}

def buy():
    req=input("Enter the item and quantity you wish to purchase (item,qty): ")
    if len(req.split(",")) !=2:
        print("Invalid input")
        return
    item,qty=req.split(",")
    if item not in storage.keys():
        print("Invalid item")
        return
    try: qty=int(qty)
    except ValueError:
        print("Invalid quantity")
        return
    if qty>storage[item][1]:
        print("Not enough items")
        return
    storage[item][1]-=qty
    if cart.get(item): cart[item]+=qty
    else: cart[item]=qty
    bought=True

def checkout():
    total=0
    for item,qty in cart.items():
        total+=storage[item][0]*qty
        print(f"- {qty}x of {item} at {storage[item][0]}ea = {storage[item][0]*qty}")
    print(f"Your total is ${total:.2f}")
    cart.clear()

def view():
    for item,list in storage.items():
        print(f"{item} costs ${list[0]}ea, ",end="")
        print(f"{list[1]} left in stock")

def remove():
    req=input("Enter the item and quantity you wish to remove from cart (item,qty): ")
    if len(req.split(",")) !=2:
        print("Invalid input")
        return
    item,qty=req.split(",")
    if item not in storage.keys():
        print("Invalid item")
        return
    try: qty=int(qty)
    except ValueError:
        print("Invalid quantity")
        return
    if qty>storage[item][1]:
        print("Not enough items")
        return
    storage[item][1]+=qty
    if cart.get(item):
        if cart.get(item)<qty:
            print(f"Invalid quantity (your cart only has {cart.get(item)} {item})")
            return
        cart[item]-=qty
    else:
        print("Invalid quantity (your cart does not contain that item)")


def search():
    # not the best imple
    item=input("Enter the name of the item you want to search for: ")
    bre=fuzz.ratio(item,"Bread")
    mil=fuzz.ratio(item,"Milk")
    che=fuzz.ratio(item,"Cheese")
    if bre>mil and bre>che:
        print(f"The store still has {storage['Bread'][1]} bread in stock at {storage['Bread'][0]}ea, feel free to purchase!")
    elif mil>bre and mil>che:
        print(f"The store still has {storage['Milk'][1]} milk in stock at {storage['Milk'][0]}ea, feel free to purchase!")
    elif che>bre and che>mil:
        print(f"The store still has {storage['Cheese'][1]} cheese in stock at {storage['Cheese'][0]}ea, feel free to purchase!")
    else:
        print("The valid options are Bread, Milk and Cheese! Happy shopping!")

user_input="meow?"
while user_input!="exit":
    user_input=input("Enter a command (buy,checkout,view,remove,search,exit): ")
    if user_input=="buy":           buy()
    elif user_input=="checkout":    checkout()
    elif user_input=="view":        view()
    elif user_input=="remove":      remove()
    elif user_input=="search":      search()
    elif user_input!="exit":        print("Invalid command")
if bought: print("Thank you for shopping with us. Have a nice day!")
else: print("Sorry to see you go without buying anything! Hope to see you soon!")