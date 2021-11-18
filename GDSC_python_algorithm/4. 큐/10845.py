class Queue:
    def __init__(self):
        self.queue_list = []

    def push(self,num):
        self.queue_list.append(num)
    
    def pop(self):
        if self.queue_list:
            print(self.queue_list[0])
            del self.queue_list[0]
        else:
            print("-1")
    
    def size(self):
        print(len(self.queue_list))

    def empty(self):
        if self.queue_list:
            print("0")
        else:
            print("1")

    def front(self):
        if self.queue_list:
            print(self.queue_list[0])
        else:
            print("-1")
    
    def back(self):
        if self.queue_list:
            print(self.queue_list[-1])
        else:
            print("-1")
        
import sys

N = int(sys.stdin.readline())
q = Queue()

for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        q.push(command[1])
    elif command[0] == "pop":
        q.pop()
    elif command[0] == "size":
        q.size()
    elif command[0] == "empty":
        q.empty()
    elif command[0] == "front":
        q.front()
    else:
        q.back()
