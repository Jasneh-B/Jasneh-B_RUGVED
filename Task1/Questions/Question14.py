#Given an array arr[], find the first repeating element. The element should occur more than once and the index of its first occurrence should be the smallest.


arr = input("Enter the array: ").split()

for i in range(len(arr)):
    arr[i] = int(arr[i])

ans = -1

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j]:
            ans = arr[i]
            break
    if ans != -1:
        break

if ans != -1:
    print(f"First repeating element: {ans} at index {arr.index(ans)} and pos {arr.index(ans) + 1}")
else:
    print("No repeating element")