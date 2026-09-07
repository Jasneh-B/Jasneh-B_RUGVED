#WAP a code to print the following patterns

pat = int(input("Enter pattern number(1 or 2): "))

if pat == 1:
    n = int(input("Enter n: "))

    for i in range(1, n + 1):
        spaces = " " * (n - i)
        astericks = "* " * i
        print(spaces + astericks)

    for i in range(n, 0, -1):
        spaces = " " * (n - i)
        astericks = "* " * i
        print(spaces + astericks)

elif pat == 2:
    n = int(input("Enter n: "))
    
    for i in range(1, n + 1):
        if i == n:
            print("*" * (2 * n - 1))
        else:
            print("*" * i + " " * (2 * (n - i) - 1) + "*" * i)

    for i in range(n - 1, 0, -1):
        print("*" * i + " " * (2 * (n - i) - 1) + "*" * i)