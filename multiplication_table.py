def multiplication_table(m,n):
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            print(i * j, end=" \t")
        print("\n")

a=int(input("enter m : "))
b=int(input("enter n : "))
multiplication_table(a,b)