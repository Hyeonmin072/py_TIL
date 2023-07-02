import random
import math
# def Ainput ():
#     count =1
#     y= list()
#     while True:
#         a = input('단어를 입력하세요 : ')
#         b = len(a)
#         if b <= 3 or b >= 20:
#             print ('3보다 크고 20보다 작은 문자열을 입력하세요.')
#             continue
#         elif count == 3:
#             print ('단어 3개 입력 완료')
#             return y[0:3]
#         else:
#             y.append(a)
#             count +=1
#             print('단어 입력 완료')
    
# index = list()
# Ainput(index)
# a=random.randint(0,3)
# print(a)
# print('선택된 단어: ',index(a))

test = []
#입력받은 단어를 리스트에 집어넣는 함수
def ainput(a):
    test.append(a)

count = 0
while True:
    a=input('단어를 입력하세요 : ')
    
    if count ==2:
        ainput(a)
        print('단어 3개 입력 완료')
        break
    
    
    elif len(a) <=3 or len(a) >=20:
        print('단어가 너무 짧거나 깁니다.')
        continue
    
    else:
        print('단어 입력완료')
        count+=1
        ainput(a)
        
print ('랜덤 단어 선택')
a = random.randint(0,2)

print('선택된 단어 : ',test[a])

print('입력된 단어 개수와 그 절반을 상수로 리턴')
print (len(test[a]))
hanbun = len(test[a])/2
print (hanbun)

print('반올림 처리')
print(round(hanbun))
ban=round(hanbun)

print('선택된 문장내 단어를 나누기')
c=test[a]
c.split()
print(list(c))

print('무작위 순번을 선택')
list = []
rannum = random.randint(0,len(test[a])-1)

for i in range(ban):
    while rannum in list:
        rannum = random.randint(0,len(test[a]))
    list.append(rannum)
list.sort()
print(list)

print('선택된 숫자의 위치에 존재하는 문자를 _로 처리')

box=[]
print('선택된 순번의 문자 : ', end='')
for i in range(0, ban):
    print(c[list[i]],end='')

for i in range(ban):
    c[list[i]]='_'
print(c)
#     box[i]=c[list[i]]
#     c.insert(list[i],'_')
# print(c)
    
        
