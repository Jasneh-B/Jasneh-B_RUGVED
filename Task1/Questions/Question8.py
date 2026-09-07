#Write a python program to divide a given string into equal parts containing n(user input) characters of same sequence. Example: string=“abcdabcdabcdabcd” n=4 output: “abcd”, “abcd”, “abcd”, “abcd” If the division is not possible or the sequence cannot be same, print out the appropriate error.


s = input("Enter string: ")
n = int(input("Enter length: "))

if len(s) % n != 0:

    print("String cannot be divided into equal parts")

else:
    parts = []
    for i in range(0, len(s), n):
        parts.append(s[i:i+n])
    first = parts[0]
    same = True
    for p in parts:
        if p != first:
            same = False

    if same == False:
        print("Sequences are not the same")
    else:
        print(parts)