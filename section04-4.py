# Section04-4
# 파이선 데이터 타입(자료형)
# 딕셔너리, 집합 자료형

# 딕셔너리(Dictionary) : 순서x, 중복x, 수정o, 삭제o

# Key, Value (Json) -> MongoDB
# 선언
# name = Key, Kim = Value
a = {'name': 'Kim', 'Phone' : '010-1234-5678', 'birth': 870214}
b = {0: 'Hello Python', 1: 'Hello Coding'}
c = {'arr' : [1,2,3,4,5]}



# print(type(a))

# 출력
print(a['name']) # a의 name이라는 키의 값을 가져와라 만약에 키가 없을 경우 오류
print(a.get('name')) ## a의 name이라는 키의 값을 가져와라 만약에 키가 없을 경우 None 으로 뜸
print(a.get('address'))
print(c['arr'][1:3])
print()

# 딕셔너리 추가
a['address'] = 'Seoul' # address 라는 이름의 키와 Seoul이라는 Value추가
print(a)
a['rank'] = [1, 3, 4]
a['rank2'] = (8, 7, 66)
print(a)
print()

# keys, values, items
#keys
print(a.keys())
print(list(a.keys()))

temp = list(a.keys())
print(temp[1:3])
print()

#values
print(a.values())
print(list(a.values()))
print()
print()


#items
print(a.items())
print()
print(list(a.items()))
print()
print(2 in b)
print()
print()


# 집합(Sets) (순서x, 중복x)

a = set()
b = set([1,2,3,4])
c = set([1,4,5,6,6])

print(type(a))
print(c)

t = tuple(b)
print(t)
l = list(b)
print(l)

print()
print()

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print(s1.intersection(s2)) # 교집합
print(s1 & s2)

print(s1 | s2) # 합집합
print(s1.union(s2))

print(s1-s2) # 차집합
print(s1.difference(s2))
print()
print()

# 추가 & 제거
s3 = set([7,8,10,15])

s3.add(18)
# s3.add(7) 중복이라 추가 안됨
print(s3)

s3.remove(15)
print(s3)

print(type(s3))