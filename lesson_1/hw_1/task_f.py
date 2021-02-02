import sys

line_1 = input().split(' ')
line_2 = input().split(' ')
dict_1 = dict()
for w in line_1:
    w_l = w.lower()
    if w_l in dict_1:
        dict_1[w_l] += 1
    else:
        dict_1[w_l] = 1
for word in line_2:
    word_l = word.lower()
    if word_l in dict_1:
        if dict_1[word_l] >= 1:
            dict_1[word_l] -= 1
        else:
            print('NO')
            sys.exit(0)
    else:
        print('NO')
        sys.exit(0)
print('YES')
