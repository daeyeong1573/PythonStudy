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