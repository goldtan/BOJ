import sys
from collections import deque

N = int(sys.stdin.readline())

board = [[i, j] for i in range(N) for j in range(N)]

num_apple = int(sys.stdin.readline())
list_apple = []

for _ in range(num_apple):
    apple = list(map(int,sys.stdin.readline().split()))
    list_apple.append(apple)

num_dir = int(sys.stdin.readline())
list_dir = []
for _ in range(num_dir):
    dir = sys.stdin.readline().split()
    list_dir.append([int(dir[0]), str(dir[1])])

print(list_dir)

snake = deque([0,0])
timer = 0
state = "D"


while snake not in board :
    if state == "D" :
        snake.append()
        snake.popleft()
    elif state == "W" :
        pass
    elif state == "A" :
        pass
    else :
        print(3) 
    
    timer +=1

