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