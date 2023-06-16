# foo ='abcd'

# for bar in foo:
#     print(bar)

# while True:
#     a =str(input('문자를 입력하세요 : '))
#     if a == 'quit':
#         print('프로그램 종료')
#         break
    
#     b =str(input('찾고자 하는 알파벳을 입력하세요 : '))
    
#     if a.count(b)>0: 
#         print(b,'가 문자열 내 존재합니다.','개수: ',a.count(b), '총 문자열 길이: ', len(a))
#     else:
#         print(b,'가 문자열 내 존재하지 않습니다.')
        

# while True:
#     count = 0
#     count1 =0
#     a =str(input('문자를 입력하세요 : '))
#     if a == 'quit':
#         print('프로그램 종료')
#         break
    
#     b =str(input('찾고자 하는 알파벳을 입력하세요 : '))
    
#     for var in a:
#         count1 += 1
    
#     for bar in a:
#         if bar == b:
#             count+=1
            
#     if count>0:
#         print(b,'가 문자열 내 존재합니다.', '개수: ', count, '총 문자열 길이: ', count1)

#     else:
#         print(b,'가 문자열 내 존재하지 않습니다. ')



import random
win=0
lose=0
draw=0
count=0

while True:
    count+=1
    compick=''
        
    com=random.randint(1,3) #1가위 #2바위 #3보
    if com==1:
        compick ='가위'
    elif com ==2:
        compick ='바위'
    elif com ==3:
        compick ='보'
        
    a=str(input('◆ 가위, 바위, 보, quit 중 하나를 입력하세요 ◆ : '))
        
    if a=='quit':
        print('승리:',win)
        print('패배:',lose)
        print('무승부:',draw)
        print('승률:',win/count*100)
        break
    
    elif a!='가위' and a!='바위' and a!='보':
        print('올바르지 않은 값입니다.')
        print()
        continue
        
    if compick==a:
        print('무승부.', '사용자:', a,'■', '컴퓨터:', compick)
        print()
        draw +=1
        
    elif a=='가위' and compick =='바위'or a=='바위'and compick =='보'or a=='보'and compick =='가위':
        print('패배.', '사용자:', a,'vs', '컴퓨터:', compick)
        print()
        lose +=1
        
    else:
        print('승리.', '사용자:', a,'■', '컴퓨터:', compick)
        print()
        win+=1
        
    
    
