"""Krusty Krab Employee Simulator."""

from random import randint

__author__ = "730163234"

valued_employee: str = str()
adventure_points: int = 0

def main() -> None:
    """Entrypoint  of the adventure""" 
    if adventure_points == 0 and valued_employee == "":
        greeting()
    print(f"Hello { valued_employee } Star! Welcome to the Krusty Krab Employee Simulator!")
    print("Main Menu:\n 1: Start your first day at the Krusty Krab!\n 2: Stay at home... \n 3: Exit Simulator")
    menu_selection: int = int(input("What do you want to do today? (Input 1, 2, or 3): "))
    if menu_selection == 1:
        sim()
    else:
        if menu_selection == 2:
            home()
        else:
            if menu_selection == 3:
                quit()
            else:
                print("Please make an integer selection between 1 and 3.")
                main()

def greeting() -> None:
    global valued_employee
    valued_employee = input("What is your name? ")

def sim() -> None:
    occupation: int = int(randint(1, 3))
    occupation1: str = str("Welcome to the Krusty Krab, today we will have you working as a Frycook")
    occupation2: str = str("Welcome to the Krusty Krab, today we will have you working as a Cashier")
    occupation3: str = str("Welcome to the Krusty Krab, today we will have you working as a Phone Answerer")
    if occupation == 1:
        print(occupation1)
        frycook()
    else:
        if occupation == 2:
            print(occupation2)
            cashier()
        else:
            if occupation == 3:
                print(occupation3)
                phone()

def home() -> None:
    print("You decide to stay home and sleep under a comfy rock.\nYou wonder what your cephalopod neighbor is up to?")
    print(f"Your total award points = {adventure_points}")
    main()
    
def quit() -> None:
    print(f"See you next time, {valued_employee}!")

def frycook() -> None:
    count: int = 0
    print("Here you will be cooking patties for our famous Krabby Patties>\nMake sure they are cooked just right, not too hot or cold!")
    while count < 5:
        cook_time: float = float(input("What tempurature will you cook the patty at? (The grill goes from 0-11) "))
        if cook_time < 4:
            print("\U00002744 The patty is too cold! \U00002744")
        else:
            if cook_time > 4 and cook_time < 8:
                print("\U0001F980 Great job, that's a patty Mr. Krabs would be proud of! \U0001F980")


def cashier() -> None:
    print("a")

def phone() -> None:
    print("a")

if __name__ == "__main__":
  main()