n = int(input())
list_word = []

for i in range(n):
    list_word.append(input())

num_group_word = 0

for word in list_word:
    list_ch = []
    state = 1
    for index, ch in enumerate(word):
        if ch not in list_ch:
            list_ch.append(ch)
        elif ch in list_ch:
            if ch != word[index-1]:
                state = 0
                break

    num_group_word += state

print(num_group_word)