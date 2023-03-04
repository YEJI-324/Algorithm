# 백준 4375번 1

while True:
    try:
        n = input()

        if n == '': break;
        else: n = int(n)

        cnt = 1
        num = 0

        while True:
            num = num * 10 + 1
            num %= n

            if num == 0:
                result = cnt
                break;
            else:
                cnt += 1

        print(result)
    except EOFError:
        break