
def menu():
# 메뉴 출력
    print("----- Menu ----\n1. 구구단 출력\n2. 1에서 20까지 양의 정수 중 3의 배수와 7의 배수 이외 값 출력\n3. 프로그램 종료\n---------------")
def gugudan(a):
        for dan in range(a):
            for num in range(1, 10):
                print(a, " X ", num, "=", a*num)
def multiple():
        for value in range(1, 21):
            if value % 3 != 0 and value % 7 != 0:
                print(value)
def whdfy():
    print("프로그램 종료")
    
    

while True:
    print(menu())
    
    inputValue = int(input("메뉴 값을 입력 하세요."))
    if inputValue == 1:
        inputDan = int(input('단을 입력하세요'))
        gugudan(inputDan)
        
    elif inputValue == 2:
        multiple()
    elif inputValue == 3:
        whdfy()
        break
    else:
        print("메뉴값은 1~3까지 양의 정수값만 입력하세요")
        continue