# ex07_function.py 함수
# 함수  입력값 ---> 함수 ---> 리턴값
# 1. 일반적인 함수 : 입력값과 리턴값이 있는 함수
def add(a,b):
    print("aaaa")
re = add(10,20)
print(re)
# 2. 입력값이 없는 함수
def printHi():
    print("안녕")

print(printHi())

# 매개변수 지정해서 호출하기
# 매개변수를 지정해서 호출하면 순서에 상관없이 사용할 수 있음
def sub(a,b):
    return a - b

re2 = sub(b=10,a=20)
print(re2)

# 입력값이 몇 개가 될 지 모를 때 *매개변수
# 입력값을 전부 모아서 튜플로 만들어줌
def addMany(*args):
    result = 0
    for i in args:
        result = result+i
    return result

addMany(1,2,3,4,5)
addMany(2,3,4)
print(re3)
print(re4)

# 매개변수에 초기값 설정하기
# def define--->정의하다
def sayMy(name,age,man=True):
    print("나의 이름은 %s입니다." %name)
    print("나의 나이는 %d살 입니다." %age)
    if man :
        print("남자입니다.")
    else :
        print("여자입니다.")

sayMy("김그린",22)
sayMy("이블루",30,False)