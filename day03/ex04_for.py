# ex04_for.py

list1 = ["one","two","three"]
for i in list1:
    print(i)
    
for i in "green":
    print(i)
    
marks = [90,50,67,70,80]
number = 0
for stu in marks:
    if stu >= 70:
        print("%d번 학생은 합격입니다." %number)
    else :
        print("%d불합격입니다." %number)
        
print(list(range(1,10,2)))

# range()함수 range(stop), range(start,stop), range(start,stop,step)
sum = 0
for i in range(1,11):
    sum = sum + i
print('1~10까지 더한 수는 %d이다.' %sum)

# for와 range를 사용해서 구구단 출력
# 2단 9단까지 출력
# 2 * 1 = 2, 2 * 2 = 4.... 2 * 9 = 18
# ...
# 9 * 1 = 9, ... 9*9=81
for i in range(2,10):
    for j in range(1,10):
        print('%d * %d = %d' %(i,j,i*j))