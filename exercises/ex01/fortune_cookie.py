"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730163234"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


fortune: int = int(randint(1,5))

print("Your fortune cookie says...")
if fortune == 1:
    print("It's a good day to be a Tar Heel!")
else:
    if fortune == 2:
        print("404: Fortune Not Found.")
    else:
        if fortune == 3:
            print("It's a secret to everybody.")
        else:
            if fortune == 4:
                print("The fortune you seek is in another cookie.")
            else:
                print("Mmm, Monkey.")

print("Now, go spread positive vibes!")
