a = input()
num_a = len(a)

for index, ch in enumerate(a):
    if ch == "-":
        num_a -= 1
    elif ch == "=":
        if a[index-2] == "d" and a[index-1] == "z":
            num_a -= 2
        else :
            num_a -= 1
    elif ch == "j":
        if a[index-1] == "l" or a[index-1] == "n":
            num_a -= 1

print(num_a)