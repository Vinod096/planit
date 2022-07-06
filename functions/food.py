from secrets import choice
from tkinter.messagebox import YES
from sqlalchemy import true
from sympy import use



burgers = {'McDonalds': 'McSpicy Chicken Burger, 20$','Hungry Jacks': 'Double Tender Crispy Chicken Burger,15$', 'Grilld': 'Chicken Burger, 25$ \n Beef Burger, 15$'}
pizza = {'Dominos': {'Chicken Pizza, 20$ '}, 'Pizza Hut': {'Pepperoni Pizza, 15$ '}, 'Martys Pizza': {'Chicken Pharma, 25$'}}


def customer(burgers, pizza):
    user = str(input("What type of food you requried (Pizza / Burgers): "))
    if user == 'burgers':
        print("Restuarants available for Burgers : \n", burgers)
    elif user == 'pizza':
        print("Restuarants available for Burgers : \n", pizza)
    else:
        print("Sorry..! Food Item is available.!")
        exit()
    return user

def order_burgers(customer,burgers) :
    food_burgers = []
    while (True):
            restuarant_name = str(input("Enter name of the resturant : "))
            if (restuarant_name == 'McDonalds'):
                print ("Resturant contains following Burgers : \n ",burgers['McDonalds'])
                food_burgers.append(burgers['McDonalds'])
                choice = input('Do you want to more food items (Yes / No ) : ')
                if choice == "yes":
                    continue
                elif choice == "no":
                    print("Thanks for Ordering..!")
                    print("Your order has been sent to Restaurant. Enjoy your food")
                    return True

            if (restuarant_name == 'Grilld'):
                print("Resturant contains following Burgers : \n", burgers['Grilld'])
                food_burgers.append(burgers['Grilld'])
                choice = input('Do you want to more food items (Yes / No ) : ')
                if choice == "yes":
                    continue
                elif choice == "no":
                    print("Thanks for Ordering..!")
                    print("Your order has been sent to Restaurant. Enjoy your food")
                    return True

            if (restuarant_name == 'Hungry Jacks'):
                print("Resturant contains following Burgers : \n ", burgers['Hungry Jacks'])
                food_burgers.append(burgers['Hungry Jacks'])
                choice = input('Do you want to more food items (Yes / No ) : ')
                if choice == "yes":
                    continue
                elif choice == "no":
                    print("Thanks for Ordering..!")
                    print("Your order has been sent to Restaurant. Enjoy your food")
                    return True
            else:
                print("Please enter valid restaurant name")
                break
    return food_burgers

def order_pizza(customer,pizza):

    food_pizza = []
    while (True):
            restuarant_name = str(input("Enter name of the resturant : "))

            if (restuarant_name == 'Dominos'):
                print("Resturant contains following Burgers : \n ",pizza['Dominos'])
                food_pizza.append(pizza['Dominos'])
                choice = input('Do you want to more food items (Yes / No ) : ')
                if choice == "yes":
                    continue
                elif choice == "no":
                    print("Thanks for Ordering..!")
                    print("Your order has been sent to Restaurant. Enjoy your food")
                    return True

            if (restuarant_name == 'Pizza Hut'):
                print("Resturant contains following Burgers : \n",pizza['Pizza Hut'])
                food_pizza.append(pizza['Pizza Hut'])
                choice = input('Do you want to more food items (Yes / No ) : ')
                if choice == "yes":
                    continue
                elif choice == "no":
                    print("Thanks for Ordering..!")
                    print("Your order has been sent to Restaurant. Enjoy your food")
                    return True

            if (restuarant_name == 'Marys Pizza'):
                print("Resturant contains following Burgers : \n ",pizza['Martys Pizza'])
                food_pizza.append(pizza['Martys Pizza'])
                choice = input('Do you want to more food items (Yes / No ) : ')
                if choice == "yes":
                    continue
                elif choice == "no":
                    print("Thanks for Ordering..!")
                    print("Your order has been sent to Restaurant. Enjoy your food")
                    return True
            else:
                print("Please enter valid restaurant name")
                exit()
    return food_pizza

def main() :

    person = customer(burgers, pizza)
    burgers_order = order_burgers(person,burgers)
    pizza_orders = order_pizza(person,pizza)
main()

