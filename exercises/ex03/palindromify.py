"""EX03 - palindromify function."""

__author__: str = "730163234"


def main() -> None:
    """Entrypoint of the program."""
    print(palindromify("race", False))
    print(palindromify("han", True))
    print(palindromify("red", True))
    print(palindromify("live on time ", False))


def palindromify(input: str, check: bool) -> str:
    """Checks for even or odd palindrome and concatenates the reversed string."""
    if check is True:
        for i in range(len(input) - 1, -1, -1):
            input = input + input[i]
            print("enter")
    elif check is False:
        for i in range(len(input) - 2, -1, -1):
            input = input + input[i]
    return input


if __name__ == "__main__":
    main()