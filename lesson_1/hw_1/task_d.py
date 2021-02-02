nk_arr = input().split(' ')
result = 0
for i in range(int(nk_arr[1])):
    result += int(nk_arr[0]*(i+1))
print(result)
