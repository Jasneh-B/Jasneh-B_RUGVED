#Write a python function to perform selection sort on a given tring.


def selection_sort(string):
    a = list(string)
    n = len(a)
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if a[j] < a[min]:
                min = j
        temp = a[i]
        a[i] = a[min]
        a[min] = temp
    ans = ""
    for char in a:
        ans += char
    return ans  

s = input("Enter a string: ")
print(selection_sort(s))