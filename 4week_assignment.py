# # your code 를 지우고 그 부분에 본인의 코드를 작성해주세요.
# 4주차 과제에는 출력이나 입력을 요구하는 문제가 없습니다. print(), input() 사용하지 마세요.
# 코드 실행 시 컴파일 에러, 런타임 에러가 발생하면 해당 문제 0점 처리하겠습니다.
# 함수 이름 변경하지 마세요. 변경 시 해당 문제 0점 처리 하겠습니다.
# 제출 기한 : 2023년 4월 10일 23시 59분
# 지각 제출 기한 : 2023년 4월 11일 23시 59분

# 1번
def double(lst):
    n=0
    for i in lst:
        for j in lst:
            if i==2*j:
                n+=1
            else :
                pass
    return n



# 2번
def pascal(n):
    if n==1:
        return [1]
    elif n>=2:
        N=[]
        for i in range(0,n-1):
            a,b,c,d=1,1,1,1
            for j in range(2, n):
                a=a*j
            for k in range(2, i+1):
                b=b*k
            for p in range(2, n-i):
                c=c*p
            d=a/(b*c)
            d=int(d)
            N.append(d)
        N.append(1)
        return N

# 3번
def beerRefrigerator(n):
    a=2
    r=[1]
    q=[]
    b=[]
    while n>=a:
        if n%a==0:
            r.append(a)
            a+=1
        else :
            a+=1
    for i in r: 
        for j in r:
            for k in r:
                if i*j*k==n:
                    q.append([i,j,k])
                else:
                    pass
    for i in q:
        i[0],i[1],i[2]=int(i[0]), int(i[1]), int(i[2])              
        b.append((i[0]*i[1])+(i[1]*i[2])+(i[2]*i[0]))
    e=min(b)
    for i in q:
        if (i[0]*i[1])+(i[1]*i[2])+(i[2]*i[0])==e:
            w=f'{i[0]} X {i[1]} X {i[2]}'

    return w
    
# 4번
def matrixMul(mat1, mat2):
    lst3=[]
    for i in range(len(mat1)):
        lst2=[]
        for j in range(len(mat2[0])):
            lst1=[]
            for k in range(len(mat1[0])):
                lst1.append(mat1[i][k]*mat2[k][j])
            lst2.append(sum(lst1))
        lst3.append(lst2)
    
    return lst3
