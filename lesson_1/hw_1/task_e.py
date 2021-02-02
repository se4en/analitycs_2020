n = int(input())
result = dict()
for i in range(n):
    new_word = input()
    s_new_word = tuple(sorted(new_word))
    if s_new_word in result:
        result[s_new_word].append(new_word)
    else:
        result[s_new_word] = [new_word]

for key in result:
    for lex in result[key]:
        print(lex, end=' ')
    print()
