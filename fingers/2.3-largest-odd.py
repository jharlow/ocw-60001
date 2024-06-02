# from collections.abc import Callable
# from typing import List
#
# all_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# is_odd: Callable[[int], bool] = lambda x: x % 2 == 1
#
# head: Callable[[List[int]], int] = lambda x: x[0]
#
# print(head(sorted(filter(is_odd, all_nums), reverse=True)))


from types import NoneType

highest_odd: int | NoneType = None
total_questions = 10
remaining_questions = total_questions

while remaining_questions > 0:
    current_question = total_questions - remaining_questions + 1
    remaining_questions -= 1
    num = int(input(f"Enter integer {current_question} of {total_questions}: "))
    if num % 2 == 0 or highest_odd is None or highest_odd < num:
        highest_odd = num

print(f"highest_odd_number is {highest_odd}")
