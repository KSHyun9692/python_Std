#for 변수 in range(반복횟수):
#for i in range(2):
    #print(i)
    #print("말티즈")
    #print(f"{i+1}번 시작")

#for 변수 in range(start,end):
#for i in range(1,4):
    #print(i)
    #print("말티즈")
    #print(f"{i+1}번 시작")

#for 변수 in range(start,end,step):
#for i in range(1,10,2):
    #print(i)
    #print("말티즈")
    #print(f"{i+1}번 시작")


for i in range(3):
    print(f"{i+1}번째 강아지")
    print("강아지를 위한 장난감 준비 중")
    print("장난감 준비 완료\n")

for i in range(1,4):
    print(f"{i}번째 강아지")
    print("강아지를 위한 장난감 준비 중")
    print("장난감 준비 완료\n")



total = 0
for i in range(1,11):
    total += i
print(total)

total2 = 0
for i in range(10):
    total2 += i + 1
print(total2)



#while 조건:
i = 0
while i < 3:
    print(i)
    print("True")
    i += 1


dan = input("구구단 실행 할 단을 입력해 주세요 : ")
for i in range(1,11):
    print(dan + " * " + str(i) + " = " + str(int(dan)*i))


dan4 = int(input("구구단 실행 할 단을 입력해 주세요 : "))
for i in range(1,11):
    print(f"{dan4} * {i} = {dan4*i}")

dan3 = input("구구단 실행 할 단을 입력해 주세요 : ")
for i in range(10):
    print(dan3 + " * " + str(i+1) + " = " + str(int(dan3)*(i+1)))

dan2 = input("구구단 실행 할 단을 입력해 주세요 : ")
end = 1
while end < 11:
    print(dan2 + " * " + str(end) + " = " + str(int(dan2)*end))
    end += 1



#while True:
#   if 조건:
#       break

password = "1234"

while True:
    user_pass = input("비밀번호를 입력하세요 : ")

    if password == user_pass:
        print("로그인 성공")
        break
    print("로그인 실패")


while True:
    user_pass = input("비밀번호를 입력하세요 : ")

    if password == user_pass:
        print("로그인 성공")
        break
    else:
        print("로그인 실패")