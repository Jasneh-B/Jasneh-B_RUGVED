#Define a function named “triple_and” that takes three parameters and returns True only if they are all True and False otherwise

def triple_and(a, b, c):
    case = a and b and c
    return case

a = False
b = False
c = True

print(triple_and(a, b, c))


