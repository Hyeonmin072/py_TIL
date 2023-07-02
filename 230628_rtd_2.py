count=0
a=1
while True:
    count+=1
    print("실행 횟수: ", count)
    x=int(input('X값을 입력하세요: '))
    if x<0:
        print('입력 값은 양의 정수만 입력이 가능합니다.')
        continue
    y=int(input('Y값을 입력하세요: '))
    
    if x < y :
        print(x,'에서',y,'사이 정수 중 짝수 값 : ',end='')
        for i in range(x,y+1):
            if i%2==0:
                print(i,',',end='')
        print()
    elif x > y :
        print('Y','[',y,']','값은 ','X', '[',x,']','값 보다 커야합니다.')
    elif x==y:
        print('프로그램 종료')
        break
    
    
        