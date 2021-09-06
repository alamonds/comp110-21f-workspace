"""Counting letters in a string."""

__author__ = "730345034"


# Begin your solution here...
letter: str = str(input("What letter do you want to search for? "))
word: str = str(input("Enter a word: "))
counter: int = 0
result: int = 0
word_length: int = len(word)
while counter < word_length:
    if word[counter] == letter:
        result = result + 1
    counter = counter + 1
print("Count: " + str(result)) 
 