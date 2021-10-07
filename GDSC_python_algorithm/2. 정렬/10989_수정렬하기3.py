import sys

N = int(sys.stdin.readline())
num_list = [0] * 10001 #

for _ in range(N):
    num_list[int(sys.stdin.readline())] += 1

for i in range(1,10001):
    if num_list[i] != 0:
        for _ in range(num_list[i]):
            print(i)

# N의 값이 10000 이하이기 때문에 리스트의 범위를 제한해주기 
# sys로 입력을 받기