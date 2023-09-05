def get_integer(m, a=0, b=5):
    """Get integer from user

    :param m: str (message)
    :param a: int (minimum)
    :param b: int (maximum)
    :return: int
    """
    getting_integer = True
    while getting_integer is True:
        try:
            my_integer = int(input(m))
        except ValueError:
            print("Please enter a positive integer")
            continue
        if my_integer < a or my_integer > b:
            print("You have not entered a valid value")
        else:
            return my_integer


def get_string(m, a=1, b=50):
    """Get a string from the user.

    :param m: str (message)
    :param a: int (minimum char)
    :param b: int (maximum char)
    :return: str
    """
    getting_string = True
    while getting_string is True:
        my_string = input(m)
        if len(my_string) < a or len(my_string) > b:
            print("You have entered too many characters, please try again.")
        else:
            return my_string


def get_short_entry(m, L=('yes', 'no')):
    """

    :param m: str(message)
    :param L: tuple ( default ('yes', 'no') )
    :return: str
    """
    yn = True
    while yn:
        my_string = input(m).lower()
        if my_string not in L:
            print("Please enter " + " or ".join(L).upper())
        else:
            return my_string.title()


# function to get the user phone number
def get_phone_number(m, a=8, b=12):
    """

    :param m: str(message)
    :param a: int(minimum)]
    :param b: int(maximum)
    :return: int
    """
    getting_phone = True
    while getting_phone is True:
        try:
            my_phone = (input(m))
        except ValueError:
            print("Please enter a different number")
            continue
        if not my_phone.isdigit():
            print("Please only enter numbers")
            continue
        if len(my_phone) < a or len(my_phone) > b:
            print("You have not entered a valid value")
        else:
            return my_phone


# printing the sandwich menu
def print_sandwiches(L):
    """

    :param L:
    :return: None
    """
    for i in range(0, len(L)):
        output = "{:<3}: {:74} --- {:10} --- {:<4}".format(i, L[i][0], L[i][1], L[i][2])
        print(output)
        print("-" * 150)


# ordering sandwiches off the menu
def add_sandwich(L, C):
    """

    :param L:
    :param C: list (Customer order list)
    :return: None
    """
    print_sandwiches(L)
    order_index = get_integer("Please enter the index number of the Sandwich you would like to order-> ", 0, len(L) - 1)
    name = L[order_index][0]
    dietary = L[order_index][1]
    price = L[order_index][2]
    message = "How many {} sandwiches would you like to order? (max is 5) -> ".format(name)
    order_amount = get_integer(message, 0, 5)
    overall_price = price * order_amount
    user_order = [order_amount, name, dietary, price, overall_price]
    C.append(user_order)
    print("-" * 150)
    return None


# edit sandwiches that the user has ordered
def edit_order(C):
    """

    :param C: list (Customer order list)
    :return: None
    """

    if len(C) == 0:
        print("You do not currently have any data entered within your order, please order before editing your order.")
        return None

    for i in range(0, len(C)):
        output = "{:<3}: {:<3}: {:74} --- {:10} --- {:<4} --- {:<4.2f}".format(i,
                                                                               C[i][0],
                                                                               C[i][1],
                                                                               C[i][2],
                                                                               C[i][3],
                                                                               C[i][4])
        print(output)
    print("-" * 150)

    # removal of sandwiches off the order
    order_index = get_integer("Please enter the index number of the Sandwich you would like to remove from your "
                              "order-> ", 0, len(C) - 1)
    order_amount = C[order_index][0]
    name = C[order_index][1]
    price = C[order_index][3]
    message = "How many {} sandwiches would you like to remove? -> ".format(name)
    removal_number = get_integer(message, 0, order_amount)
    new_amount = order_amount - removal_number
    C[order_index][0] = new_amount
    new_price = price * new_amount
    C[order_index][4] = new_price
    if new_amount == 0:
        C.pop(order_index)
    return None


# collect customer details
def details(D):
    """

    :param D: list (Customer details list)
    :return: None
    """
    if len(D) != 0:
        detail_correction = get_short_entry(
            "There are details already stored in our system, would you like to re-enter them? (Yes or No) --> ")
        if detail_correction == "No":
            return None
        elif detail_correction == "Yes":
            D.clear()

    # available collection options
    collection_options = '''
    P : Pickup
    D : Delivery
       '''
    print(collection_options)
    collection = get_short_entry("Please select your collection option: ", ['p', 'd']).upper()

    # pickup up delivery function
    if collection == "P":
        print("Please enter your customer details below:")
        print("-" * 80)
        name = get_string("Please enter your full name --> ")
        phone_number = get_phone_number("Please enter your phone number --> ")
        address = "Not Applicable"
        collection_method = "Pickup"
        print("-" * 80)
        details = [name, phone_number, collection_method, address]
        D.append(details)

    # delivery function
    elif collection == "D":
        print("Please enter your customer details below:")
        print("-" * 80)
        name = get_string("Please enter your full name --> ")
        phone_number = get_phone_number("Please enter your phone number --> ")
        address = get_string("Please enter your address --> ")
        print("An automatic $3 delivery free will be added to your total")
        collection_method = "Delivery"
        print("-" * 80)
        details = [name, phone_number, collection_method, address]
        D.append(details)


