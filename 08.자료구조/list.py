#변수 = [데이터1, 데이터2, ... 데이터n]
list = ["삼성", "네이버", "SK"]

print(list[0])
print(list[1])
print(list[2])

#list 길이
print(len(list))

num_list = [1,2,3,4,5,6,7,8,9]
print(num_list[0:3])
print(num_list[3:])

#2차원 리스트
game_map = [
    ["대검", "포션", None],
    ["대검2", "포션2", None],
    ["대검3", "포션3", None]
]

for i in list:
    print(i + " 회사 입니다")


print(game_map[0])
print(game_map[0][2])
print(game_map[0][1])
print(game_map[1][1])


scores = [120, 150, 180, 200, 170]
max_score = 0
for i in scores:
    if max_score > i:
        max_score = max_score
    elif max_score < i:
        max_score = i
print("최고점수는 : " + str(max_score))

#max -> list에서 제일 큰 값 찾아줌
print(max(scores))

rooms = [
    [3,1,2],
    [2,0,1],
    [1,3,2]
]

for i in rooms:
    print(i)


print(range(len(rooms)))

total_item = 0
for i in range(len(rooms)):
    #print(i)
    for y in rooms[i]:
        #print(y)
        if y == 0:
            print("아이템이 없습니다.")
        elif y > 0:
            total_item += y
            print(total_item)
print("총 수집한 아이템 수 : " + str(total_item))


#sum -> list 값을 더해줌
total_item2 = 0
for room in rooms:
    total_item2 += sum(room)
print(total_item2)