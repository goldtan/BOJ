word = input()
word = str.upper(word)
list_char = list(set(word))

many_count = -5

for i in list_char:
    if many_count < word.count(i):
        many_count = word.count(i)
        state = i
    elif many_count == word.count(i):
        state = "?"

print(state)