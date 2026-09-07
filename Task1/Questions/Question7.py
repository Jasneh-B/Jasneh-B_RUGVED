#Write a program to print the Fibonacci Sequence till n-values where n is user input


n = int(input("Enter the number of terms: "))
print("Fibonacci Sequence:")
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
    i += 1