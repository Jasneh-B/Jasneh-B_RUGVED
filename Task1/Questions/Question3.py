#Write a python program to check if given number is a hill number

num = input("Enter a number: ")

a = []
for x in num:
    a.append(int(x))

n = len(a)
flag = 0

if n < 3 or a[0] != a[n - 1]:
    print("Not a hill number")
else:
    i = 0
    while i < n - 1 and a[i] < a[i + 1]:
        i += 1
    
    peak = i

    if peak == 0 or peak == n - 1:
        print("Not a hill number")
    else:
        while i < n - 1 and a[i] > a[i + 1]:
            i += 1
        
        if i == n - 1:
            print("hill number")
        else:
            print("Not a hill number")