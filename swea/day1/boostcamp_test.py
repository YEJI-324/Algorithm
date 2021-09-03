def solution(numbers, hand):
    left_cur = 10
    right_cur = 12
    answer = ''
    
    def which_hand(num):
        left_temp = left_cur + 1
        right_temp = right_cur + 1
        left_temp = abs(left_temp - num)
        right_temp = abs(right_temp - num)
        if left_temp < right_temp: # 왼손
            answer += "L"
            left_cur = num
        elif left_temp > right_temp: # 오른손
            answer += "R"
            right_cur = num
        else: # 왼손 = 오른손
            if hand == 'left':
                answer += "L"
                left_cur = num
            elif hand == 'right':
                answer += "R"
                right_cur = num
    
    for i in range(len(numbers)):
        if numbers[i] == 0: # 0일 때
            which_hand(11)
        elif numbers[i] % 3 == 0: # 3 6 9
            answer += "R"
            right_cur = numbers[i]
        elif numbers[i] % 3 == 1: # 1 4 7
            answer += "L"
            left_cur = numbers[i]
        elif numbers[i] % 3 == 2: # 2 5 8
            which_hand(numbers[i])
    
    return answer