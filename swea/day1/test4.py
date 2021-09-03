import math

def main():
    T = int(input()) # test case

    for test_case in range(1, T+1):
        ring_num, kan_num = map(int, input().split())
        lock_state = []
        click_cnt = 0

        destination_index = 0
        destination_max = 0

        for i in range(kan_num):
            lock_state.append(list(input()))
            if lock_state[i].count('1') > destination_max:
                destination_max = lock_state[i].count('1')
                destination_index = i

        for i in range(ring_num):
            if lock_state[destination_index][i] != '1':
                j = 1
                while lock_state[destination_index+j][i] != '1' and lock_state[destination_index-j][i] != '1':
                    j+=1
                click_cnt += j
                    
        print("#%d %d" %(test_case, click_cnt))

main()