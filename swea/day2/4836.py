import sys
sys.stdin = open("input1.txt", "r")

T = int(input())
for test_case in range(1, T + 1):

    palette = [[0 for  i in range(10)]for i in range(10)]
    N = int(input())
    result = 0

    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                if color == 1: # red
                    if palette[r][c] == 0: palette[r][c] = 1 # white -> red
                    elif palette[r][c] == 2: palette[r][c] = 3; result += 1; # blue -> purple
                else: # blue
                    if palette[r][c] == 0: palette[r][c] = 2 # whilte -> blue
                    elif palette[r][c] == 1: palette[r][c] = 3; result += 1;
    
    print("#{} {}".format(test_case, result))