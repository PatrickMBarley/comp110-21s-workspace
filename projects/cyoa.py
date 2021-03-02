"""Krusty Krab Employee Simulator."""

from random import randint

__author__ = "730163234"

player: str = str()
points: int = int()
award_count: int = int()


def main() -> None:
    """Entrypoint  of the adventure.""" 
    if points == 0 and player == "":
        greet()
    elif award_count >= 5 and player != "":
        farewell()
    print(f"Hello {player} Star! Welcome to the Krusty Krab Employee Simulator!")
    print("Main Menu:\n1: Start your day at the Krusty Krab!\n2: Stay at home... \
            \n3: Check points/purchase awards.\n4: Exit Simulator")
    menu_selection: int = int(input("What do you want to do today? (Input 1, 2, 3, or 4): "))
    if menu_selection == 1:
        sim()
    else:
        if menu_selection == 2:
            home()
        else:
            if menu_selection == 3:
                award()
            else:
                if menu_selection == 4:
                    quit()
                else:
                    print("Please make an integer selection between 1 and 3.")
                    main()


def greet() -> None:
    """Greets the player and asks for their name."""
    global player
    print("Welcome valued employee!")
    player = input("What is your name? ")


def sim() -> None:
    """Randomly chooses one of three simulations for the player to experience."""
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
    """The player can stay at home and check their point total."""
    print("You decide to stay home and sleep under a comfy rock.\nYou wonder what your cephalopod neighbor is up to?")
    print(f"Your total award points = {points}")
    main()


def award() -> None:
    """Allows the player to purchase awards."""
    global points
    global award_count
    print(f"Hi {player} Star, you have {points} award points and {award_count} awards. \
            \nWould you like to redeem 10 points for an award?")
    answer: str = str()
    while answer not in ("yes", "no"):
        answer = (input("Enter yes or no"))
        if answer == "yes":
            if points >= 10:
                award_count = award_count + 1
                points = points - 10
                print(f"Congratulations, {player} Star! You have won an award! \
                        \nEveryone here is super proud of you!\nKeep up the good work!")
            else:
                print("You have not performed well enough to get an award.\nCome back when you have 10 points.")
        elif answer == "no":
            print(f"Okay, see you later {player} Star!")
        else:
            print("Please enter yes or no")
    main()


def quit() -> None:
    """Quits the simulator and ends the program."""
    print(f"See you next time, {player} Star!")
    exit()


def frycook() -> None:
    """Frycook simulation, allows the palyer to choose cooking temp for food in order to get points."""
    count: int = 0
    MIN_TEMP = 4
    MAX_TEMP = 8
    print("Here you will be cooking patties for our famous Krabby Patties! \
            \nMake sure they are cooked just right, not too hot or cold!")
    while count < 5:
        cook_time: float = float(input("What tempurature will you cook the patty at? (The grill goes from 0-11) "))
        if cook_time < MIN_TEMP:
            print("\U00002744 The patty is too cold! \U00002744")
            global points
            points = points - 1
            count += 1
        else:
            if cook_time >= MIN_TEMP and cook_time <= MAX_TEMP:
                print("\U0001F980 Great job, that's a patty Mr. Krabs would be proud of! \U0001F980")
                points = points + 1
                count += 1
            else:
                print("\U0001F525 Are you trying to burn down the Krusty Krab!?!? \U0001F525")
                points = points - 1
                count += 1
    print(f"That's enough patties for today, see you tomorrow!\nYour total award points = {points}")
    main()


def cashier() -> None:
    """Allows the player to experience the existential dread of their cephalopod neighbor."""
    global points
    points = points + 1
    print(f"(You can't help but shake the dread that you will work this job for 40 years and then die) \
            \nSee you tomorrow!\nYour total award points = {points}")
    main()


def phone() -> None:
    """Runs a scenario in which the player gives random responses to customers, no points given."""
    Answer1: str = str(f"No, this is {player}.")
    Answer2: str = str(f"Noooo, this is {player}...")
    Answer3: str = str(f"NO, this is {player}!!!")
    count: int = 0
    print("Here you will be taking calls from hungry and inquisitive customers!")
    while count < 3:
        Answer: int = int(randint(1, 3))
        print("Is this the Krusty Krab?")
        if Answer == 1:
            print(Answer1)
            count += 1
        else:
            if Answer == 2:
                print(Answer2)
                count += 1
            else:
                if Answer == 3:
                    print(Answer3)
                    count += 1
    print(f"Maybe we should try this another time...\nYour total award points = {points}")
    main()


def farewell() -> None:
    """The end game of the simulator. The win state of the game."""
    print(f"You have performed admirably {player} Star.\nThe Krusy Krab will forever be in your debt. \
            \n{award_count} awards is an astounding accomplishment for a seastar such as yourself. \
            \nAfter a legendary lifetime of service, we think it is time you finally rest.\nGod speed, sailor...")
    exit()


if __name__ == "__main__":
    main()