words_num = int(input())
words_list = []

for _ in range(words_num):
    word = str(input())
    words_list.append((word, len(word)))
    
words_list = list(set(words_list)) # 집합(set)은 중복 안됨 -> 리스트에서 중복 제거할 때 set으로 바꾼 뒤 다시 list로 타입 변환하기

words_list.sort(key=lambda word: (word[1], word[0])) # key지정해서 정렬하는 방법

for i in range(len(words_list)):
    print(words_list[i][0])