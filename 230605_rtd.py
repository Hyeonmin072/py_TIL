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

stdList=[]
count=10
a=1

for i in range(count):
        print("학생",end='')
        print(i+1,end='')
        stdList.append(int(input("의 성적 : ")))
        
sum=0

for l in range(count):
        sum+=stdList[l]
        
print("학생",count,"명 성적의 총 합은 : ", sum)1