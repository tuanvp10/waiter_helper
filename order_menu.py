#  As a user I want to be able to order 3 times, and have my responses added to a list, so they aren't forgotten

# As a user, I want to have my order read back to me in formatted way, so I know what I ordered.

from menu import Menu

class Waiter(Menu):

    def __init__(self):
        super().__init__()

    def customer_order(self):
        print("Hello and welcome to make your own takeaway!")
        print(show_menu.food_base(), "\n")
        choice1 = input("Firstly, please pick a base\n")
        print(show_menu.toppings(), "\n")
        choice2 = input("Now pick toppings you would like to add\n")
        print(show_menu.sauces(), "\n")
        choice3 = input("Now finally pick what sauce you would like to add\n")


        final_order = [choice1, choice2, choice3]
        print("Here's your order:\n" + "\n".join(final_order))



show_menu = Waiter()
show_menu.customer_order()