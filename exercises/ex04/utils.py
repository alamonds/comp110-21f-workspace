"""List utility functions."""

__author__ = "730345034"


def all (numbers: list[int], num: int) -> bool:
    if len(numbers) == 0:
        return False
    for item in numbers:
        if item != num:
            return False
    return True


def is_equal (L1: list[int], L2: list[int]) -> bool:
    result: bool = False
    if len(L1) == len(L2):
        i: int = 0
        while i < len(L1):
            if L1[i] == L2[i]:
                result = True
            else: 
                return False
            i = i + 1
    return result


def max (nums: list[int]) -> int:
    if len(nums) == 0:
        raise ValueError("max() arg is an empty List")
    max_num: int = 0
    for input in nums:
        if input > max_num:
            max_num = input
    return max_num