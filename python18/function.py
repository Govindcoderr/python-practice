def pattern(n):
    if n <= 0:  # Base condition to stop recursion
        return
    elif n < 25:
        print("*" * n)
        pattern(n - 1)
    else:
        print("Enter a number less than 25")

# Take input and convert to integer
n = int(input("Enter Number: "))
pattern(n)
