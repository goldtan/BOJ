N = int(input())
new = []
for _ in range(N):
    new.append(list(map(int,input().split())))

new.sort()

for i in new:
    print(i[0],i[1])

# 이중 리스트 형태일 때는, list[n][0]을 기준으로 정렬