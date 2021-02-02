digits = input().split(' ')
digits = list(map(int, digits))
pmax = [0, 0]
dmax = [0, 0]
zero_count = 0
for digit in digits:
    if digit == 0:
        zero_count += 1
    elif digit > pmax[1]:
        if digit > pmax[0]:
            pmax[1] = pmax[0]
            pmax[0] = digit
        else:
            pmax[1] = digit
    elif digit < dmax[1]:
        if digit < dmax[0]:
            dmax[1] = dmax[0]
            dmax[0] = digit
        else:
            dmax[1] = digit

if pmax[0]*pmax[1] >= dmax[0]*dmax[1]:
    if (pmax == [0, 0]) & (zero_count < 2):
        print(dmax[0], dmax[1])
    elif (pmax[1] == 0) & (dmax[1] == 0) & (zero_count < 1):
        print(dmax[0], pmax[0])
    else:
        print(pmax[1], pmax[0])
else:
    print(dmax[0], dmax[1])
