import sys

n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

m = int(input())
m_list = list(map(int, input().split()))

def binary(target, arr, start, end):
    if(start>end):
        return 0

    mid = (start+end)/2

    if(target == arr[mid]):
        return 1
    elif(target<arr[mid]):
        binary(target, arr, start, mid-1)
    else:
        binary(target, arr, mid+1, end)

for target in m_list :
    print(binary(target, n_list, 0, len(n_list)-1))
#
#첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 
# 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 
# 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 
# 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 
# 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.
#
#M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.
#
#5
#4 1 5 2 3
#5
#1 3 7 9 5

# N = int(input())
# A = []

# for _ in range(N):
#     A.append(int(input())


# print(A[0])
