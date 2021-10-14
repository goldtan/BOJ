import sys

K = int(sys.stdin.readline())
num_stack = []
for _ in range(K):
    num = int(sys.stdin.readline())
    num_stack.append(num)
    if num == 0:
        num_stack.pop()
        num_stack.pop()

print(sum(num_stack))