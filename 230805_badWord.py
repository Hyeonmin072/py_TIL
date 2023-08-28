# 비속어 필터링 프로그램

# 입력 받은 단어를 모두 끊어서 저장하기
# 끊어서 저장한 단어들을 모두 검사
# 비속어 필터에 포함된 단어들은 모두 지정된 *로 블라인드 처리

while True:
    
    InputAs = str(input("입력 : "))
    
    word = InputAs.split(' ')
    
    BadWord = list()
    
    for i in range(len(word)):
        if word[i] == "ㅅㅂ":
            word[i] = "**"
        elif word[i] == 'ㅄ':
            word[i] = '*'
        elif word[i] =='ㅂㅅ':
            word[i]='**'
            
    print("출력 :",*word)
    
    if InputAs == "종료":
        print('프로그램 종료')
        break
    