#sw expert academy
#1일차 - 전기버스


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

sys.stdin = open("input2.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    K, N, M = map(int, input().split()) # K: 최대 이동 정류장 수/ N: 종점/ M: 충전기 수
    arr = list(map(int, input().split())) # arr: 충전기가 있는 정류장 번호
    move = K # move: 남은 이동 수
    cnt = 0; # cnt: 충전 횟수
    j = 0
    for i in range (0, N):
        move -= 1
        if(move<0) : break;
        if(i == arr[j] & move < arr[j+1]-arr[j]): cnt += 1; move += K;
        j += 1
    print("#%d %d %d" %(test_case, cnt, move))
