from typing import Literal

binary_string = input("Enter a binary string (only 0 and 1s accepted): ")


def binary_char_to_int(char: str) -> Literal[0, 1]:
    if len(char) != 1:
        raise TypeError("Some char got processed as 0 or more than 1 chars")
    if char not in ("0", "1"):
        raise ValueError("Your input contained a value other than 0 or 1")
    return 1 if char == "1" else 0


def parse_binary_string(string: str):
    return enumerate(map(binary_char_to_int, reversed(list(string))))


def get_binary_value(binary_data: enumerate[Literal[0, 1]]):
    return sum(binary * 2**power for power, binary in binary_data)


print(get_binary_value(parse_binary_string(binary_string)))
