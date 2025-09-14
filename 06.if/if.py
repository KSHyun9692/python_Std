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