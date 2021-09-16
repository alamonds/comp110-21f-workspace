"""An exercise in remainders and boolean logic."""

__author__ = "730345034"

flag: int = int(input("Enter an int: "))
result: str = ""

def unc(number):
    if number % 2 == 0 and number % 7 == 0:
        return ("Tar Heels")
    else:
        if number % 2 == 0:
            return ("Tar")
    if number % 7 == 0:
        return ("Heels")
    else:
        if number % 7 > 0:
            return ("Carolina")
        if number % 2 > 0:
            return ("Carolina")    
print(unc(flag))

