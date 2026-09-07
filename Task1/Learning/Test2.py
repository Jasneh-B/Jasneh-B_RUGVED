"""

from Test1 import student

Student1 = student("XYZ", "Computer Science", 9.2)
Student2 = student("ABC", "Mechanical Engineering", 7.2)

for student in [Student1, Student2]:
    print(student.on_honor_roll())

"""

from Test1 import Chef
from Test3 import ChineseChef

mychef = Chef()
mychef.make_chicken()
mychef.make_salad()
mychef.make_special_dish()

print("\n")

myChineseChef = ChineseChef()
myChineseChef.make_special_dish()
myChineseChef.make_fried_rice()
