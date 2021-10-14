import sys

n = int(sys.stdin.readline())
# num_list = []
# for _ in range(n):
#     num_list.append(int(sys.stdin.readline()))
num_list = [int(sys.stdin.readline()) for _ in range(n)]

num_stack = []
#op_list = []

BREAK_POINT = 2
index = num_list[0] + 1

for idx, i in enumerate(num_list):
    if BREAK_POINT == 1:
        break
    
    if len(num_stack) != 0:
        if i == n:
            for _ in (index, i+1):
                num_stack.append(index)
                index += 1
                print("+")
            for _ in range(n - idx):
                idx += 1
                if num_stack.pop() != num_list[idx]:
                    print("NO")
                    BREAK_POINT =1
                    break
                num_stack.pop()
                print("-")

            BREAK_POINT -= 1
            break

        elif i == num_stack[-1]:
            num_stack.pop()
            print("-")

        elif i != num_stack[-1]:
            for _ in (index, num_stack[-1]):
                num_stack.append(index)
                index += 1
                print("+")
            num_stack.pop()
            print("-")
        

    else :
        for j in range(1,num_list[0]+1):
            num_stack.append(j)
            print("+")
        j += 1
        num_stack.pop()
        print("-")


#op_list.append("-")

# 첫번째 값 출력
#for i in range(1,num_list[0]+1):
#    num_stack.append(i)
#    op_list.append("+")
