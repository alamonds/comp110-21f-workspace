"""Finding duplicate letters in a word."""

__author__ = "730345034"


word: str = input("Enter a word: ")
def duplicate(word) -> str:
    i: int = 0
    while i < len(word):
        j: int = i + 1
        while j < len(word):
            if word[i] == word[j]:
                return("Found duplicate: True")
            j += 1
        i += 1
    return("Found duplicate: False")


print(duplicate(word))