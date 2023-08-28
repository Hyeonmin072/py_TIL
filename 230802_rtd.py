# 멤버 변수는 인스턴트 변수와 클래스 변수로 나눠진다
# 멤버 메소드의 경우 인스턴스 메소드와 클래스 메소드 그리고 스태틱 메소드 라는 것이 존재한다


# class Bar:
#     name = "temp" # 클래스 변수
    
    
# obj1=Bar()
# obj2=Bar()

# obj1.name="hm" # 인스턴스 변수
# obj2.name="kimu" #인스턴스 변수


# print(obj1.name)
# print(obj2.name)
# print(Bar.name)


# class Foo:
#     id = 0 #클래스 변수

#     def __init__(self, argName):
#         self.myName = argName #myName -> 인스턴스 변수
#         self.myId = Foo.id +1 #myId -> 인스턴스 변수
#         Foo.id = Foo.id +1 # id -> 클래스 변수
        
#     def prtId(self):
#         print(Foo.id)
    
# obj1 = Foo("hi")
# obj2 = Foo("hello")

# Foo.id =100

# obj1.prtId()
# obj2.prtId()

# 클래스 변수는 클래스가 선언될 때 만들어짐
# 인스턴스 변수는 객체가 만들어질 때 만들어짐
# 클래스 변수는 각 객체가 공유해서 사용할 수 있음
# 특정 클래스의 값이 모든 객체가 공유할 필요가 있을 때 사용하는 것이 클래스 변수

# class Foo:
#     id = 0 # 클래스 변수
    
#     def __init__(self): #인스턴스 변수는 생성자로 접근해야함
#         self.myName ="Hm" # 인스턴스 변수
        
# obj1 = Foo()
# obj2 = Foo()

# obj1.id=2
# obj2.id=3

# print(obj1.id,obj2.id,Foo.id)

# 인스턴스 변수는 각 객체에서 동적으로 그때그때 할당 시킴
# 클래스 변수는 독립적으로 클래스 안에서 따로 존재함 클래스 변수는 전 객체가 공유하며 클래스 변수의 변경이 필요할 경우 클래스이름.변수명 으로 접근이 필요함
# obj1.id 의 경우 객체로 접근하는 코드이나 객체 내 id라는 변수가 존재하지 않으니 동적으로 id라는 변수를 만들어냄

class Student:
    
    classId=2
    
    def __init__(self):
        self.name=""
        self.id =0
        
        
    def prtName(self): #인스턴스 메소드
        print(self.name)
        # 인스턴스 변수를 이용하여 알고리즘을 작성하여 사용 
        
        
    @classmethod
    def prtClassId(cls): # 클래스 메소드
        print(cls.classId)
        # 클래스 메소드는 클래스 내 클래스 변수에 접근이 가능하다
        
        
    @staticmethod
    def prtHello(): # 스태틱 메소드
        print("hello")
        
        
obj1=Student()

obj1.prtClassId()
Student.prtClassId()

obj1.prtHello()
Student.prtHello()

obj1.prtName()
Student.prtName()