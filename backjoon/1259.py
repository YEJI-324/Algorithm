num = int(input())

while num != 0:
    num = str(num)
    num_len = len(num)
    cnt = 0
    for i in range(int(num_len/2)):
        if num[i] == num[num_len-1-i]: cnt += 1
    if cnt == int(num_len/2) : print('yes')
    else: print('no')
    num = int(input())