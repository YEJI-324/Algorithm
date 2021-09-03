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