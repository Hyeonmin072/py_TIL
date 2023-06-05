# bar=[]
# for num in range(10):
#         value=int(input("학생 성적 입력: "))
#         bar.append(value)

# sum=0
# for num in range(10):
#         sum+=bar[num]
# print(sum/10)

# bar = list()
# foo=[1,3,4,5,"fkfkfk"]
# print(type(bar),type(foo))
# print(bar,foo)

# foo.append(1) #끝부터 원소를 추가
# print(foo)

# bar.append("tk")
# print(bar)

# pos=[9,8,7,6,5]
# print(pos[0])
# print(pos[1])
# print(pos[2])
# print(pos[3])
# print(pos[4])

# stdList=[]
# count=10
# a=1

# for i in range(count):
#         print("학생",end='')
#         print(i+1,end='')
#         stdList.append(int(input("의 성적 : ")))
        
# sum=0

# for l in range(count):
#         sum+=stdList[l]
        
# print("학생",count,"명 성적의 총 합은 : ", sum)

a=[] #주민등록 번호 리스트
sum=0 #계산식 총합 계산
b=2 #체크   
result=0

print("- 을 포함한 주민등록 번호 13자리를 입력해주세요")
for i in range(13):
    a.append(input("주민등록 번호 입력 :"))
    if a[i].isdigit():
        a[i]=int(a[i])
        sum = a[i]*b
        print("TRUE")
    else:
        b-=1
        print("FALSE")
    if b!=9:
        b+=1
    elif b==9:
        b=2
        
a.append(input("주민등록 번호 입력:"))
if a[13].isdigit():
    a[13]=int(a[13])
    print("TRUE")
else:
    print("FALSE")

print("\n")
print("입력된 주민등록 번호: ",end="")
for i in range(14):
    print(a[i],end="")
print("\n")
    
result=(11-(sum%11))% 10
if result == a[13]:
    print("올바른 주민등록 번호입니다.")
else:
    print("올바르지 않은 주민등록 번호 입니다.")
    