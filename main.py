# function is used whenever program needs an index number or integer of one character length
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
            # code used for program to call on the getting_integer function
            my_integer = int(input(m))
        # message to be presented to the user if input entered is not an integer or a negative integer
        except ValueError:
            print("Please enter a positive integer")
            continue
        # message to be presented to the user if an \integer is entered that is outside the minimum and maximum length parameters
        if my_integer < a or my_integer > b:
            print("You have not entered a valid value")
        else:
            # program is to return the accepted entered integer
            return my_integer


# function is used whenever a less than 50 character long input is asked of by the user
def get_string(m, a=1, b=50):
    """Get a string from the user.

    :param m: str (message)
    :param a: int (minimum char)
    :param b: int (maximum char)
    :return: str
    """
    getting_string = True
    while getting_string is True:
        # code used for program to call on the getting_string function
        my_string = input(m)
        # message to be presented to the user if a message is entered that is outside the minimum and maximum length parameters
        if len(my_string) < a or len(my_string) > b:
            print("You have entered too many characters, please try again.")
        else:
            # program is to return the accepted entered string
            return my_string


# function is used whenever a yes or no input is asked for
def get_short_entry(m, L=('yes', 'no')):
    """

    :param m: str(message)
    :param L: tuple ( default ('yes', 'no') )
    :return: str
    """
    yn = True
    while yn:
        # code used for program to call on the get_short_entry function
        my_string = input(m).lower()
        # message to be presented to the user if an input other than yes or no is entered
        if my_string not in L:
            print("Please enter " + " or ".join(L).upper())
        else:
            # program is to return the accepted entered string
            return my_string.title()


# function is used to get the user phone number
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
            # code used for program to call on the getting_phone function
            my_phone = (input(m))
        # message to be presented to the user if an input that is invalid or negative is entered, program will then continue
        except ValueError:
            print("Please enter a different number")
            continue
        # message to be presented to the user if an input containing characters other than numbers is entered, program will then continue
        if not my_phone.isdigit():
            print("Please only enter numbers")
            continue
        # message to be presented to the user if a phone number is entered that is outside the minimum and maximum length parameters
        if len(my_phone) < a or len(my_phone) > b:
            print("You have not entered a valid value")
        else:
            # program is to return the accepted entered phone number
            return my_phone


# function to print the sandwich menu
def print_sandwiches(L):
    """

    :param L:
    :return: None
    """
    # programing is calling on sandwich list to print the menu when the function is called upon
    for i in range(0, len(L)):
        # formatted as index number, name, dietary requirement, price
        output = "{:<3}: {:74} --- {:10} --- {:<4}".format(i, L[i][0], L[i][1], L[i][2])
        # sandwich menu is then printed and formatted using lines to divide code into sections
        print(output)
        print("-" * 150)


# function to order sandwiches off the menu
def add_sandwich(L, C):
    """

    :param L:
    :param C: list (Customer order list)
    :return: None
    """
    # users ordered is printed to show them editing options
    print_sandwiches(L)
    # user is asked which sandwich they would like to add, validated by the length of the sandwich order
    order_index = get_integer("Please enter the index number of the Sandwich you would like to order-> ", 0, len(L) - 1)
    # variables are identified
    name = L[order_index][0]
    dietary = L[order_index][1]
    price = L[order_index][2]
    # user is asked how many sandwiches they would like to add
    message = "How many {} sandwiches would you like to order? (max is 5) -> ".format(name)
    # addition is validated by the get integer function
    order_amount = get_integer(message, 0, 5)
    # overall price is calculated with amount of sandwiches
    overall_price = price * order_amount
    # amount of sandwiches is added to the order, it is formatted to break up large chunks of code
    user_order = [order_amount, name, dietary, price, overall_price]
    C.append(user_order)
    print("-" * 150)
    return None


