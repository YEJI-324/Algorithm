#sw expert academy
#1일차 - min max

import sys

sys.stdin = open("input1.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
        N = int(input())
        arr = list((map(int, input().split())))
        Min = min(arr)
        Max = max(arr)
        print("#%d %d" %(test_case,Max-Min))