"""Tar Heels exercise redux as a structured program."""

__author__ = "730163234"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    response: int = int(input("Enter an int: "))
    print(tar_heels(response))


def tar_heels(response: int) -> str:
    """Calculates the appropriate response based on the user's integer input."""
    Rem2: int = int(response % 2)
    Rem7: int = int(response % 7)
    Option1: str = str("TAR HEELS")
    Option2: str = str("TAR")
    Option3: str = str("HEELS")
    Option4: str = str("CAROLINA")
    if Rem2 == 0 and Rem7 == 0:
        return Option1
    else:
        if Rem2 == 0 and Rem7 != 0:
            return Option2
        else:
            if Rem2 != 0 and Rem7 == 0:
                return Option3
            else:
                return Option4


if __name__ == "__main__":
    main()
