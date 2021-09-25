s = input()
l = []
index = 0

for i in range(97,123):
    index_k = 0
    l.append(-1)
    for j in s:
        if chr(i) == j:
            if l[index] ==-1:
                l[index] = index_k
        index_k +=1
    index +=1
            
for k in l:
    print(k, end = " ")