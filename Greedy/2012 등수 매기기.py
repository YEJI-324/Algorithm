# 백준 2012 등수 매기기

import sys

def sort_expect_rank_asc(before):
    before.sort()

def get_dissatisfaction(expect_rank):
    result = 0

    for i, rank in enumerate(expect_rank):
        index = i + 1
        result += abs(rank - index)
    
    return result

def solution():
    student_num = int(sys.stdin.readline())
    expect_rank = []
    for _ in range(student_num):
        expect_rank.append(int(sys.stdin.readline()))

    sort_expect_rank_asc(expect_rank)
    dissatisfaciton = get_dissatisfaction(expect_rank)
    print(dissatisfaciton)

solution()