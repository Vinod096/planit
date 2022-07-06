
food_burgers = {'McDonalds': 'McSpicy Chicken Burger, $20','Hungry Jacks': 'Double Tender Crispy Chicken Burger,$15', 'Grilld': 'Chicken Burger, $25 & Beef Burger $15'}
food_pizza = {'Dominos': 'Chicken Pizza, $20 ', 'Pizza Hut': 'Pepperoni Pizza, $15 ', 'Martys Pizza': 'Chicken Pharma, $25'}


def customer():
    food_type = str.lower((input("What type of food you requried (Pizza / Burgers): ")))
    if food_type == 'burgers':
        for x, y in food_burgers.items():
            print(x, ' \t: \t', y)
    elif food_type == 'pizza':
        for x, y in food_pizza.items():
            print(x, ' \t: \t', y)
    else:
        print("Sorry..! Food Item is available.!")
        exit()
    return food_type


def order_burgers():
    restuarant_name = str.lower((input("Enter name of the resturant : ")))
    if (restuarant_name == 'mcdonalds' or 'mcd'):
        print("Order : ", food_burgers['McDonalds'])
    elif (restuarant_name == 'grilld'):
        print("Order : ", food_burgers['Grilld'])
    elif (restuarant_name == 'hungry jacks'):
        print("Resturant contains following Burgers : \n ",food_burgers['Hungry Jacks'])
    else:
        print("Please enter valid restaurant name")


def order_pizza():
    restuarant_name = str.lower((input("Enter name of the resturant : ")))
    if (restuarant_name == 'dominos'):
        print("Order : ", food_pizza['Dominos'])
    elif (restuarant_name == 'pizza hut'):
        print("Order : ", food_pizza['Pizza Hut'])
    elif (restuarant_name == 'martys pizza'):
        print("Order : ", food_pizza['Martys Pizza'])
    else:
        print("Please enter valid restaurant name")


def main():
    order = customer()
    if order == 'burgers':
        order_burgers()
    elif order == 'pizza':
        order_pizza()


main()
