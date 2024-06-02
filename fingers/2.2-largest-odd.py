from collections.abc import Callable
from typing import List, TypeVar

x = int(input("Item one"))
y = int(input("Item two"))
z = int(input("Item three"))


is_odd: Callable[[int], bool] = lambda x: x % 2 == 1


T = TypeVar("T")


def head(items: List[T]) -> T:
    return items[0]


print(head(sorted(filter(is_odd, [x, y, z]), reverse=True)))
