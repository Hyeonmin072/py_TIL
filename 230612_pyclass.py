# row = 3


# for i in range (1, row+1):
#     for j in range(0, row-1):
#         print(" ")
#     for k in range (1, row+1):
#         print("*",end='')
#         print()



# 3번 반복
# for i in range (1, a+1):
# # * 3회 출력 및 1회씩 줄이는 반복문
#     for j in range(a):
#         print("*", end='')
#     print()
#     a-=1
    
    
# # a번 반복
# for i in range(1, a+1):
# # 공백을 a-1개 출력 1개씩 감소
#     for j in range(a-i):
#         print(" ",end="")
# # 별을 1개 출력 1개씩 증가
#     for k in range(i):
#         print("*", end='')
#     print()


# a줄 출력

# for i in range(a):
# # 공백 a-1개 만큼 출력 -1
#     for j in range(a-i):
#         print(" ",end="")
# # 별 i번 출력 i+2
#     for k in range(i+1):
#         print("*",end="")
#     for l in range(i):
#         print("*",end="")
#     print()

#키보드로부터 양수를 입력받아
#홀 또는 짝수 판별 후 아래와 같이 출력
#홀수면 홀수 짝수면 짝수라고 출력
#만약 입력값이 0이하라면 에러메세지 출력 후 재입력(양의 정수가 입력될 때 까지)


    
# a = int(input("숫자 입력 : "))
# while (a<=0):
#     print("양의 정수를 입력하세요")
#     a = int(input("숫자 입력 : "))

# if a%2==0:
#     print("짝수입니다.")
        
# elif a%2==1:
#     print("홀수입니다.")
    
# else:
#     print("양의 정수를 입력하세요.")


# a = int(input("입력 : "))
# b=0
# while a<=0:
#     print("양수 입력 필요")
#     a = int(input("입력 : "))
    
# if a%2==0:
#     print("짝수")
# else:
#     print("양수 입력")




a = int(input("입력 : "))
stack=0
    
while a<=0 and stack<1:
    print("양수를 입력하세요")
    a = int(input("입력 : "))
    if stack==2:
        print("2회 오입력으로 프로그램 종료.")
        break
    stack+=1
    
if a % 2 ==0 and a>0:
    print("짝")
elif a%2 == 1 and a>0:
    print("홀")