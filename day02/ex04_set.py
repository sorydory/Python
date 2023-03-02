# 집합 자료형 파이썬2.3부터 지원
# 집합 자료형 특징 : 중복을 허용하지 않음, 순서가 없다(인덱싱 안 됨)
s1 = set([1,2,3,4,5])
s2 = set("hello")
print(s1)
print(s2)
print(list(s2))
s3 = set([1,2,1,3,5,4,5,2])
print(s3)
l3 = list(s3)
print(l3)

# 집합 관련 함수
# 교집합 집합1&집합2, 집합1.intersection(집합2)
numberset1 = set([1,2,3,4,5,6])
numberset2 = set([4,5,6,7,8,9])
print(numberset1 & numberset2)
print(numberset1.intersection(numberset2))

# 합집합 집합1 | 집합2, 집합1.union(집합2)
print(numberset1 | numberset2)
print(numberset1.union(numberset2))

# 차집합 집합1- 집합2, 집합1.difference(집합2)
print(numberset1 - numberset2)
print(numberset1.difference(numberset2))

# 값 1개 추가하기 add()
numberset1.add(20)
print(numberset1)

# 값 여러개 추가하기 update()
numberset1.update([100,200,300])
print(numberset1)

# 특정 값 제거하기 remove(value)
numberset1.remove(100)
print(numberset1)
