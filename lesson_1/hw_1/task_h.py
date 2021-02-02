digits = input().split(' ')
digits = list(map(int, digits))

cur_range = [0, 0, 0]
result = []
start = False
for i in range(len(digits)):
    if not start:
        cur_range[0] = digits[i]
    elif cur_range[1:] == [0, 0]:
        if digits[i] != digits[i-1]:
            cur_range[2] = digits[i] - cur_range[0]
        else:
            cur_range[1] = digits[i-1] + 1
            cur_range[2] = 1
            result.append(cur_range.copy())
            cur_range = [digits[i], 0, 0]
    else:
        if digits[i] != digits[i-1] + cur_range[2]:
            if cur_range[2] > 0:
                cur_range[1] = digits[i-1] + 1
            else:
                cur_range[1] = digits[i-1] - 1
            result.append(cur_range.copy())
            cur_range = [digits[i], 0, 0]
    start = True
if start:
    if cur_range[2] == 0:
        cur_range[2] = 1
    if cur_range[2] > 0:
        cur_range[1] = digits[-1] + 1
    else:
        cur_range[1] = digits[-1] - 1
    result.append(cur_range.copy())
for range_i in result:
    print(range_i[0], range_i[1], range_i[2])
