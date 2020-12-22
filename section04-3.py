# Section04-3
# 파이썬 데이터 타입(자료형)
# 리스트, 튜플
# 리스트(순서있음,중복허용,수정가능,삭제가능)

#선언

a = []
a = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Banana', 'Orange'] #자료형이 달라도 가능
e = [10, 100, ['Pen', 'Banana', 'Orange']] #리스트 안에 리스트 선언가능

# 인덱싱
print(d[-2])
print(d[3])
print(d[0]+d[1])
print(e[2][1])
print(e[-1][-2])
print()

# 슬라이싱
print(d[0:1])
print(e[2][1:3])
print()

# 연산
print(c+d) #리스트 합치기
print(c*3) 
print(str(c[0])+'hi') # c[0]은 정수이기에 문자형으로 바꿔준다

# 리스트 수정, 삭제
c[0] = 77 # c[0] = 1을 77로 바꾸기
print(c)

c[1:2] = [100, 1000, 10000] #c의 1부터 2사이에 100,1000,10000으로 바꾸기
print(c)
c[1] = ['a','b','c']
print(c)
print()

#리스트 삭제
del c[1]
print(c)
del c[-1]
print(c)
print()
print()

# 리스트 함수
y = [5,2,3,1,4]
y.append(6) # 인덱스 마지막에 리스트에 값 추가
print(y)
y.sort() #정렬
print(y)
y.reverse() #역순
print(y)
y.insert(2,'하이') # 인덱스를 지정해서 추가
print(y),
y.remove(2) 
print(y) # del은 인덱스 순서로 삭제하지만 remove일때는 원하는 데이터 값을 삭제한다
y.pop()  # 마지막 원소 출력후 삭제
print(y) #LIFO
ex = [88,77]
y.extend(ex) #y list 와 ex list 결합
print(y)
print()
print()


# 튜플(순서 가능, 중복 가능, 수정 불가능, 삭제 불가능)
# 중요 데이터 저장

a = ()
b = (1,)
c = (1,2,3,4)
d = (10,100,('a','b','c'))

print(c[2])
print(c[3])
print(d[2][0])
print(d[2:])
print(d[2][0:2])
print(c+d)
print(c*3)
print()
print()


# 튜플 함수

z = (5,2,1,3,4,1)

print(z)
print(3 in z) # z튜플안에 3이라는 값이 있는가
print(z.index(3)) # z튜플의 3번째 인덱스 값 출력
print(z.count(1)) # z에 1이 몇개 있는가
