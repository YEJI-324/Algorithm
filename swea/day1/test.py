import copy

# 1
# 8
# 3 2 E
# 2 4 S
# 3 4 N
# 1 2 N
# 4 5 S
# 1 1 N
# 5 3 S
# 5 4 W


def main():
    T = int(input())

    for test_case in range(1, T+1):
        N = int(input()) # 차량 수
        car_info = [[3] for _ in range(N)] # 차량 정보
        parking_info = [[0 for _ in range(7)] for _ in range(7)]

        result = 0

        # 주차장 경계
        for i in range(6):
            parking_info[i][0] = -1
            parking_info[0][i] = -1
        for i in range(7):
            parking_info[i][6] = -1
            parking_info[6][i] = -1
            
        visited = copy.deepcopy(parking_info)
        visited_num = []

        for i in range(N): # 주차 정보 세팅
            car_info[i] = list(input().split())
            car_x = int(car_info[i][0])
            car_y = int(car_info[i][1])
            car_direction = car_info[i][2]
            
            if car_direction == 'E':
                parking_info[car_x][car_y] = i+1
                parking_info[car_x][car_y-1] = i+1
            elif car_direction == 'W':
                parking_info[car_x][car_y] = i+1
                parking_info[car_x][car_y+1] = i+1
            elif car_direction == 'S':
                parking_info[car_x][car_y] = i+1
                parking_info[car_x-1][car_y] = i+1
            elif car_direction == 'N':
                parking_info[car_x][car_y] = i+1
                parking_info[car_x+1][car_y] = i+1
        
        def move_car(car_num):
            x = int(car_info[car_num][0])
            y = int(car_info[car_num][1])
            direction = car_info[car_num][2]
            move_cnt = 0
            print("car_num : ", car_num+1)
            print("x는 %d y는 %d" %(x, y))
            visited[x][y] = 1
            visited_num.append(car_num)
            print("direction : ", direction)
            if direction == 'E':
                visited[x][y-1] = 1
                if parking_info[x][y+1] == -1: 
                    # 반대방향으로 이동하기
                    if parking_info[x][y-2] != 0:
                        if visited[x][y-2] != 1:
                            move_cnt += move_car(parking_info[x][y-2] - 1)
                        else: return 0
                    else: 
                        move = 2
                        while parking_info[x][y-move] == 0: 
                            move += 1
                            if parking_info[x][y-move] != -1:
                                print("ㅇㄴ ", parking_info[x][y-move] - 1)
                                move_cnt += move_car(parking_info[x][y-move] - 1)
                            car_info[car_num][0] = x                                
                            car_info[car_num][1] = y-move
                            parking_info[x][y] = 0
                            parking_info[x][y-1] = 0
                            parking_info[x][y-move] = car_num+1
                            parking_info[x][y-move-1] = car_num+1
                elif parking_info[x][y+1] != 0: 
                    if visited[x][y+1] != 1: 
                        move_cnt += move_car(parking_info[x][y+1] - 1)
                    else: return 0
                else: 
                    move = 1
                    while parking_info[x][y+move] == 0:
                        visited[x][y+move] = 1 
                        move += 1  
                        if parking_info[x][y+move] != -1:
                            print("ㅇㄴ ", parking_info[x][y+move])
                            move_cnt += move_car(parking_info[x][y+move]-1)
                        car_info[car_num][0] = x
                        car_info[car_num][1] = y+move
                        parking_info[x][y] = 0
                        parking_info[x][y-1] = 0
                        parking_info[x][y+move] = car_num+1
                        parking_info[x][y+move-1] = car_num+1
            elif direction == 'W':
                visited[x][y+1] = 1
                if parking_info[x][y-1] == -1:
                    #반대 방향으로 이동하기
                    if parking_info[x][y+2] != 0:
                        if visited[x][y+2] != 1:
                            move_cnt += move_car(parking_info[x][y+2] - 1)
                        else: return 0
                    else:
                        move = 2
                        while parking_info[x][y+move] == 0:
                            move += 1
                            if parking_info[x][y+move] != -1:
                                move_cnt += move_car(parking_info[x][y+move] - 1)
                            car_info[car_num][0] = x
                            car_info[car_num][1] = y+move
                            parking_info[x][y] = 0
                            parking_info[x][y+1] = 0
                            parking_info[x][y+move] = car_num+1
                            parking_info[x][y+move+1] = car_num+1
                elif parking_info[x][y-1] != 0:
                    print("call")
                    if visited[x][y-1] != 0:
                        return 0
                    else: 
                        print("call!")
                        move_cnt += move_car(parking_info[x][y-1] - 1)
                        if parking_info[x][y-1] == 0:
                            move = -1
                            while parking_info[x][y+move] == 0:
                                move += 1
                                if parking_info[x][y+move] != -1:
                                    move_cnt += move_car(parking_info[x][y+move])
                                visited[x][y+move] = 1
                                car_info[car_num][0] = x
                                car_info[car_num][1] = y+move
                                parking_info[x][y] = 0
                                parking_info[x][y+1] = 0
                                parking_info[x][y+move] = car_num+1
                                parking_info[x][y+move+1] = car_num+1
                elif parking_info[x][y-1] == 0:
                    move = -1
                    while parking_info[x][y+move] == 0:
                        move += 1
                        if parking_info[x][y+move] != -1:
                            move_cnt += move_car(parking_info[x][y+move])
                        visited[x][y+move] = 1
                        car_info[car_num][0] = x
                        car_info[car_num][1] = y+move
                        parking_info[x][y] = 0
                        parking_info[x][y+1] = 0
                        parking_info[x][y+move] = car_num+1
                        parking_info[x][y+move+1] = car_num+1
            elif direction == 'N':
                visited[x+1][y] = 1
                if parking_info[x-1][y] == -1:
                    #move back ward
                    if parking_info[x+2][y] != 0:
                        if visited[x+2][y] != 1:
                            move_cnt += move_car(parking_info[x+2][y] - 1)
                        else: return 0
                    else:
                        move = 2
                        while parking_info[x+move][y] == 0:
                            move += 1
                            if parking_info[x+move][y] != -1:
                                move_cnt += move_car(parking_info[x+move][y] - 1)
                            car_info[car_num][0] = x+move
                            car_info[car_num][1] = y
                            parking_info[x][y] = 0
                            parking_info[x+1][y] = 0
                            parking_info[x+move][y] = car_num+1
                            parking_info[x+move+1][y] = car_num+1
                elif parking_info[x-1][y] != 0:
                    if visited[x-1][y] == 0:
                        if move_car(parking_info[x-1][y] - 1) == 0:
                            if parking_info[x+2][y] != 0:
                                if visited[x+2][y] != 1:
                                    move_cnt += move_car(parking_info[x+2][y] - 1)
                                else: return 0
                            else:
                                move = 2
                                while parking_info[x+move][y] == 0:
                                    move += 1
                                    if parking_info[x+move][y] != -1:
                                        move_cnt += move_car(parking_info[x+move][y] - 1)
                                    car_info[car_num][0] = x+move
                                    car_info[car_num][1] = y
                                    parking_info[x][y] = 0
                                    parking_info[x+1][y] = 0
                                    parking_info[x+move][y] = car_num+1
                                    parking_info[x+move+1][y] = car_num+1
                        else: 
                            move_cnt += move_car(parking_info[x-1][y] - 1)
                    else: return 0
                else:
                    move = 1
                    while parking_info[x-move][y] == 0:
                        move += 1
                        if parking_info[x-move][y] != -1:
                            move_cnt += move_car(parking_info[x-move][y] - 1)
                        visited[x-move+1][y] = 1
                        car_info[car_num][0] = x-move
                        car_info[car_num][1] = y
                        parking_info[x][y] = 0
                        parking_info[x+1][y] = 0
                        parking_info[x-move][y] = car_num+1
                        parking_info[x-move+1][y] = car_num+1
            elif direction == 'S':
                visited[x-1][y] = 1
                if parking_info[x+1][y] == -1:
                    #move back ward
                    if parking_info[x-2][y] != 0:
                        if visited[x-2][y] != 1:
                            move_cnt += move_car(parking_info[x-2][y] -1)
                        else: return 0
                    else:
                        move = 2
                        while parking_info[x-move][y] == 0:
                            move += 1
                            print("여기")
                            if parking_info[x-move][y] != -1:
                                print("여기 %d %d" %(x-move,y))
                                move_cnt += move_car(parking_info[x-move][y] - 1)
                        car_info[car_num][0] = x-move
                        car_info[car_num][1] = y
                        parking_info[x][y] = 0
                        parking_info[x-1][y] = 0
                        parking_info[x-move+1][y] = car_num+1
                        parking_info[x-move][y] = car_num+1
                elif parking_info[x+1][y] != 0:
                    if visited[x+1][y] != 1:
                        move_cnt += move_car(parking_info[x+1][y] - 1)
                    else: return 0
                else:
                    move = 1
                    while parking_info[x+move][y] == 0:
                        move += 1
                        if parking_info[x+move][y] != -1:
                            move_cnt += move_car(parking_info[x+move][y] - 1)
                        visited[x+move-1][y] = 1
                        car_info[car_num][0] = x+move
                        car_info[car_num][1] = y
                        parking_info[x][y] = 0
                        parking_info[x-1][y] = 0
                        parking_info[x+move][y] = car_num+1
                        parking_info[x+move-1][y] = car_num+1
            
            move_cnt += 1
            print("move cnt : ", move_cnt)
            for j in range(7):
                print(visited[j])
            for j in range(7):
                print(parking_info[j])
            return move_cnt

        result += move_car(0)

        print("#%d %d" %(test_case, result))
    
main()