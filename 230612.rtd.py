# bar = [6,7,8]

# for value in bar:
#     print(value)
    
# foo = list()

# for value in range(6, 9):
#     foo.append(value)
    
    
# print(foo)

# foo=[6,7,8]
# bar =(6,7,8)

# foo[0]=100
# print(foo)

# bar = list()

# for value in range(1, 101):
#     bar.append(value)
    
# foo = tuple(bar)

# print(type(foo))

# inputSsid=input("주민번호를 입력하세요. ")
# ssidList=list()
# for value in inputSsid:
#     if value.isdigit():
#         ssidList.append(int(value))
        
        
# checkDigitList=(2,3,4,5,6,7,8,9,2,3,4,5)
# sum=0
# for index in range(len(checkDigitList)):
#     sum+=ssidList[index]*checkDigitList[index]
    
    
# checkValue = (11-sum%11)%10

# if checkValue == ssidList[-1]:
#     print("유효")
# else:
#     print("무효")
import random
count=3
comChoose=list()
for i in range(0, 3):
    comChoose=random.randint(0,9)
    comChoose=int(comChoose)
    print(comChoose)
    
    for j in range(0,3):
        if comChoose[i]==comChoose[j]:
            comChoose[i]=random.randint(0,9)
    