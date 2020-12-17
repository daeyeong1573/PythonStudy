# 데이터 타입

v_str1 = "Niceman"
v_bool = True # True = 1 False = 0
v_str2 = "Goodboy"
v_float = 10.4
v_int = 7
v_dict = {
    "name" : "Kim",
    "age" : 25
}

v_list = [3,5,7]
v_tuple = 3,5,7
v_set = {7,8,9}

print(type(v_tuple))
print(type(v_list))
print(type(v_set))
print(type(v_str1))
print(type(v_int))
print(type(v_float))
print(type(v_bool))

i1 = 39
i2 = 939
big_int1 = 999999999999
big_int2 = 777777777777
f1 = 1.234
f2 = 3.784
f3 = .5
f4 = 10.

print(i1 * i2)
print(big_int1 * big_int2)
print(f1 ** f2)
#자동 형변환
print(f3 + i2)
result = f3+i2

print(result,type(result))
print()
a = 5.
b = 4
c = 10

print(type(a), type(b))
result2 = a + b
print(result2)
print()

# 형변환
# int, float, complex(복소수)

print(int(result2))
print(float(c))
print(complex(3))
print(int(True))
print(int(False))
print(int('3'))
print(complex(False))

print()
# 단항 연산자
y = 100
y += 100
print(y)
print()

# 수치 연산 함수
# https://docs.python.org/3/library/math.html #파이썬 공식 링크

print(abs(-7))
n,m = divmod(100 , 8)
# n = 몫 m = 나머지
print(n,m)
print()

import math

print(math.ceil(5.1)) #5.1보다 큰정수 중 가장 작은수
print(math.floor(3.784)) #3.784보다 작은정수 중 가장 작은수