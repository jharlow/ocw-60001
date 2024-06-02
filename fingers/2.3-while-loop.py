num_xs = int(input("how many times should I print the letter X? "))
to_print = ""

# Alternative for no need of while/for
# print(num_xs * "X")

# Actual
while num_xs > 0:
    to_print += "X"
    num_xs -= 1

print(to_print)
