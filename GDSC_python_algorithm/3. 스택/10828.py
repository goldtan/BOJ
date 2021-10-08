class Stack:
    def __init__(self):
        self.stack_list = []
    def push(self, num):
        self.stack_list.append(num)
    def pop(self):
        if len(self.stack_list) == 0:
            print("-1")
        else:
            print(self.stack_list.pop())
    def size(self):
        print(len(self.stack_list))
    def empty(self):
        if len(self.stack_list) == 0:
            print("1")
        else :
            print("0")
    def top(self):
        if len(self.stack_list) == 0:
            print("-1")
        else :
            print(self.stack_list[-1])

import sys

N = int(sys.stdin.readline())
s = Stack()

for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        s.push(command[1])
    elif command[0] == "pop":
        s.pop()
    elif command[0] == "size":
        s.size()
    elif command[0] == "empty":
        s.empty()
    else :
        s.top()

