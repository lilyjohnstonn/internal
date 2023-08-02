def get_integer(m):
    my_integer=int(input(m))
    return my_integer

def get_string(m):
    my_string=input(m)
    return my_string

def get_YN(m):
    yn = True
    while yn:
        my_string = input(m).lower()
        if my_string not in ["yes", "no"]:
            print("Please enter Yes or No")
        else:
            return my_string.title()



#printing the sandwich menu
def print_sandwiches(L):
    for i in range(0, len(L)):
        output = "{:<3}: {:74} --- {:10} --- {:<4}". format(i, L[i][0], L[i][1], L[i][2])
        print(output)

#ordering sandwiches off the menu
def add_sandwich(L,C):
    print_sandwiches(L)
    print("-"*150)
    order_index = get_integer("Please enter the index number of the Sandwich you would like to order-> ")
    name = L[order_index][0]
    dietary = L[order_index][1]
    price = L[order_index][2]
    message = "How many {} sandwiches would you like to order? -> ".format(name)
    order_amount = get_integer(message)
    overall_price = price * order_amount
    user_order = [order_amount, name, dietary, price, overall_price]
    C.append(user_order)
    return None

#edit sandwiches that the user has ordered
def edit_order(C):
    for i in range(0, len(C)):
        output = "{:<3}: {:<3}: {:74} --- {:10} --- {:<4} --- {:<4.2f}".format(i, C[i][0], C[i][1], C[i][2], C[i][3], C[i][4])
    print(output)

    order_index = get_integer("Please enter the index number of the Sandwich you would like to remove from your order-> ")
    order_amount = C[order_index][0]
    name = C[order_index][1]
    dietary = C[order_index][2]
    price = C[order_index][3]
    overall_price = C[order_index][4]
    message = "How many {} sandwiches would you like to remove? -> ".format(name)
    removal_number = get_integer(message)
    new_amount = order_amount - removal_number
    C[order_index][0] =  new_amount
    new_price = price * new_amount
    C[order_index][4] = new_price
    return None

#collect customer details
def details(D, C):
    if len(D) != 0:
        detail_correction = get_YN("There are details already stored in our system, would you like to re-enter them? (Yes or No) --> ")
        if detail_correction == "No":
            return None
        elif detail_correction == "Yes":
            D.clear()

    collection_options = '''
    P : Pickup
    D : Delivery
       '''
    print(collection_options)
    collection = get_string("Please select your collection option: ").upper()

    if collection == "P":
        print("Please enter your customer details below:")
        print("-" * 80)
        name = get_string("Please enter your full name --> ")
        phone_number = get_integer("Please enter your phone number --> ")
        address = "Not Applicable"
        collection_method = "Pickup"
        print("-" * 80)
        details = [name, phone_number, collection_method, address]
        D.append(details)

    elif collection == "D":
        print("Please enter your customer details below:")
        print("-" * 80)
        name = get_string("Please enter your full name --> ")
        phone_number = get_integer("Please enter your phone number --> ")
        address = get_string("Please enter your address --> ")
        print("An automatic $3 delivery free will be added to your total")
        collection_method = "Delivery"
        print("-" * 80)
        details = [name, phone_number, collection_method, address]
        D.append(details)



#review the order and customer details
def review_order(C,D):
    title = "{:5}: {:6}: {:78} {:14} {:9} {:11}".format("Index", "Amount", "Sandwich Type", "Dietary", "Price",
                                                        "Total Price")
    print("Order:")
    print(title)
    print("-" * 150)
    for i in range(0, len(C)):
        output = "{:5}: {:6}: {:74} --- {:10} --- {:5} --- {:<4.2f}". format(i, C[i][0], C[i][1], C[i][2], C[i][3], C[i][4])
        print(output)
    if "Delivery" in D:
        output = "{:<3}: {:<3}: {:74} --- {:10} --- {:<4} --- {:<4.2f}".format("", "1", "Delivery", "", "",
                                                                               3)


    print("-"*150)

    for i in range(0, len(D)):
        output = f"Name --- {D[i][0]:20}, Phone Number --- {D[i][1]:13}, Collection Method --- {D[i][2]:7}, Address --- {D[i][3]:30}"
        print("Details:")
        print(output)
        return None

#menu_list
def main():
    my_sandwiches = [
        ["Halloumi and Apricot Jam", "Vegetarian", 15.95],
        ["Roasted Beetroot, Carrots, Spiced Nuts and Whipped Feta", "Vegetarian", 15.95],
        ["Cheddar and Jalapeno", "Vegetarian", 13.95],
        ["Sausage and Egg", "No Dietary", 14.95],
        ["Smoked Salmon Deluxe", "No Dietary", 15.95],
        ["Buttermilk Chicken, Scotch Bonnet Jam, Pickled Cabbage and Crispy Shallots", "No Dietary", 18.95]
    ]

    customer_order = []
    customer_details = []

    user_choice = '''
    M : Sandwich Menu
    O : Order 
    E : Edit Order
    C : Customer Details
    R : Review Order
    Q : Quit 
    '''

    run=True
    while run == True:
        print(user_choice)
        choice = get_string("Please select your option: ").upper()
        print("-"*150)
        if choice == "M":
            print_sandwiches(my_sandwiches)

        elif choice == "O":
            add_sandwich(my_sandwiches, customer_order)

        elif choice == "E":
            edit_order(customer_order)

        elif choice == "C":
            details(customer_details, customer_order)

        elif choice == "R":
            review_order(customer_order, customer_details)

        elif choice == "Q":
            print("Thank you")
            run = False


if __name__ == "__main__":
    main()
