"""An exercise in remainders and boolean logic."""

__author__ = "730345034"

flag: int = int(input("Enter an int: "))
result: str = ""

def unc(number):
    if number % 2 == 0 and number % 7 == 0:
        return ("TAR HEELS")
    else:
        if number % 2 == 0:
            return ("TAR")
    if number % 7 == 0:
        return ("HEELS")
    else:
        if number % 7 > 0:
            return ("CAROLINA")
        if number % 2 > 0:
            return ("CAROLINA")    
print(unc(flag))