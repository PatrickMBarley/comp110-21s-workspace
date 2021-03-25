"""EX03 - avoid_fifth function."""

__author__: str = "730163234"


def main() -> None:
    """Entrypoint of the program."""
    print(avoid_fifth("hello"))
    print(avoid_fifth("The sentence we have here possesses E's galore!"))


def avoid_fifth(input: str) -> str:
    """Identifies specified letters and concatenates them out in a new string."""
    result: str = ""
    for i in range(0, len(input)): 
        if input[i] != "e" and input[i] != "E": 
            result = result + input[i]
    return result


if __name__ == "__main__":
    main()