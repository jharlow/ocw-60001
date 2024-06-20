def isIn(str_one: str, str_two: str) -> bool:
    return True if str_one in str_two or str_two in str_one else False


print(f"isIn(cattoro, cat) = {isIn('cattoro', 'cat')}")
print(f"isIn(cat, cattoro) = {isIn('cat', 'cattoro')}")
print(f"isIn(no, yes) = {isIn('no', 'yes')}")
