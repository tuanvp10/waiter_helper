# User Stories

## 1. As a user I want to be able to see the menu in a formatted way, so that I can order my meal.

## 2. As a user I want to be able to order 3 times, and have my responses added to a list, so they aren't forgotten

## 3. As a user, I want to have my order read back to me in formatted way, so I know what I ordered.

### First Iteration

- As a user I want to be able to see the menu in a formatted way, so that I can order my meal.
- The user will be given a set menu with prices next to the dish.

This shows below, the class I have produced that will be later imported to be used:
```python
class Menu:

    def food_base(self):
        return "Pick your base:: \nEgg Noodles \nUdon Noodles \nJasmine Rice \nWhole Grain Rice"

    def toppings(self):
        return "Choose your favourites:: \nChicken \nBeef \nPork \nPrawn \nMixed Vegetables"

    def sauces(self):
        return "Pick a sauce:: \nSweet and Sour \nOyster \nGreen Curry \nSzechuan"
```

### Second Iteration

This iteration will show the menu of choices and allows the user to pick where finally in the end, be totalled and show the user what they ordered.

```python
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
```
