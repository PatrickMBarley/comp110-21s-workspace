"""EX03 - prime functions."""

__author__: str = "730163234"


def main() -> None:
    """Entrypoint of the program."""
    print(is_prime(3))
    print(is_prime(6))
    print(is_prime(31))
    print(is_prime(110))
    print(list_primes(3, 7))
    print(list_primes(10, 20))
    print(list_primes(25, 28))
    print(list_primes(-1, 5))


def is_prime(input: int) -> bool:
    """Calculates whether or not the inputed value is prime or not."""
    if input > 1:
        for i in range(2, input):
            if input % i == 0:
                return False
        return True
    else:
        return False


def list_primes(first: int, second: int) -> list[int]:
    """Calculates whether or not the inputed range has prime numbers and compiles those numbers into a list."""
    list = []
    for i in range(first, second):
        if is_prime(i):
            list.append(i)
    return list
            

if __name__ == "__main__":
    main()