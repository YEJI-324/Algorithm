c_num = int(input()) #크레인 수
c_limit = list(map(int, input().split())) #각 크레인의 무게 제한
b_num = int(input()) #박스 수
b_weight = list(map(int, input().split())) #각 박스의 무게

result = 0

temp = []

c_limit.sort(reverse=True)
b_weight.sort(reverse=True)

while b_num>=c_num:
    for i in range(c_num):
        if c_limit[i] >= b_weight[i] : 
            print('temp [{}] = b_weight[{}] = {}'.format(i,i,b_weight[i]))
            temp.append(b_weight[i]) #옮길 박스 저장
        else:
            for j in range(len(b_weight)-1-i):
                if c_limit[i] >= b_weight[i+j] : temp.append(b_weight[i+j]); break
                print(c_limit[i] >= b_weight[i+j])
                print('c_limit[{}] = {}'.format(i,c_limit[i]))
                print('temp [{}] = b_weight[{}] = {}'.format(i,i+j,b_weight[i+j]))
    b_num -= len(temp)
    print(temp)
    b_weight = [x for x in b_weight if x not in temp]
    result += 1 #옮긴 횟수 증가

print(b_weight)

#if b_num<c_num:
#    for i in range(b_num):
        
