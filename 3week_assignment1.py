# 1번
def grade(score):
    if score >= 90 :
        return 'A' 
    elif score >= 80 : 
        return 'B'
    elif score >= 70 : 
        return 'C'
    elif score >= 60 : 
        return 'D' 
    else :
        return 'F'



# 2번
def quadrant(x, y):
    if x>0 and y>0 :
        return '제 1사분면'
    elif x<0 and y>0 :
        return '제 2사분면'
    elif x<0 and y<0 :
        return '제 3사분면'
    elif x>0 and y<0 :
        return '제 4사분면'
 

# 3번
def leapYear(year):
    if year%4!=0 or (year%100==0 and year%400!=0):
        return '윤년이 아닙니다.'
    else :
         return '윤년입니다.'


# 4번
def dice(a, b, c):
    
    if a==b==c :
        return 10000+1000*a
    elif a==b :
        return 1000+100*a
    elif b==c :
        return 1000+100*b
    elif c==a :
        return 1000+100*c
    else :
        return 100*max(a,b,c)
   


# 5번
def alarm(time):
    hour = time//100
    m = time - hour * 100
    if m > 45 :
        m-=45
        return str(hour)+'시'+str(m)+'분'
    else :
        m=15+m
        hour=hour-1
        if hour==-1 :
            hour+=24
            return str(hour)+'시'+str(m)+'분'
        else :
            return str(hour)+'시'+str(m)+'분'


