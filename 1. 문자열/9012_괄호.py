n = int(input())

def is_ps (ps):
    num_left, num_right = 0, 0
    state = "YES"
    for i in ps:
        if num_left >= num_right:
            if i == "(":
                num_left +=1
            elif i == ")":
                num_right +=1
        else:
            state = "NO"
            break
        
    if num_left == num_right:
        print(state)
    else:
        print("NO")
        
for i in range(n):
    is_ps(input())