# User Input

x = int(input("Enter a number to see Multiplication Tables: "))

print(type(x))


def multipy(n):
    for i in range(10):
        s = n * i
        print(n, "X", i, "=", s)


multipy(x)

# range = range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
