from typing import Any


def add_everything_up(a: int | float | str, b: int | float | str) -> int | float | str:
    try:
        return a + b
    except TypeError:
        return str(a) + str(b)


print(add_everything_up(1, 2))
print(add_everything_up("1", 2))
print(add_everything_up(52.56, 8))