"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730345034"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
FORTUNE: int = 5
random: int = randint(0,10)
print("Your fortune cookie says... ")
if random == 9:
    print("Your week will get better")
if random == FORTUNE:
    print("You will get an A on your next exam.")
else:
    if random > FORTUNE: 
        print("Something exciting is coming!")
    else:
        print("Someone special is coming your way!") 

print("Now, go spread positive vibes")    