# function to edit the amount of sandwiches that the user has ordered
def edit_order(C):
    """

    :param C: list (Customer order list)
    :return: None
    """
    # preventative code used to disable the user from using the edit order function if they do not have any sandwiches already within the order
    if len(C) == 0:
        print("You do not currently have any data entered within your order, please order before editing your order.")
        return None

    # printing the current order, formatted with the index number, amount ordered, name, dietary requirement, price, and total price
    for i in range(0, len(C)):
        output = "{:<3}: {:<3}: {:74} --- {:10} --- {:<4} --- {:<4.2f}".format(i,
                                                                               C[i][0],
                                                                               C[i][1],
                                                                               C[i][2],
                                                                               C[i][3],
                                                                               C[i][4])
        # current order is printed and formatted using lines to divide code into sections
        print(output)
    print("-" * 150)

    # code begins to remove sandwiches off the order by the index number of desired sandwich to be entered
    order_index = get_integer("Please enter the index number of the Sandwich you would like to remove from your "
                              "order-> ", 0, len(C) - 1)
    # variables are identified
    order_amount = C[order_index][0]
    name = C[order_index][1]
    price = C[order_index][3]
    # user is asked how many sandwiches they would like to remove
    message = "How many {} sandwiches would you like to remove? -> ".format(name)
    # removal is validated by the get integer function
    removal_number = get_integer(message, 0, order_amount)
    # new number is calculated and new price is created, both are replaced within the order
    new_amount = order_amount - removal_number
    C[order_index][0] = new_amount
    new_price = price * new_amount
    C[order_index][4] = new_price
    # if sandwiches have been completely removed they will be popped and removed entirely from the order
    if new_amount == 0:
        C.pop(order_index)
    return None


# function to collect customer details and define delivery method
def details(D):
    """

    :param D: list (Customer details list)
    :return: None
    """
    # when details are already stored within the details list, if statement will be used to ask user if they would like to re-enter details
    if len(D) != 0:
        # short entry function is used to only allow a yes or no answer
        detail_correction = get_short_entry(
            "There are details already stored in our system, would you like to re-enter them? (Yes or No) --> ")
        # if the user's details don't need to be re-entered, the user will return to the main function
        if detail_correction == "No":
            return None
        # if the user's details do need to be re-entered, the current details will be cleared and the user will continue through the function
        elif detail_correction == "Yes":
            D.clear()

    # presenting available collection options that the user can choose from
    collection_options = '''
    P : Pickup
    D : Delivery
       '''
    print(collection_options)
    # user is asked which collection method of collection they would like, this is done by the short_entry function as p and d are made to equal yes and no
    collection = get_short_entry("Please select your collection option: ", ['p', 'd']).upper()

    # if statement program will run if pickup is chosen
    if collection == "P":
        # user is asked to enter applicable details, because pickup has been chosen their address is not applicable
        print("Please enter your customer details below:")
        print("-" * 80)
        name = get_string("Please enter your full name --> ")
        phone_number = get_phone_number("Please enter your phone number --> ")
        address = "Not Applicable"
        collection_method = "Pickup"
        print("-" * 80)
        # details are formatted and then appended to the details list so that they are stored within the program
        details = [name, phone_number, collection_method, address]
        D.append(details)

    # elif statement program will run if delivery is chosen
    elif collection == "D":
        # user is asked to enter applicable details, address is needed due to the collection method being delivery
        print("Please enter your customer details below:")
        print("-" * 80)
        name = get_string("Please enter your full name --> ")
        phone_number = get_phone_number("Please enter your phone number --> ")
        address = get_string("Please enter your address --> ")
        # user is notified about the automatic delivery fee that will be added to their total when their order is finalized
        print("An automatic $3 delivery free will be added to your total")
        collection_method = "Delivery"
        print("-" * 80)
        # details are formatted and then appended to the details list so that they are stored within the program
        details = [name, phone_number, collection_method, address]
        D.append(details)


# function to review the order and customer details
def review_order(C, D):
    """

    :param C: list (Customer order list)
    :param D: list (Customer details list)
    :return: None
    """
    # this functionally mainly includes formatting to produce a receipt like piece of code showing the final order and details
    print("Marsden Gourmet Sandwich Bar Order:")
    print("-" * 150)
    # headers for the order is formatted as index, amount , name, dietary, price, overall price
    order_title = "{:5}: {:6}: {:78} {:14} {:9} {:11}".format("Index", "Amount", "Sandwich Type", "Dietary", "Price",
                                                              "Total Price")
    # printing the headers for the order list
    print(order_title)
    print("-" * 150)
    total = 0
    for i in range(0, len(C)):
        # order list is formatted as index, amount , name, dietary, price, overall price
        output = "{:5}: {:6}: {:74} --- {:10} --- {:5} --- {:<4.2f}".format(i, C[i][0], C[i][1], C[i][2], C[i][3],
                                                                            C[i][4])
        # the total of all sandwiches is calculated
        total += C[i][4]
        # printing the order from the order list
        print(output)
    print("-" * 150)
    print("Details:")
    print("-" * 150)
    # headers for the details is formatted as name, phone number, collection method, address
    delivery_title = "{:20} {:20} {:20} {:30}".format("Name", "Phone Number", "Collection Method", "Address")
    # printing the headers for the details list
    print(delivery_title)
    for i in range(0, len(D)):
        # details list is formatted as name, phone number, collection method, address
        output = f"{D[i][0]:20} {D[i][1]:20} {D[i][2]:20} {D[i][3]:30}"
        # printing the details from the details list
        print(output)

    print("-" * 150)
    # the total price is being calculated
    amount_due = total
    # if statement is used to define whether the collection method is delivery, if so the delivery fee is added
    if "Delivery" in range(2, len(D)):
        amount_due += 3
    # total price is calculated and printed, rounded to two decimal places
    print("Total Price - {:.2f}".format(amount_due))
    print("-" * 150)
    return None


