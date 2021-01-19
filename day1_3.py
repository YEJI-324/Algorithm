# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''

import sys

sys.stdin = open("input3.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    a=list(map(int, list(input())))
    cnt_list = [0 for i in range(10)]
    for i in a:
        cnt_list[i] += 1
    max_num = 0
    max_cnt = 0
    for i in range(9, -1, -1):
        if(cnt_list[i]>max_cnt): max_cnt = cnt_list[i]; max_num = i;
    print("#%d %d %d" %(test_case,max_num,max_cnt))