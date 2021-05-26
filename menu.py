# As a user I want to be able to see the menu in a formatted way, so that I can order my meal.
# The user will be given a set menu with prices next to the dish.

class Menu:

    def food_base(self):
        return "Pick your base:: \nEgg Noodles \nUdon Noodles \nJasmine Rice \nWhole Grain Rice"

    def toppings(self):
        return "Choose your favourites:: \nChicken \nBeef \nPork \nPrawn \nMixed Vegetables"

    def sauces(self):
        return "Pick a sauce:: \nSweet and Sour \nOyster \nGreen Curry \nSzechuan"
