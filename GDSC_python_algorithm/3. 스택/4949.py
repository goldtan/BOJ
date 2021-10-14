import sys

while True:
    a = sys.stdin.readline()
    if a == ".\n":
        break
    stack_a = []
    list_a = list(a)
    for i in list_a:
        if i == "(" or i == ")" or i == "[" or i == "]" :
            if len(stack_a) == 0 and (i == ")" or i == "]"):
                stack_a.append(i)
                break
            stack_a.append(i)
            if (i == "]" and stack_a[-2] =="[") or (i == ")" and stack_a[-2] =="("):
                stack_a.pop()
                stack_a.pop()
    if len(stack_a) ==0:
        print("yes")  
    else : print("no")