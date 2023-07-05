# class는 동일한 형태(내용)을 가지는 객체를 여러개 찍어내기 위해서 필요함

#Student 라는 클래스를 정의
class Student:
    name='' #클래스 내 멤버 변수
    
    def prtName(self): #클래스 내 멤버 메서드
        print(self.name)       
    
    #생성자
    
    def __init__(self):
        print("객체 생성")



stdObj = Student() # Student로 생성된 객체의 메모리 주소값이 stdObj로 넘어가게됨
# 생성자 생성


#특정 클래스의 객체를 찍으면 반환되는 것은 생성된 객체의 메모리 주소 값이 반환됨

# 특정 클래스의 객체를 찍는 행위를 객체화한다고함

#변수가 담는 값이 메모리 주소값이냐 아니냐에 따라서 원시 변수와 참조 변수로 나뉜다, 메모리 주소를 담는 경우 참조 변수라고한다

stdObj.name = '김현민'
# stdObj가 가르키는 주소의 name값을 '김현민'으로 변경

# .연산자 있는 경우 . 왼쪽에 (좌항) 있는 연산자의 메모리 주소로 점프한다

stdObj.prtName()
#stdObj가 가르키는 주소 값의 내 선언한 함수인 prtName() 함수를 사용


# 참조변수는 특정 객체에 접근하기 위해서 필요함, 참조 변수에 특정 객체의 메모리 주소를 담기 때문
# stdObj = Studen()를 이용하여 stdObj에 메모리 주소를 담아 stdObj.name='김현민'을 사용하면 stdObj 메모리 주소로 점프하여 name으로 이동해 해당 객체의
# name 값을 '김현민'으로 변경한다.

