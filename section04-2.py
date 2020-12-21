# Section04-2
# 문자열, 문자열연산 , 슬라이싱

str1 = "I am Boy"
str2 = "NiceMan"
str3 = " "
str4 = str('abc')

print(len(str1), len(str2), len(str3), len(str4)) # len > 문자열 길이(공백도 셈)
print()

escape_str1 = "Do you have a \"big collection\""
print(escape_str1)

escape_str2 = "tab\ttab\ttab"
print(escape_str2)

#Raw String **
raw_s1 = r'C:\Programs\Test\Bin'
print(raw_s1) 
raw_s2 = r'a\\a\aa'
print(raw_s2)
print()





# 멀티라인

multi = \
"""
문자열
멀티라인
테스트
"""
print(multi)

# 문자열 연산
str_o1 = "*"
str_o2 = "abc"
str_o3 = "def"
str_o4 = "NiceMan"

print(str_o1 * 100)
print(str_o2 + str_o3)
# print(str_o1 + 3) #문자열 + 정수는 더할수 없음
print(str_o1 * 3)
print('a' in str_o4) # a라는 문자가 str_o4에 포함되어 있는가
print('f' not in str_o4) # f라는 문자가 str_o4에 포함되어 있지 않는가

# 문자열 형 변환
print(str(77)+'a') #77이 문자열 형태로 형변환되어 가능
print(str(10.4))
print()

#문자열 함수
# 참고 : https://www.w3schools.com/python/python_ref_string.asp

# a = 'niceman'
# b = "Orange"

# print(a.islower()) # a가 모두 소문자인가?
# print(b.endswith('e')) # b의 끝 글자가 e라는 문자가 있는가?(대소문자 구분)
# print(a.capitalize()) #첫 글자를 대문자로 
# print(a.replace('nice', 'good')) #nice를 good로 교환
# print(list(reversed(b))) #리스트 형식으로 역순으로 출력

# 문자열 슬라이싱
a = 'niceman'
b = 'orange'
# 문자의 길이 측정할땐 0부터 셈
print(a[0:3])# 0부터3번째 전 글짜 출력 즉 nic 
print(a[0:4])
print(a[0:len(a)]) # 0부터 문자길이 만큼 출력
print(a[:4]) #처음부터 4번째 전까지 출력
print(a[:]) #전체 출력
print(b[0:4:2]) #0부터 4전까지 출력하는데 2만큼 건너뛰어서 출력
print(b[1:-2]) #1부터 -2앞까지 출력 -1=e
print(b[::-1]) #-1부터 끝까지 출력 : 역순으로 출력