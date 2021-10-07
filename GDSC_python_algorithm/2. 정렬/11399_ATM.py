N = int(input())

time_list = list(map(int, input().split()))
time_list.sort()

time = 0
sum_time = 0

for i in time_list:
    time += i
    sum_time += time

print(sum_time)