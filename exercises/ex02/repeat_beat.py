"""Repeating a beat in a loop."""

__author__ = "730345034"


# Begin your solution here...
zero: int = 0
beat: str = str(input("What beat do you want to repeat? ")) 
number: int = int(input("How many times do you want it to repeat? "))
result: str = str("")

if (number < 1):
    print("No beat...")
else:
    while number > zero:
        result = result + beat + " "
        number = number -1
    print(result)

