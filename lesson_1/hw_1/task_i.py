import sys


def safe_input():
    try:
        return input()
    except EOFError:
        sys.exit(0)


def ask(questions):
    global balance
    balance -= (len(questions) + 10)
    for q in questions:
        print(f'? {q}')
    print('+', flush=True)
    answers = []
    for _ in range(len(questions)):
        answers.append(int(safe_input()))
    return answers


def generate_q(a, b):
    return [int((b - a) * (i + 1) / 10 + a) for i in range(10)]


def update_ab(a, b, answers):
    i = answers.index(1)
    dif = int((b - a) / 10)
    a = a + i * dif
    b = a + dif
    return a, b


if __name__ == '__main__':
    balance = 100
    a = 0
    b = 100000
    quest = generate_q(a, b)
    while (balance > 0) & (b - a > 10):
        answ = ask(quest)
        if sum(answ) == 0:
            print(f'! {100000}')
            sys.exit(0)
        a, b = update_ab(a, b, answ)
        quest = generate_q(a, b)
    answ = ask(quest)
    print(f'! {a + answ.index(1)}')
