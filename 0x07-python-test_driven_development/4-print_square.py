#!/usr/bin/python3
def print_square(size):
    if isinstance(size, int):
        if size > 0:
            for _ in range(size):
                print("#" * size)
        else:
            raise ValueError("size must be >= 0")
    else:
        raise TypeError("size must be an integer")

print_square(4)
print("")
print_square(10)
print("")
print_square(0)
print("")
print_square(1)
print("")
try:
    print_square(-1)
except Exception as e:
    print(e)
print("")