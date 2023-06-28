def get_integer(m):
    my_integer=int(input(m))
    return my_integer

def get_string(m):
    my_string=input(m)
    return my_string

def single_loop_print(L):
    for i in range(0, len(L)):
        output = "{:<3}:{:80} --- {:30} --- {:<10}". format(i, L[i][0], L[i][1], L[i][2])
        print(output)


def add_sandwich():
    return None

def main():
    my_sandwiches = [
        ["Halloumi and Apricot Jam", "Vegetarian", 15.95],
        ["Roasted Beetroot, Carrots, Spiced Nuts and Whipped Feta", "Vegetarian", 15.95],
        ["Cheddar and Jalapeno", "Vegetarian", 13.95],
        ["Sausage and Egg", "", 14.95],
        ["Smoked Salmon Deluxe", "", 15.95],
        ["Buttermilk Chicken, Scotch Bonnet Jam, Pickled Cabbage and Crispy Shallots", "", 18.95]
    ]

    user_choice = '''
    P : Print Sandwich Options
    Q : Quit 
    '''

    run=True
    while run == True:
        print(user_choice)
        choice = get_string("Please select your option:").upper()
        if choice == "P":
            single_loop_print(my_sandwiches)

        elif choice == "Q":
            print("Thank you")
            run = False

main()
