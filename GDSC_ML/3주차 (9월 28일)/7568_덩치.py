n = int(input())

person = []
rank_list = []
for i in range(n):
    person.append(list(map(int,input().split())))
    rank_list.append(0)

for index in range(n):
    rank = 1
    index_kg=person[index][0]
    index_cm=person[index][1]

    for kg, cm in person:
        if kg > index_kg and cm > index_cm :
            rank += 1
    print(rank)

# 처음에 했던 시도는 1위부터 5위를 정하려고 하였는데 쉽지 않았음
