

WELCOME_MSG = """Drink list:
    1. Espresso
    2. Americano
    3. Latte Macchiato
    4. Black Tea
    5. Green Tea
    6. Yellow Tea
    7. Quit"""

class Beverage:

    def __init__(self, drink, calories, price):

        self.__drink = drink
        self.__price = price
        self.__calories = calories
        self.__sugar = 0
        self.__milk = 0

    def addSugar(self):
        print("How much sugar would you like to add?", end = ' ')
        while True:
            sugar = input()
            if sugar > '3' or sugar < '0':
                print("Enter a number between 0 and 3:", end = ' ')
                continue
            sugar = int(sugar)
            if sugar + self.__sugar + self.__milk > 3:
                print("You can only add three total condiments, try again:", end = ' ')
            else:
                self.__sugar += sugar
                print("You added", str(sugar), "sugar(s) to your drink.\n")
                break

    def addMilk(self):
        print("How much milk would you like to add?", end = ' ')
        while True:
            milk = input()
            if milk > '3' or milk < '0':
                print("Enter a number between 0 and 3:", end = ' ')
                continue
            milk = int(milk)
            if milk + self.__sugar + self.__milk > 3:
                print("You can only add three total condiments, try again:", end = ' ')
            else:
                self.__sugar += milk
                print("You added", str(milk), "milk(s) to your drink.\n")
                break

    def __str__(self):
        return "Here is your " + self.__drink + " with " + self.__calories + " calories for " + self.__price + " dollars"

    

class Latte(Beverage):

    def __init__(self):
        super().__init__("Latte", '400', '5')
        self.__lactose = "50 mg"

    def getLactose(self):
        return self.__lactose

    def __str__(self):
        return super().__str__()

class Tea(Beverage):

    def __init__(self, drink, color, calories, price):
        super().__init__(drink, calories, price)
        self.__color = color

    def getColor(self):
        return self.__color

    def __str__(self):
        return super().__str__()

class MainController:

    def __init__(self):

        print(WELCOME_MSG)
        self.__drink = int(input("Enter your drink choice: "))

    def getDrink(self):
        return self.__drink




def main():

    while True:

        menu = MainController()
        if menu.getDrink() == 1:
            drink = Beverage("Espresso", '150', '3')
        elif menu.getDrink() == 2:
            drink = Beverage("Americano", '200', '4')
        elif menu.getDrink() == 3:
            drink = Latte()
        elif menu.getDrink() == 4:
            drink = Tea("Black Tea", "black", '70', '1.50')
        elif menu.getDrink() == 5:
            drink = Tea("Green Tea", "green", '80', '2')
        elif menu.getDrink() == 6:
            drink = Tea("Yellow Tea", "yellow", '100', '2.50')
        elif menu.getDrink() == 7:
            print("Goodbye")
            break
        else:
            print("Invalid drink selection, try again.")

        drink.addSugar()
        drink.addMilk()
        print(drink)
        input("Press enter to continue...\n")


if __name__ == "__main__":
    main()
