"""List utility functions part 2."""

__author__ = "730345034"

# Define your functions below

def only_evens(lst: list) -> list:
    result: list[int] = []
    for item in lst:
        if item % 2 == 0:
            result.append(item)
    return result 

def sub(lol: list, start: int, end: int) -> list:
    result: list[int] = []
    i: int = 0
    while i < len(lol):
        if i >= start and i < end: 
            result.append(lol[i])
        i = i + 1
    return result

a_list = [10, 20, 30, 40]
print(sub(a_list, 1, 3))

def concat(a: list, b: list) -> list:
    result: list[int] = []
    for item in a: 
        result.append(item)
    for item in b:
        result.append(item)
    return result

a = [1,2,3]
b = [3,4,5]
print(concat(a,b))





