while True :
    try:
        print(input())
    except EOFError: # EOFError
        break

'''
나의 코드는 
계속 EOFError 발생

i = 100

while i:
    a = input()
    if "" in a:
        break
    print(a)
    i-=1
'''
