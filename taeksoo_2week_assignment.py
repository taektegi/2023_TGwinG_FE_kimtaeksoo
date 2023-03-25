# 1번
def sum(a, b):
    print(a+b)
    return
sum(3, 2)

# 2번
def sub(a, b):
    print(a-b)
    return
sub(3, 2)

# 3번
def mul(a, b):
    print(a*b)
    return
mul(3, 2)

# 4번
def div(a, b):
    print(a/b)
    return
div(4, 2)

# 5번
def distance(x1, y1, x2, y2):
    print(((x1-x2)**2+(y1-y2)**2)**(1/2))
    return
distance(1, 2, 3, 4)

# 6번
def title():
    lylics = "Switch sides and I'm beside you."
    print(lylics[21:-1])
    return 
title()

# 7번
def reverseStr(string):
    print(string[::-1])
    return 
reverseStr("Hello")

# 8번
def introduce():
    a=input("이름을 입력하세오 : ")
    b=input("취미를 입력하세요 : ")
    c=input("재학 중인 학교를 입력하세요 : ")
    d=input("생일을 입력하세요 : ")
    print("제이름은 "+a+"입니다. 취미는 "+b+"입니다. 저는"+c+"를 다니고 있습니다. 제 생일은 "+d[2:4]+"월 "+d[4:6]+"일 입니다.")
    return 
introduce()

# 9번
def calc():
    a=input("첫 번째 수를 입력하세요 : ")
    b=input("두 번째 수를 입력하세요 : ")
    a=int(a)
    b=int(b)
    c=a+b
    d=a-b
    e=a*b
    f=a//b
    c=str(c)
    d=str(d)
    e=str(e)
    f=str(f)
    print("두 수의 합 : "+c)
    print("두 수의 차 : "+d)
    print("두 수의 곱 : "+e)
    print("두 수의 몫 : "+f)
    return 
calc()