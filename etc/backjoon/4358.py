#백준 4358 생태학
# Red Alder
# Ash
# Aspen
# Basswood
# Ash
# Beech
# Yellow Birch
# Ash
# Cherry
# Cottonwood
# Ash
# Cypress
# Red Elm
# Gum
# Hackberry
# White Oak
# Hickory
# Pecan
# Hard Maple
# White Oak
# Soft Maple
# Red Oak
# Red Oak
# White Oak
# Poplan
# Sassafras
# Sycamore
# Black Walnut
# Willow

# 주어진 각 종의 이름을 사전순으로 출력하고, 그 종이 차지하는 비율을 백분율로 소수점 4째자리까지 반올림해 함께 출력한다.

import sys

input = sys.stdin.readline

trees = {}
num = 0 #전체 종 수

while True:
    tree = input().rstrip()
    if not tree:
        break
    if tree in trees:
        trees[tree] += 1
        num+=1
    elif tree not in trees:
      trees[tree] = 1  
      num+=1

trees = sorted(trees.items())

for tree, value in trees:
    print(tree, "{:.4f}".format(value/num*100))

