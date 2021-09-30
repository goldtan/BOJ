while True:
    a = input()
    if a =="0":
        break
    state = "yes"
    for index, i in enumerate(a):
        if a[-(index+1)] != i:
            state = "no"
            break

    print(state)

# reverse_character를 사용해도 풀 수 있음 reverse_sentence += char 
# 자료구조 스택을 사용해도 쉬울 것 같음