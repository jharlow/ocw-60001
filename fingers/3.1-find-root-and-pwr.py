int = int(input("Enter integer: "))

for pwr in range(1, 6):
    root = 1
    while root**pwr <= int:
        if root**pwr == int:
            print(f"Root is {root} and power is {pwr}")
            break
        else:
            root += 1
