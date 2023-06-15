# for bar in range(1, 11):
#     print(bar, end="")
    
#     if bar == 5:
#         break
    
    
# for dan in range(2,10):
#     if dan == 4:
#         break
    
    
#     for num in range(1,10):
#         print(dan, "X", num, "=", dan*num)
        
#         if num == 5:
#             break

# Q. 파이썬 인터프리터가 break 문장을 만나면 어떻게 동작하는가 ?
#   break 문을 만나면 인터프리터는 소스코드의 실행 흐름을 break문을 기점으로 첫번째 만나는 반복문까지 올라간다
#   반복문을 만나면 현재 실행 중인 반복문을 즉시 탈출 한다

# Q.break 문은 어디에서 사용되는가 ?
    #반복문
# Q.break 문을 언제 사용하는가 ?
    #반복문에서 특정 조건을 달성하여 더 이상 반복이 필요하지 않아 탈출(반복 정지)이 필요한 경우
    
    
# while True:
#     a=int(input("양의 정수를 입력하시오 : "))
        
#     if(a<=0):
#         print("양의 정수만 입력이 가능합니다.",end="")
#     elif(a%3==0):
#         print("3의 배수입니다.")
        
#     elif(a==100):
#         print("프로그램을 종료합니다.") 
#         break
    
        
#     else:
#         print("3의 배수가 아닙니다.")
        
        
        
# for bar in range(1, 11):
#     if bar % 2 == 0:
#         continue
    
#     print(bar, end="")

# continue는 조건을 달성할 경우 break문처럼 반복문을 탈출하지 않고 첫번째 반복문을 만날때 까지 올라간 후 반복문을 계속해서 진행함


# for i in range(2, 10):
#     if i % 2 == 1:
#         continue
#     for dan in range(1, 10):
#         if dan % 2 == 1:
#             continue
#         print(i,'*', dan,'=',i*dan)
#     print('------------')
a=5
for i in range (a):
    for k in range (a-i,5):
        print('o',end='')
    for j in range (a-1, 5):
        print('x',end='')
    print()
  