# class Student:
#     name=''
#     def prtName(self):
#         print(self.name)
    
# obj=Student()
# # Student 클래스의 객체를 하나 생성
# obj.name='리차드'
# obj.prtName()


# class Bar:
#     name='리차드'
    
#     def prtName1(kkk):
#         name='khm'
#         print(name)
 
#     def prtName2(kkk):
#         kkk.name='foo'
#         print(kkk.name)

# obj=Bar()

# obj.prtName1() 
# #obj가 가르키는 메모리 주소의 알고리즘을 실행 
# #함수 내 name을 선언하여 khm으로 변경하여 프린트했기 때문에 khm 출력
# print(obj.name)
# #obj가 가르키는 객체의 name을 출력하게함, 따라서 리차드 출력

# obj.prtName2()
# #obj가 가르키는 객체 내의 함수인 name2 함수를 실행
# #매개변수인 kkk 내 name을 foo인 문자열로 선언
# #프린트 kkk.name으로 foo 출력
# print(obj.name)
# #이미 위에서 kkk.name으로 foo 문자열을 선언 해 놓았기 때문에
# #그대로 문자열 foo출력

#따라서 총 출력값은
#khm
#리차드
#foo
#foo

# ★ 클래스 내에서 메소드를 선언할 때 무조건 1개 이상의 매개변수가 선언 되어야 한다
# ★ 선언한 메소드에서 선언한 첫번째 매개변수에는 현재 메소드를 호출한 객체의 주소가 넘어온다

# 만약 클래스 내 함수의 두번째 매개 변수는 사용할 때 괄호 안에 첫번째 인자와 같은가 ? YES

# class Bar:
#     name = "pos"
    
#     def test(self):
#         name="king"
#         print(self.name)
        
# obj = Bar()
# obj.test()

class Bar:
    name = '리차드'
    
    def __init__(self,arg): #생성자
        print(arg)
    
    def prtSomething(self):
        print('곤니찌와')
    
    
    def prtName(self, arg1, arg2):
        print(self.name, arg1, arg2)
        self.prtSomething()
        
obj=Bar('리차드')

obj.prtName("HELLO",'안녕하세요')
# ★ 객체 내 함수를 호출할 때 외적으로는 인자값이 없는 것으로 보이지만
# ★ 실제로는 함수를 사용하는 참조 변수의 메모리 주소값을 가지고 있다.

# 생성자는 알고리즘으로 함수와 동일하다
# 함수와 동일하다면 생성자는 메소드와 같다고 할 수 있으나 용도는 다르다
# 생성자는 딱 한번만 실행되며 객체가 만들어질 때 만들어진다.
# obj = Bar()에서 ()가 생성자가 만들어지는 부분은 ()다

# 생성자는 무조건 메모리 주소 값을 반환해야하기 때문에 리턴 값을 정할 수 없다