# review the order and customer details
def review_order(C, D):
    """

    :param C: list (Customer order list)
    :param D: list (Customer details list)
    :return: None
    """
    print("Marsden Gourmet Sandwich Bar Order:")
    print("-" * 150)
    order_title = "{:5}: {:6}: {:78} {:14} {:9} {:11}".format("Index", "Amount", "Sandwich Type", "Dietary", "Price",
                                                              "Total Price")
    print(order_title)
    print("-" * 150)
    total = 0
    for i in range(0, len(C)):
        # index, amount , name, dietary, price, overall price
        output = "{:5}: {:6}: {:74} --- {:10} --- {:5} --- {:<4.2f}".format(i, C[i][0], C[i][1], C[i][2], C[i][3],
                                                                            C[i][4])
        total += C[i][4]
        print(output)
    print("-" * 150)
    print("Details:")
    print("-" * 150)
    delivery_title = "{:20} {:20} {:20} {:30}".format("Name", "Phone Number", "Collection Method", "Address")
    print(delivery_title)
    for i in range(0, len(D)):
        # name, phone number, collection method, address
        output = f"{D[i][0]:20} {D[i][1]:20} {D[i][2]:20} {D[i][3]:30}"
        print(output)

    print("-" * 150)
    amount_due = total
    if "Delivery" in range(2, len(D)):
        amount_due += 3
    print("Total Price - {}".format(amount_due))
    print("-" * 150)
    return None


def finalize_order(C, D):
    """

    :param C: list (Customer order List)
    :param D: list (Customer details list)
    :return: None
    """
    if len(C) == 0:
        print("You do not currently have any data entered within your order, please order before finalizing your order.")
        return None

    if len(D) == 0:
        print("You do not currently have any details entered within your order, please enter your details before "
              "finalizing your order.")
        return None

    print(review_order(C, D))
    confirm_order = get_short_entry("Would you like to confirm your order? (Yes/No) -> ").upper()
    if confirm_order == "YES":
        print("Thank you for your order at Marsden's Gourmet Sandwich Bar")
        C.clear()
        D.clear()
        print("A new order is beginning . . .")
        print("-" * 150)
    elif confirm_order == "NO":
        print("-" * 150)
    else:
        print("Error: Yes No should have been captured on get short entry")
    return None


# menu_list
def main():
    """Run program

    :return: None
    """
    my_sandwiches = [
        ["Halloumi and Apricot Jam", "Vegetarian", 15.95],
        ["Roasted Beetroot, Carrots, Spiced Nuts and Whipped Feta", "Vegetarian", 15.95],
        ["Cheddar and Jalapeno", "Vegetarian", 13.95],
        ["Sausage and Egg", "No Dietary", 14.95],
        ["Smoked Salmon Deluxe", "No Dietary", 15.95],
        ["Buttermilk Chicken, Scotch Bonnet Jam, Pickled Cabbage and Crispy Shallots", "No Dietary", 18.95]
    ]

    customer_order = []
    # order_amount, name, dietary, price, overall_price
    customer_details = []

    user_choice = '''
    M : Sandwich Menu
    O : Order 
    E : Edit Order
    C : Customer Details
    R : Review Order
    F : Finalize Order
    Q : Quit 
    '''

    # customer option menu
    run = True
    while run:
        print(user_choice)
        choice = get_string("Please select your option: ", 1, 1).upper()
        print("-" * 150)
        # print sandwich menu
        if choice == "M":
            print_sandwiches(my_sandwiches)

        # order sandwiches
        elif choice == "O":
            add_sandwich(my_sandwiches, customer_order)

        # edit order
        elif choice == "E":
            edit_order(customer_order)

        # enter customer details
        elif choice == "C":
            details(customer_details)

        # review order
        elif choice == "R":
            review_order(customer_order, customer_details)

        elif choice == "F":
            finalize_order(customer_order, customer_details)

        # quit the program
        elif choice == "Q":
            print("Thank you")
            run = False

        else:
            print("Unrecognised entry")


if __name__ == "__main__":
    main()
