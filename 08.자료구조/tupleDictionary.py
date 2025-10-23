#tuple : 변수 = (데이터, 데이터, ....., 데이터)
leg_day = ("스쿼트", "런지", "레그컬")
#print(leg_day)


#dictionary : 변수 = {'':222, '':222, '':333}
price = {
    '사과' : 1000,
    '배' : 2000,
    '오렌지' : 3000,
    '수박' : 4000
}
#print(price)
#print(price['사과'])

for key in price.keys():
    print(key)

for value in price.values():
    print(value)

for key,value in price.items():
    print(key, value)



stock_price = {
    '삼성전자' : [81000, 81500, 82000],
    'SK하이닉스' : [140000, 141000, 139500],
    '네이버' : [350000, 355000, 345000]
}

for key,value in stock_price.items():
    #print(value)
    print(f"{key} 평균 주식 가격 : {int(sum(value) / len(value))}")


stock_info = {
    '삼성전자' : {'최고가' : 85000, '최저가':80000, '현재가':82000},
    'SK하이닉스' : {'최고가' : 145000, '최저가':1390000, '현재가':140500},
    '네이버' : {'최고가' : 360000, '최저가':340000, '현재가':350000}
}


max_value = 10
min_value = 0

for key,value in stock_info.items():
    #print(key)
    #print(value)
    for key2,value2 in value.items():
        #print(key2)
        #print(value2)
        if(key2 == "최고가"):
            max_value = value2
            #print(f"{key} 의 최고가 : {max_value}")
        if(key2 == "최저가"):
            min_value = value2
            #print(f"{key} 의 최저가 : {min_value}")
    print(f"{key} - 최고가 : {max_value}, 최저가 : {min_value}")


for key,value in stock_info.items():
    max_value = value['최고가']
    min_value = value['최저가']
    print(f"{key} - 최고가 : {max_value}, 최저가 : {min_value}")