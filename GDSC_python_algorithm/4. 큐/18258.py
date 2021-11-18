from collections import deque

import sys

N = int(sys.stdin.readline())
deq = deque()

for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        deq.append(command[1])
    elif command[0] == "pop":
        if len(deq) ==0:
            print(-1)
        else:
            print(deq[0])
            deq.popleft()
    elif command[0] == "size":
        print(len(deq))
    elif command[0] == "empty":
        if len(deq) == 0:
            print("1")
        else:
            print("0")
    elif command[0] == "front":
        if len(deq) == 0:
            print("-1")
        else:
            print(deq[0])
    else:
        if len(deq) == 0:
            print("-1")
        else:
            print(deq[-1])