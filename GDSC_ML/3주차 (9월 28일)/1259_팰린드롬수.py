a=[]

while True:
    num = input()

    if num =="0":
        break
    i=0
    while len(num)//2 > i:
        
        if(num[i]!=num[-(i+1)]):
            a.append("no")

            break

        if len(num)//2<i+2:
            a.append("yes")
        i+=1

for i in a:
    print(i)