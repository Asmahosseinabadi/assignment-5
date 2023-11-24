n = int(input("enter n: "))
pascal_triangle = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(i+1):
        if j == 0 or j == i:
            pascal_triangle[i][j] = 1
        else:
            pascal_triangle[i][j] = pascal_triangle[i-1][j-1] + pascal_triangle[i-1][j]

for i in range(n):
    for j in range(i+1):
        print(pascal_triangle[i][j], end="  ")
    print()
