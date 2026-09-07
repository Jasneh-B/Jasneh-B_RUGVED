#Write a python function to check if a given credit card number is valid or not using Luhn’s Algorithm


def check(card_num):

    total = 0
    rev = card_num[::-1]

    for i in range(len(rev)):
        digit = int(rev[i])
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9

        total += digit

    if total % 10 == 0:
        return True
    else:
        return False

num = input("Enter credit card number: ")

if check(num) == True:
    print("Valid credit card number")
else:
    print("Invalid credit card number")