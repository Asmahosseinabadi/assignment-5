def chessboard(m, n):
    board = ""
    for i in range(m):
        for j in range(n):
            if (i + j) % 2 == 0:
                board += "# "
            else:
                board += "* "
        board += "\n"
    print(board)
a=int(input("enter m : "))
b=int(input("enter n : "))
chessboard(a,b)