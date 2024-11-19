# Shopping cart program

cart = {}

def display_menu():
    print("\n ****SHOPPING CART MENU**** ")
    print("1. Add item to cart")
    print("2. Remove from the cart")
    print("3. Update item quantity")
    print("4. View cart")
    print("5. Total price")
    print("6. Exit")

def add_item():
    item_name = input("Enter the item name: ").strip().lower()
    price =  float(input("Enter the item's price: "))
    quantity = int(input("Enter the quantity of the item: "))

    if item_name in cart:
        cart[item_name]['quantity'] += quantity
        print(f"{item_name.capitalize()} quantity updated to {cart[item_name]['quantity']}")
    else:
        cart[item_name] = {'price' : price , 'quantity' :quantity}
        print(f"{item_name.capitalize()} added to the cart")

def remove_item():
    item_name = input("Enter the item to remove: ").strip().lower()

    if item_name in cart:
        del cart[item_name]
        print(f"{item_name.capitalize()} remove from the cart")
    else:
        print(f"{item_name.capitalize()} is not in the cart")

def update_quantity():
    item_name = input("Enter the item name for update the quantity: ").strip().lower()
    
    if item_name in cart:
        quantity = int(input("Enter the quantity: "))

        cart[item_name]['quantity'] = quantity
        print(f"{item_name.capitalize()} quantity updated to {quantity}")
    else:
        print(f"{item_name.capitalize()} is not in the cart")

def view_cart():
    if not cart:
        print("Your cart is empty.")
        return
    
    print ("\n Current Cart Contents: ")
    total_cost = 0

    for item, details, in cart.items():
        each_total = details['price']*details['quantity']
        total_cost += each_total

        print(f"{item.capitalize()} - price: ₹{details['price']:.2f} | quantity :{details['quantity']} | each_total : ₹{each_total:.2f}")
    print(f" overall total : ₹{total_cost:.2f}")

def calculate_total():
    if not cart:
        print("Your cart is empty.")
    else:
        total_cost = sum(details['price'] * details['quantity'] for details in cart.values())
        print(f" The total cost of all items : ₹{total_cost:.2f}")

def main():
    while True:
        display_menu()
        choice = input("choose an option (1-6): \n")

        if choice == '1':
            add_item()
        elif choice == '2':
            remove_item()
        elif choice == '3':
            update_quantity()
        elif choice == '4':
            view_cart()
        elif choice =='5':
            calculate_total()
        elif choice == '6':
            print("Exit from the program.")
            break
        else:
            print("Invaild option. Please try again.")

if __name__ == "__main__":
    main()

        
        
    

