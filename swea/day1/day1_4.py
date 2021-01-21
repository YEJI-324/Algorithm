import sys

sys.stdin = open("input4.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    v = list(map(int, input().split()))
    m_sum = []
    for i in range(0, n-m+1):
        m_sum.append(sum(v[i:i+m]))
    Min = min(m_sum)
    Max = max(m_sum)
    print("#%d %d" %(test_case,Max-Min))