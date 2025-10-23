if 10 == 10:
    print("True1")

a = 10
b = 9

if a == 10:
    print("True2")

if b > a:
    print("True3")

if a > b:
    print("True4")

pwd = True

if pwd:
    print("is True")
else:
    print("is false")


num = 10

if num > 10:
    print("num is big")
elif num < 10:
    print("num is small")
else:
    print("num is 10")

age = int(input("How old are you?")) #input -> 사용자 입력값을 리턴해줌

print(type(age))

if age < 19:
    print("can't age")
elif age >= 19 and age <= 35:
    print("drink beer")
elif age > 35 or age <= 40:
    print("drink soju")
else: 
    print("go ahead")





#################################
x = 10
y = 20

print(x < y)
print( x <= y)
print( x >= y)
print( x > y)

origin_pass =  "1234"
user_pass = input()
if origin_pass == user_pass:
    print("로그인 성공")
elif user_pass == "":
    print("비밀번호를 입력하세요.")
else:
    print("로그인 실패")


now_sub = input("현재 구독자 수를 입력하세요 : ")
if int(now_sub) >= 1000:
    print("수익 창출이 가능 합니다.")
else:
    print("수익 창출이 불가능 합니다.")



stdy_time = input("공부 시간을 입력하세요(시간) : ")
if int(stdy_time) >= 10:
    print("휴대폰 잠금이 해제 됩니다.")
elif int(stdy_time) >= 5:
    print("휴대폰을 30분간 사용 가능합니다.")
else:
    print("휴대폰 사용이 불가능 합니다.")