#ex01_print.py

print("python" "javascript" "java")
print("python" + "javascript" + "java")
print("python", "javascript", "java")
# print 함수 호출 시 end 매개변수에 끝 문자를 지정할 수 있음
# 지정하지 않으면 \n 줄바꿈이 지정되어있음
print(1,end=" ")
print(2)
for i in range(5):
    print(i, end = " ")