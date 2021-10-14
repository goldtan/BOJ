import sys 

N1 = list(sys.stdin.readline().rstrip('\n'))
rev_N2 = []

M = int(sys.stdin.readline())

for _ in range(M):
    command = sys.stdin.readline().rstrip('\n')
    if command == "L" and len(N1) != 0 :
        rev_N2.append(N1.pop())
    elif command == 'D' and len(rev_N2) != 0 :
        N1.append(rev_N2.pop())
    elif command == 'B' and len(N1) != 0 :
        N1.pop()
    elif "P" in command :
        list_command = list(command)
        N1.append(list_command[2])

rev_N2.reverse()
print(''.join(N1 + rev_N2))


'''
for _ in range(M):
    command = sys.stdin.readline()
    if command == "L\n":
        state = max(state-1, 0)
    elif command == 'D\n':
        state = min(state, len(N))
    elif command == 'B\n':
        if state == 0:
            pass
        else : 
            del N[state]
            state -= 1
    else :
        list_command = list(command)
        N.insert(state,list_command[2])
        state += 1

print("".join(N))
'''

# 시간 초과.. 생각해보니 스택은 안 쓴 듯
# 이를 해결하기 위해 O(1)인 append와 pop을 사용해야 한다고 함.