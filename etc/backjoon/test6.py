def solution(arr):
    result = []
    arr_set = list(set(arr))
    if len(arr) == len(arr_set):
        result.append(-1)
        return result
    else:
        for num in arr_set:
            num_cnt = 0
            for i in range(len(arr)):
                if num == arr[i]:
                    num_cnt += 1
            if num_cnt>1: result.append(num_cnt)
    return result

print(solution([1,2,3,3,3,3,4,4]))
print(solution([3,2,4,4,2,5,2,5,5]))
print(solution([3,5,7,9,1]))