#Write a python function to encrypt a string using Ceasar’s Cipher


def encrypt(string, shift):
    ans = ""
    for i in range(len(string)):
        char = string[i]
        if char.isupper():
            ans += chr(((ord(char) + shift - 65) % 26) + 65)
        elif char.islower():
            ans += chr(((ord(char) + shift - 97) % 26) + 97)
        else:
            ans += char
    return ans


string = input("Enter a string: ")
shift_value = int(input("Enter shift value: "))

print("Encrypted string is " + encrypt(string, shift_value))