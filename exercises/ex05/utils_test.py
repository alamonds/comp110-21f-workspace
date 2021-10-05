"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730345034"

from exercises.ex05.utils import only_evens, sub, concat

def test_only_evens_empty() -> None:
    a: list[int] = []
    assert only_evens(a) == []

def test_only_evens_some() -> None:
    a: list[int] = [1, 2, 3, 4]
    assert only_evens(a) == [2, 4]

def test_only_evens_many() -> None:
    a: list[int] = [3,5,7,9]
    assert only_evens(a) == []

def test_sub_empty() -> None:
    a: list[int] = []
    b: int = 0
    c: int = 1
    assert sub(a, b, c) == []

def test_sub_some() -> None:
    a: list[int] = [10, 20, 30, 40]
    b: int = 1
    c: int = 3
    assert sub(a, b, c) == [20, 30]

def test_sub_many() -> None:
    a: list[int] = [1, 2, 3, 4, 5]
    b: int = 2
    c: int = 3
    assert sub(a, b, c) == [3]

def test_concat_empty() -> None:
    a: list[int] = []
    b: list[int] = []
    assert concat(a, b) == []

def test_concat_some() -> None:
    a: list[int] = [1, 2, 3]
    b: list[int] = [4, 5, 6]
    assert concat(a, b) == [1, 2, 3, 4, 5, 6]

def test_concat_many() -> None:
    a: list[int] = [2, 4, 6]
    b: list[int] = [8, 10, 12]
    assert concat(a, b) == [2, 4, 6, 8, 10, 12]


