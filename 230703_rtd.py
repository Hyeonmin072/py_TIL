# 5명 학생 성적을 입력받아 아래와 같이 출력하는 프로그램 작성

# 1번쨰 학생이름:ㅇㅇㅇ
# 1번째학생 국어 성적 :100
# 1번째 학생 영어 성적 : 100
# 1번째 학생 수학 성적 : 100

# 2번쨰 학생이름:ㅇㅇㅇ
# 2번째학생 국어 성적 :100
# 2번째 학생 영어 성적 : 100
# 2번째 학생 수학 성적 : 100

# 3번쨰 학생이름:ㅇㅇㅇ
# 3번째학생 국어 성적 :100
# 3번째 학생 영어 성적 : 100
# 3번째 학생 수학 성적 : 100

# 4번쨰 학생이름:ㅇㅇㅇ
# 4번째학생 국어 성적 :100
# 4번째 학생 영어 성적 : 100
# 4번째 학생 수학 성적 : 100

# 5번쨰 학생이름:ㅇㅇㅇ
# 5번째학생 국어 성적 :100
# 5번째 학생 영어 성적 : 100
# 5번째 학생 수학 성적 : 100
# 출력 결과

# 1. 홍길동 국어 100 영어 100 수학 100 합계 300 평균 : 
# 5번까지

# count=1
# while True:
    
#     if count ==6:
#         break
    
#     print(count,end=''),
#     a=(input('번째 학생 이름 : '))
#     print(count,end=''), 
#     b=int(input('번째 학생 국어 성적 : '))
#     print(count,end='')
#     c=int(input('번째 학생 영어 성적 : '))
#     print(count,end='')
#     d=int(input('번째 학생 수학 성적 : '))
    
#     sum =b+c+d
#     aver=sum/3
#     print(count,end='')
#     print ('.',a,'국어:',b,'영어:',c,'수학: ',d,'총점',sum,'평균',aver)
#     count+=1

class Student :
    name = ''
    lag = 0
    eng = 0
    mat = 0
    sum = lag+eng+mat
    avg = sum / 3
    
    
    def getSum(self):
        self.sum = self.lag + self.eng + self.mat
        return self.sum
    
    def getAvg(self):
        self.avg = self.getSum()/3
        return self.avg
    
    def printStdInfo(self):
        print(self.name,'\t', self.lan,'t', self.eng,'\t', self.mat,'\t', self.getSum(),'\t', self.getAvg())
    # 클래스 안에 존재하는 함수를 메소드(method)라고 한다.
    
    
std1 = Student()
std1.name = '홍길동'
std1.lag = 100
std1.eng = 100
std1.mat = 100
std1.avg

print (std1.avg)




# std1 = Student()로 불러옴에 따라 std1을 객체로 선언하며 Student 클래스의 메모리 주소를 std1로 가져옴
# 여기서 std1은 참조 변수로 메모리값을 저장하는 변수를 가르킨다.
 