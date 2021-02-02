def solution1(arg):
    return list(map())


def solution2(arg):
    return [arg[pos]*(pos + 1) for pos in range(len(arg))]


def solution3(arg):
    return [i for i in arg if i % 3 == 0 or i % 5 == 0]


def solution4(arg):
    return [j for i in arg for j in i]


def solution5(arg):
    return [(d_1, d_2, max_dig) for max_dig in range(5, arg + 1) for d_1 in range(1, max_dig)
            for d_2 in range(d_1, max_dig) if d_1*d_1 + d_2*d_2 == max_dig*max_dig]


def solution6(arg):
    return [[elem + add for elem in arg[1]] for add in arg[0]]


def solution7(arg):
    return [[row[i] for row in arg] for i in range(len(arg[0]))]


def solution8(arg):
    return [[int(dig) for dig in cur_str if dig != ' '] for cur_str in arg]


def solution9(arg):
    return {chr(ord('a') + i): i*i for i in arg}


def solution10(arg):
    return {name[0].upper() + name[1:].lower() for name in {word.lower() for word in arg if len(word) > 3}}


solutions = {
    'solution1': solution1,
    'solution2': solution2,
    'solution3': solution3,
    'solution4': solution4,
    'solution5': solution5,
    'solution6': solution6,
    'solution7': solution7,
    'solution8': solution8,
    'solution9': solution9,
    'solution10': solution10
}

if __name__=='__main__':
    print(solution1('python'))
    print(solution2('python'))
    print(solution3(range(16)))
    print(solution4([[1, 2, 3], [4, 5, 6, 7], [8, 9], [0]]))
    print(solution5(15))
    print(solution6(([0, 1, 2], [0, 1, 2, 3, 4])))
    print(solution7([[1, 2], [3, 4], [5, 6]]))
    print(solution8(["0", "1 2 3", "4 5 6 7", "8 9"]))
    print(solution10(['Alice', 'vova', 'ANTON', 'Bob', 'kAMILA', 'CJ', 'ALICE', 'Nastya']))