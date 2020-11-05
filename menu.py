class Menu:
    def __init__(self):
        self.menu = [
            "Spicy Chicken",
            "Sweat and Sour Beef",
            "Fries",
            "Mash Potatoes",
            "Pizza",
            "Carbonara",
            "Bolognese",
            "Wine",
            "Beer",
            "Water",
            "BLT Sandwich",
        ]


class Waiter(Menu):
    def __init__(self):
        super().__init__()
        self.order = []

    def ordering(self):
        is_ordering = True
        print("What would you like to order?")

        while is_ordering:
            choice = input("=> ")

            if choice in self.menu:
                self.order.append(choice)
            else:
                print("We do not offer that type of food")

            print("Anything else?")

            choice_2 = input("=> ")
            if choice_2.lower() == "no":
                is_ordering = False

        return self.order

    def __str__(self):
        return " ".join(k for k in self.order)


def main():
    user = Waiter()

    print("Welcome to our restaurant.")
    user.ordering()
    print(f"You have ordered:\n{user}")


if __name__ == "__main__":
    main()