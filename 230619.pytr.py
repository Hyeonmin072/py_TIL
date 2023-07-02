
# # # a = int(input('수 입력:'))

# # # for z in range(a):
# # #     for x in range(a):
# # #         if z == 0 or z == a-1:
# # #             continue
# # #         elif z==x or z+x == a-1:
# # #             print('*',end='')
# # #         else:
# # #             print(' ',end='')
# # #     if z==0 or z==a-1:
# # #         print('*'*a)
# # #     else:
# # #         print()
# # # count=0
# # # count1=0

# # # while True:
    
# # #     a=input()
# # #     b=input()
# # #     for bar in a:
# # #         count+=1
        
# # #     for var in a:
# # #         if var ==b:
# # #             count1+=1
            
# # #     if count1>0:
# # #         print('같은 알파벳이 존재함')
# # #     print(count)
    
    
# # a = int(input(':'))

# # for z in range(a):
# #     for x in range(a):
# #         if z==0 or z==a-1:
# #             continue
        
# #         elif z==x or z+x==a-1:
# #             print('*',end='')
# #         else:
# #             print(' ',end='')
            
# #     if z==0 or z==a-1:
# #         print('*'*a)
        
# #     else:
# #         print()


# # a = int(input(":"))

# # for z in range(a):
    
# #     if z==0 or z==a-1:
# #         print('*'*a)
# #         continue
    
# #     for x in range(a):
# #         if z==x or z+x==a-1:
# #             print('*',end='')
# #         else:
# #             print(' ',end='')
            
# #     else:
# #         print()

# import random
# compick=""
# win=0
# lose=0
# draw=0
# while True:
    
#     mypick=input('가위, 바위, 보 !')
    
#     if mypick=='정지':
#         print(win,'승')
#         print(lose,'패')
#         print(draw,'무승부')
    
#     com=random.randint(1,3)
#     if com==1:
#         compick="가위"
#     elif com==2:
#         compick="바위"
#     elif com ==3:
#         compick="보"
#         #승리
#     if (mypick=="가위"and compick=="보") or (mypick=="바위"and compick=="가위") or (mypick=="보"and compick=="가위"):
#         print('승리 !', '컴퓨터의 선택 ', compick)
#         win+=1
#     elif mypick==compick:
#         print('무승부 !', '컴퓨터의 선택 ', compick)
#         draw+=1
#     else:
#         print('패배 !', '컴퓨터의 선택 ', compick)
#         lose+=1
    
        
    
a = int(input(':'))

for z in range(a):
    if z==0 or z==a-1:
        print('*'*a)
        continue
    for x in range(a):
        if z==x or z+x==a-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()
        