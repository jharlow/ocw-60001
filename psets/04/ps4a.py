# Problem Set 4A
# Name: John Harlow


from functools import reduce
from typing import List


def get_permutations(sequence: str) -> List[str]:
    """
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    """

    match len(sequence):
        case 1:
            return [sequence]
        case 2:
            return [sequence[0] + sequence[1], sequence[1] + sequence[0]]
        case _:
            return reduce(
                lambda acc, val: [
                    val[:i] + sequence[0] + val[i:] for i in range(len(val) + 1)
                ]
                + acc,
                get_permutations(sequence[1:]),
                [],
            )


if __name__ == "__main__":
    #    #EXAMPLE
    example_input = "abc"
    print("Input:", example_input)
    print("Expected Output:", ["abc", "acb", "bac", "bca", "cab", "cba"])
    print("Actual Output:", get_permutations(example_input))

    example_input_1 = "dog"
    print("Input:", example_input_1)
    print("Expected Output:", ["dog", "dgo", "odg", "ogd", "gdo", "god"])
    print("Actual Output:", get_permutations(example_input_1))

    example_input_2 = "cat"
    print("Input:", example_input_2)
    print("Expected Output:", ["cat", "cta", "act", "atc", "tca", "tac"])
    print("Actual Output:", get_permutations(example_input_2))

    example_input_3 = "sun"
    print("Input:", example_input_3)
    print("Expected Output:", ["sun", "snu", "usn", "uns", "nsu", "nus"])
    print("Actual Output:", get_permutations(example_input_3))
