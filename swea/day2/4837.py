import sys
import copy
sys.stdin = open("input2.txt", "r")

T = int(input())


def subset(a, n, k):
    result = 0
    if n == 1:
        for i in range(len(a)): 
            if a[i] == k: result += 1
    else:
        for i in range(len(a)):
            temp = copy.deepcopy(a)
            temp.remove(temp[i])
            result += subset(temp, n-1, k-a[i])
    return result

for test_case in range(1, T + 1):
    nums = [i for i in range(1, 13)] # 1~12 list
    N, K = map(int, input().split())
    print("#{} {}".format(test_case, subset(A, N, K)))
    