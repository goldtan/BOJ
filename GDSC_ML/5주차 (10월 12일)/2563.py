import sys

N = int(sys.stdin.readline())

white_board = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(N):
    left, down = map(int, sys.stdin.readline().split())
    for i in range(left,left+10):
        for j in range(down, down+10):
            white_board[i][j] = 1
    
    #white_board[left:left+10][down:down+10] = 1

color_sum = 0

for k in range(101):
    color_sum += sum(white_board[k])

print(color_sum)
