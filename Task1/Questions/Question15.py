#Rotate an n*n matrix by 90° clockwise.Take a user input for a matrix and print the elements in spiral order

n = int(input("Enter size of square matrix: "))

matrix = []
for i in range(n):
    row = []
    for j in range(n):
        value = int(input("Enter element: "))
        row.append(value)
    matrix.append(row)

for i in range(n):
    for j in range(i, n):
        temp = matrix[i][j]
        matrix[i][j] = matrix[j][i]
        matrix[j][i] = temp

for i in range(n):
    matrix[i].reverse()

top = 0
bottom = n - 1
left = 0
right = n - 1

print("Spiral Order is ")
while top <= bottom and left <= right:
    for i in range(left, right + 1):
        print(matrix[top][i], end=" ")
    top = top + 1

    for i in range(top, bottom + 1):
        print(matrix[i][right], end=" ")
    right = right - 1

    if top <= bottom:
        for i in range(right, left - 1, -1):
            print(matrix[bottom][i], end=" ")
        bottom = bottom - 1

    if left <= right:
        for i in range(bottom, top - 1, -1):
            print(matrix[i][left], end=" ")
        left = left + 1
