import sys

n = int(sys.stdin.readline())

std_birth = []
std_name = {}
for i in range(n):
    std = sys.stdin.readline().split()
    std_birth.append(int(std[3]+std[2].zfill(2)+ std[1].zfill(2)))
    std_name[int(std[3]+std[2].zfill(2)+std[1].zfill(2))] = std[0]

print(std_name[max(std_birth)])
print(std_name[min(std_birth)])
