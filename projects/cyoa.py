"""Calling all the Monsters-Project."""

__author__ = "730345034"

from random import randint

spider: str = '\U0001F577'
pumpkin: str = '\U0001F383'
bat: str = '\U0001F987'
blood: str = '\U0001FA78'
web: str = '\U0001F578'
ghost: str = '\U0001F47B'
player: str = ""
points: int = 0

emojis: list[str] = [spider, pumpkin, bat, blood, web, ghost]


"""Defining main."""
def main() -> None:
    greet()
    option: str = input("What do you want to do? Enter: Reset points, play, or exit-- ")
    while option != "exit":
        if option == "exit":
            exit()
        if option == "play":
            points = number(points, player)
            if points > 25:
                print("hahaha you die <3")
                exit()
            if points == 25:
                print("Winner winner frog stew dinner!")
                exit()
        if option == "Reset points": 
            message()
        option = input("What do you want to do? Enter: Reset points, play, or exit-- ")


"""Defining message."""
def message() -> None: 
    print("Have a SPOOKTACULAR Halloween!!")
    points = 0
    print(f"Score: {points}")


"""Defining greeting."""
def greet() -> None: 
    print("Calling all the monsters: Enter the number of Halloween symbols you want, we will add the values of each! Get to 25 to stay alive!")
    player = input("Enter a player name: ")
    print(f"Welcome, {player}")


"""Defining number."""
def number(points:int, player:str) -> int: 
    num: int = int(input("Enter a number: "))
    i: int = 0
    while i < num:
        emoji: str = emojis[randint(0, 5)] 
        print(emoji)
        if emoji == spider:
            points = points + 4
            i= i + 1
        if emoji == bat:
            points = points + 6
            i = i + 1
        if emoji == pumpkin:
            points = points + 3
            i = i + 1
        if emoji == blood:
            points = points + 1
            i = i + 1
        if emoji == web:
            points = points + 8
            i = i + 1
        if emoji == ghost:
            points = points + 25
            i = i + 1
    print(f"Score: {points}")
    return points


if __name__ == "__main__":
    main()