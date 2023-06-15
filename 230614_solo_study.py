# a = int(input("줄 입력: "))
# a*=2
# for i in range (a):
#     for l in range (0, i):
#         print(" ",end="")
#     for j in range (0, a-1):
#         print("*",end="")
#     print()
#     a-=2


a = int(input("줄 입력: "))
b=a
c=a
a*=2
for i in range (c):
    for l in range (0, i):
        print(" ",end="")
    for j in range (0, a-1):
       print("*",end="")
    a-=2
    print()
    
for i in range (c):
    for j in range (0, b-1):
        print(" ",end="")
    for k in range (1, a+1):
        print("*",end="")
    b-=2
    a+=2
    print()
    


