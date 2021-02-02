def dig_sum(number):
    result = 0
    while (number//10 > 0):
        result += number % 10
        number //= 10
    result += number
    return result


if __name__ == '__main__':
    n = int(input())
    dict_1 = {}
    for elem in list(map(int, input().split(' '))):
        if dig_sum(elem) in dict_1:
            dict_1[dig_sum(elem)].append(elem)
        else:
            dict_1[dig_sum(elem)] = [elem]
    keys_list = sorted(list(dict_1.keys()))
    for key in keys_list:
        list_1 = sorted(dict_1[key])
        for dig in list_1:
            print(dig, end=' ')
