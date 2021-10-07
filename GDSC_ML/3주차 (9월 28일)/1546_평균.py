n = int(input())

num_list = input().split()
new_list = []
sum = 0
max_num = int(max(num_list))

for index, i in enumerate(num_list):
    new_num = int(i) / max_num * 100
    new_list.append(new_num)
    sum += new_list[index]

print(sum/n)

# 실제 정답과 출력값의 절대오차 또는 상대오차가 10-2 이하 ?4