# function is called upon to finalize the users order and start a new one when finalized
def finalize_order(C, D):
    """

    :param C: list (Customer order List)
    :param D: list (Customer details list)
    :return: None
    """
    # if the length of the customers order list is 0, they haven't ordered the finalization function will not run as there is nothing to finalise
    if len(C) == 0:
        # the function will instead ask them to return to the main menu and place an order
        print(
            "You do not currently have any data entered within your order, please order before finalizing your order.")
        return None

    # if the length of the customer details list is 0, they haven't entered details the finalization function will not run as there is no details to send the order too
    if len(D) == 0:
        # the function will instead ask them to return to the main menu and enter their details
        print("You do not currently have any details entered within your order, please enter your details before "
              "finalizing your order.")
        return None

    # function will print the final receipt using the review_order function
    print(review_order(C, D))
    # they will be asked if they want to confirm their order using the short_entry (yes/no) function
    confirm_order = get_short_entry("Would you like to confirm your order? (Yes/No) -> ").upper()
    # if they want to confirm their order both the customer details and customer order lists will be cleared, they will be notified a new order is starting and will be returned to the main function
    if confirm_order == "YES":
        print("Thank you for your order at Marsden's Gourmet Sandwich Bar")
        C.clear()
        D.clear()
        print("A new order is beginning . . .")
        print("-" * 150)
    # if they do not wish to confirm their order they will be returned to the main function to continue their order
    elif confirm_order == "NO":
        print("-" * 150)
    # any other inputs will be identified as an error and the user will be asked to re-enter an input
    else:
        print("Error: Yes No should have been captured on get short entry")
    return None


# funtion holding the menu_list
def main():
    """Run program

    :return: None
    """
    # sandwich list holding the names, dietary requirements and price of the sandwiches which is then used across almost every function
    my_sandwiches = [
        ["Halloumi and Apricot Jam", "Vegetarian", 15.95],
        ["Roasted Beetroot, Carrots, Spiced Nuts and Whipped Feta", "Vegetarian", 15.95],
        ["Cheddar and Jalapeno", "Vegetarian", 13.95],
        ["Sausage and Egg", "No Dietary", 14.95],
        ["Smoked Salmon Deluxe", "No Dietary", 15.95],
        ["Buttermilk Chicken, Scotch Bonnet Jam, Pickled Cabbage and Crispy Shallots", "No Dietary", 18.95]
    ]

    # order list which gains details of the order formatted by order_amount, name, dietary, price, overall_price
    customer_order = []

    # details list which gains details of the customer formatted by name, phone number, collection method, address
    customer_details = []

    # user choice list which gives the user options which link to functions above
    user_choice = '''
    M : Sandwich Menu
    O : Order 
    E : Edit Order
    C : Customer Details
    R : Review Order
    F : Finalize Order
    Q : Quit 
    '''

    # customer options menu
    run = True
    while run:
        print(user_choice)
        # the user is asked to select what they would like to out of the options below which are linked to functions
        choice = get_string("Please select your option: ", 1, 1).upper()
        print("-" * 150)
        # output when m is entered, will cause the sandwich menu to print calling on the my_sandwiches list
        if choice == "M":
            print_sandwiches(my_sandwiches)

        # output when o is entered, will cause the add sandwich function to run, calling on the menu and details list
        elif choice == "O":
            add_sandwich(my_sandwiches, customer_order)

        # output when e is entered, will cause the edit order function to run, calling on the order list
        elif choice == "E":
            edit_order(customer_order)

        # output when c is entered, will cause the details function to run, calling on the details list
        elif choice == "C":
            details(customer_details)

        # output when r is entered, will cause the review order function to run, calling on the order and details list
        elif choice == "R":
            review_order(customer_order, customer_details)

        # output when f is entered, will cause the finalize order function to run, calling on the order and details list
        elif choice == "F":
            finalize_order(customer_order, customer_details)

        # output when q is entered, will cause the program to quit
        elif choice == "Q":
            print("Thank you")
            run = False

        # output for all unexpected inputs
        else:
            print("Unrecognised entry")


if __name__ == "__main__":
    main()
