"""
from math import *

name = input("Enter your name: ")
age = int(input("Enter your age: "))

name_1 = [ name , age , "Hello" , "World" ]
name_2 = [int(input("Enter your age2: ")), int(input("Enter your age3: ")), int(input("Enter your age4: ")), int(input("Enter your age5: "))]

name_2.sort() 
print(name_2)

print(name_1)
print(name_1[0])
print(name_1[1:])
print(name_1[1:3])

age1 = age + 4

print(f"HI {name} your age is {age1}")    

print(len(name))

print(age1 % age) 




x = open ("test.txt", "r+")

print(x.read())

x.write("\nprint('This is a test')")

x.seek(0)
print(x.read())
x.close()


class student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    def on_honor_roll(self):
        if self.gpa >= 8.5:
            return True
        else:
            return False


    def display(self):
        print(f"Student Name: {self.name}, Major: {self.major}, GPA: {self.gpa}")

"""



class Chef:
    def make_chicken(self):
        print("The chef makes chicken")

    def make_salad(self):
        print("The chef makes salad")

    def make_special_dish(self):
        print("The chef makes biryani")