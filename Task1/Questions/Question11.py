#Write a Python program that prints the grade level of a given text using Coleman-Liau formula.

text = input("Enter text: ")

letters = 0
words = 1
sentences = 0

for char in text:
    if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
        letters += 1
    if char == ' ':
        words += 1
    if char == '.' or char == '!' or char == '?':
        sentences += 1

L = (letters/words) * 100
S = (sentences/words) * 100

index = 0.0588 * L - 0.296 * S - 15.8
grade = round(index)

if grade < 1:
    print("Less than Grade 1")
elif grade >= 16:
    print("More than Grade 16")
else:
    print("Grade", grade)