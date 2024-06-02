import numpy


def get_float_input(message: str):
    return float(input(message))


x = get_float_input("Enter a number (x): ")
y = get_float_input("Enter a number to raise it by (y): ")
raised = float(x**y)
log = round(numpy.log2(x))
print(f"Raised number (x to the power of y): {raised}")
print(f"Log of (x) is: {log}")
