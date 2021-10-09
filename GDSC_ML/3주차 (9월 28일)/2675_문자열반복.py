n = int(input())

for i in range(n):
    sum = ""
    a = input().split()
    for i in a[1]:
        sum += i*int(a[0])
    print(sum)
