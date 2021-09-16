"""Drawing forests in a loop."""

__author__ = "730345034"

depth = int(input("Depth: "))
TREE: str = '\U0001F332'

i = 1
while i <= depth:
    result: str = ""
    j = 0
    while j < i:
        result += TREE
        j += 1
    print(result)
    i += 1