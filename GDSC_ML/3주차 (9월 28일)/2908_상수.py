A, B = input().split()
A = int("".join(reversed(A)))
B = int("".join(reversed(B)))

print(max(A, B))

# reverse는 list타입에서 제공하는 함수
# revresed는 내장함수, reversed object를 리턴 join 함수와 함께 사용
