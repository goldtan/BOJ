n_test = int(input())

while n_test:
    s = input()
    score = 1
    tot = 0
    for i in s:
        if i == 'O':
            tot+= score
            score += 1
        else:
            score = 1
    print(tot)
    n_test -= 1