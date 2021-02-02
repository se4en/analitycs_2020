def solution():
    digits = input().split(' ')
    digits = list(map(int, digits))
    N = int(input())

    result = None
    cur_len = len(digits) + 1

    for i in range(len(digits)):
        for j in range(i + 1, len(digits)):
            cur_sum = sum(digits[i: j])
            if (cur_sum > N) and (j - i < cur_len):
                result = digits[i: j]
                cur_len = j - i
    return result


if __name__ == '__main__':
    solution()
