N, M = map(int,input().split())

board = []
recolor = []
for i in range(N):
    board.append(input())
wrong_list = []
for n in range(N-7):
    for m in range(M-7):
        wrong_white = 0
        wrong_black = 0
        for j in range(n,n+8):
            for k in range(m,m+8):
                if (j%2 == n%2 and k%2 == m%2) or (j%2 != n%2 and k%2 != m%2):
                    if board[j][k]=="B":
                        pass
                    else :
                        wrong_black += 1
                else :
                    if board[j][k] =="B":
                        wrong_black += 1
                    else : pass

                if (j%2 == n%2 and k%2 == m%2) or (j%2 != n%2 and k%2 != m%2):
                    if board[j][k]=="W":
                        pass
                    else :
                        wrong_white += 1
                else :
                    if board[j][k] =="W":
                        wrong_white += 1
                    else : pass

        wrong_list.append(min(wrong_black, wrong_white))

print(min(wrong_list))

# 4중 for문을 쓰는게 최선일까..?
