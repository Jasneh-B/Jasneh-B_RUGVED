#Create a function that takes two strings as input and checks whether they are anagrams of each other.

def anagram(string1, string2):
    s1 = string1.lower()
    s2 = string2.lower()
    
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

if anagram(string1, string2) == True:
    print("Anagrams")
else:
    print("Not Anagrams")