# your code 를 지우고 코드를 작성하세요.
# 5주차 과제에는 출력이나 입력을 요구하는 문제가 없습니다. print(), input() 사용하지 마세요.
# 코드 실행 시 컴파일 에러, 런타임 에러가 발생하면 해당 문제 0점 처리하겠습니다.
# 함수 이름 변경하지 마세요. 변경 시 해당 문제 0점 처리 하겠습니다.
# result, answer 변수를 사용하여 문제를 풀이하세요. 반환값은 result나 answer 변수입니다.
# 제출 기한: 2023년 4월 17일 23시 59분
# 지각 제출 기한: 2023년 4월 18일 23시 59분

def calcCircleArea(r):
    result = float()
    result=r**2*3.14
    return result

def calcLog(a, b):
    import math
    result = float()
    result=math.log(b,a)
    result=round(result,2)
    return result

def calcSin(x):
    import math
    result = float()
    result=math.sin(x)
    result=round(result,2)
    return result

def calcFactorial(x):
    import math
    result = int()
    result=math.factorial(x)
    return result

def calcCombination(n, r):
    import math
    result = int()
    result=math.comb(n, r)
    return result

def calculator(order):
    answer = 0
    if len(order.split())==3:
        a=float(order.replace('e','2.72').split()[1])
        b=float(order.split()[-1])
    else:
        c=float(order.split()[-1])
    if order.find('원넓이')==0:
        answer=calcCircleArea(c)
    elif order.find('로그')==0:
        answer=calcLog(a, b)
    elif order.find('사인')==0:
        answer=calcSin(c)
    elif order.find('팩토리얼')==0:
        answer=calcFactorial(int(c))
    elif order.find('조합')==0:
        answer=calcCombination(int(a), int(b))
        
    return answer

print(calculator("원넓이: 10"))
print(calculator("로그: e 10"))
print(calculator("사인: 100"))
print(calculator("팩토리얼: 5"))
print(calculator("조합: 3 2"))
