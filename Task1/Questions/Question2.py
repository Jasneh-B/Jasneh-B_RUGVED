#Write a python program to sort a string alphabetically and print the count of each character.

string = input("Enter a string: ")


string = sorted(string.lower())


for ch in set(string):
    count = 0
    for x in string:
        if x == ch:
            count += 1
    print(ch, ":", count)

