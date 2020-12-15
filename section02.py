#Section02-1
#파이썬 기초 코딩
#Print 구문의 이해

#기본출력
print('Hello world')
print("Hello World")
print("""Hello Python""")
print('''Hello Python''')

print()#줄 바꾸기

# Separator 옵션 사용
print('T','E','S','T')
print('T','E','S','T',sep='')
print()
print('2020','12','12',sep='-')
print('rlaeodud9983','naver.com',sep='@')
print()

#End 옵션 사용
print('Welcome To', end=' ')
print('the black parade',end=' ')
print('piano notes')
print()

#Format 사용
print('{} and {}'.format('You', 'Me'))
print("{0} and {1} and {0}".format('You','Me'))
print("{a} are {b}".format(a='You', b='Me'))

 # %s : 문자, %d : 정수, %f : 실수
print("%s's favorite number is %d" % ('Eunki', 7))

# %5d 5칸 띄어쓰기 후 정수 출력
# %4.2f 4칸 띄어쓰기 후 소수점 2번째자리까지 출력
print("Test1: %5d, Price:  %4.2f" % (776,6534.123)) 
#format 사용할때는 % 안붙여도 됨
print("Test1: {0: 5d}, Price: {1: 4.2f}".format(776,6534.123))
print("Test1: {a: 5d}, Price: {b: 4.2f}".format(a = 776, b= 6534.123))
print()

#Escape
# \ = Enter위의 원 표시 
"""
\n : 줄 바꾸기
\t : tap만큼 띄기
\\ : 문자
\' : 문자
\" : 문자
\r : 캐리지 리턴
\f : 폼 피드
\a : 벨 소리
\b : 백 스페이스
\000 : NULL 문자

"""

print("'You'")
print('\'you\'')
print("""'you'""")
print('\\you\\')
print('you\n\n\n')
print('\t\t\t test')