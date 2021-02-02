n = int(input())
list_1 = []
counter = 0
for elem in input().split(' '):
    if not (elem in list_1):
        list_1.append(elem)
        print(elem, end=' ')
    else:
        counter += 1
print('\n', counter, sep='')
