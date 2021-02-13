"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730163234"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


def fortune_cookie() -> str:
    """Generates a random integer value between 1 and 5 and generates a unique fortune for that integer."""
    fortuneval: int = int(randint(1, 5))
    fortune1: str = str("It's a good day to be a Tar Heel!")
    fortune2: str = str("404: Fortune Not Found.")
    fortune3: str = str("It's a secret to everybody.")
    fortune4: str = str("The fortune you seek is in another cookie.")
    fortune5: str = str("Mmm, Monkey.")
    if fortuneval == 1:
        return fortune1
    else:
        if fortuneval == 2:
            return fortune2
        else:
            if fortuneval == 3:
                return fortune3
            else:
                if fortuneval == 4:
                    return fortune4
                else:
                    return fortune5


# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()
