short = []

for _ in range(9):
    short.append(int(input()))



short.sort()
break_point = 8
for i in short:
    if break_point == 0:
        break_point -= 1
        break
    for j in short:
        if break_point == 1:
            break_point -= 1
            break
        if sum(short) - i - j == 100:
            for k in short:
                if i != k and j != k:
                    print(k)
                    break_point -= 1