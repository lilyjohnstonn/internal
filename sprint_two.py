def get_integer(m):
    my_integer=int(input(m))
    return my_integer

def get_string(m):
    my_string=input(m)
    return my_string

def print_sandwiches(L):
    for i in range(0, len(L)):
        output = "{:<3}: {:74} --- {:10} --- {:<4}". format(i, L[i][0], L[i][1], L[i][2])
        print(output)

def review_order(C):
    for i in range(0, len(C)):
        output = "{:<3}: {:74} --- {:10} --- {:<4} --- {:<4}". format(C[i][0], C[i][1], C[i][2], C[i][3], C[i][4])
        print(output)
    return None

def add_sandwich(L,C):
    print_sandwiches(L)
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

    user_choice = '''
    M : View Sandwich Menu
    R : Review Order
    O : Order Sandwiches
    Q : Quit 
    '''

    run=True
    while run == True:
        print(user_choice)
        choice = get_string("Please select your option: ").upper()
        if choice == "M":
            print_sandwiches(my_sandwiches)
        elif choice == "O":
            add_sandwich(my_sandwiches, customer_order)
        elif choice == "R":
            review_order(customer_order)
        elif choice == "Q":
            print("Thank you")
            run = False



if __name__ == "__main__":
    main()
