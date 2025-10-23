#def 함수이름(매개변수1, 매개변수2, ...... ):
#   내용
#   return 반환값

def first_function():
    print("hello")

first_function()

def first2_function(name, age):
    print("hello my name is ", name, " age is ", age)

first2_function("KSH",23)

def first3_function(name="ksh", age=23, test="test"):
    print("hello my name is ", name, " age is ", age, "test ", test)

first3_function()

def plus(a=0, b=0):
    print(a + b)

def minus(a=1, b=0):
    print(a - b)

def multiply(a=0, b=0):
    print(a * b)

def divide(a=0, b=1):
    print(a / b)

def power(a=0, b=1):
    print(a ** b)

plus(3, 4)
minus(5, 3)
multiply(2, 8)
divide(6, 3)
power(3, 3)

plus()
minus()
multiply()
divide()
power()

def tax_calc(money):
    return money * 0.35

def pay_tax(tax):
    print("you pay ", tax)

to_pay = tax_calc(150000000)
pay_tax(to_pay)

name = "ksh"
age = 23
eye = "black"

print(f"Hello my name is {name} i have {age} years in the earth, {eye} is my eye color")



def easy_recipe(a, b):
    print(f"{a} 와 {b}를(을) 이용해서 요리를 시작합니다.")
    result = a + b + '볶음밥'
    print("요리 완료")
    return result

dish = easy_recipe("라면", "치즈")
print(dish)


def cal_avg_gold(a, b, c):
    avg = (a + b + c) / 3
    return avg

teamGold = cal_avg_gold(12000, 15000, 18000)
print(teamGold)

def cal_kda(kill, deth, assist):
    a = (kill + assist) / deth
    return a

kda = cal_kda(10, 2, 7)
print(kda)