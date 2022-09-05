prices={
    "Bread":    0.42,
    "Milk":     1.69,
    "Cheese":   6.94
}

inv={
    "Bread":    69,
    "Milk":     42,
    "Cheese":   10
}

cart={}

def buy():
    req=input("Enter the item and quantity you wish to purchase (item,qty): ")
    if len(req.split(",")) !=2:
        print("Invalid input")
        return
    item,qty=req.split(",")
    if item not in prices.keys():
        print("Invalid item")
        return
    try: qty=int(qty)
    except ValueError:
        print("Invalid quantity")
        return
    if qty>inv[item]:
        print("Not enough items")
        return
    inv[item]-=qty
    if cart.get(item): cart[item]+=qty
    else: cart[item]=qty

def checkout():
    total=0
    for item,qty in cart.items():
        total+=prices[item]*qty
        print(f"- {qty}x {item}")
    print(f"Your total is ${total:.2f}")
    cart.clear()

user_input="meow?"
while user_input!="exit":
    user_input=input("Enter a command (buy,checkout,exit): ")
    if user_input=="buy":           buy()
    elif user_input=="checkout":    checkout()
    elif user_input!="exit":        print("Invalid command")
print("Thank you for shopping with us. Have a nice day!")