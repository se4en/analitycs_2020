def def_of_normal_man(digit):
    result = 0
    global amount
    while amount >= digit * 0.9999:
        result += 1
        amount -= digit
    return result


if __name__ == '__main__':
    amount = float(input())
    money = {
        10.0: 0,
        5.00: 0,
        2.00: 0,
        1.00: 0,
        0.50: 0,
        0.10: 0,
        0.05: 0,
        0.01: 0
    }
    for key in money.keys():
        money[key] = def_of_normal_man(key)
        if money[key] > 0:
            print(f'{key:5.2f}\t{money[key]}')
