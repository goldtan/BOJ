import sys

N = int(sys.stdin.readline())
top = list(map(int,sys.stdin.readline().split()))

signal_list = []

for _ in range(N):
    max_num_idx = 0
    var_pop = top.pop()

    for idx, i in enumerate(top):
        if var_pop < i:
            max_num_idx = idx + 1

    signal_list.append(max_num_idx)


signal_list.reverse()
print(signal_list)