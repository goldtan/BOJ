n = int(input())

for i in range(n):
    test_data = list(map(int, input().split()))
    H = test_data[0]
    N = test_data[2]
    if N % H == 0:
        Y = H
        X = N // H
    else:
        Y = N % H
        X = N // H + 1
    print("%d%02d" % (Y, X))
