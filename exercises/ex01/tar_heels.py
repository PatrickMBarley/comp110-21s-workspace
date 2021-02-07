"""An exercise in remainders and boolean logic."""

__author__ = "730163234"


TarHeels: int = int(input("Input an integer: "))
Rem2: int = int(TarHeels % 2)
Rem7: int = int(TarHeels % 7)

if Rem2 == 0 and Rem7 == 0:
    print("TAR HEELS")
else:
    if Rem2 == 0 and Rem7 != 0:
        print("TAR")
    else:
        if Rem2 != 0 and Rem7 == 0:
            print("HEELS")
        else:
            print("CAROLINA")
