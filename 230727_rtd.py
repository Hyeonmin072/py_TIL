# 상속은 멤버 변수와 멤버 메소드를 부모 클부래스에서 자식 클래스로 물려주는 것
# 상속은 단일 상속과 다중 상속이 있는데 파이썬은 다중 상속을 지원한다

# 다중 상속은 상속 받을 부모 클래스가 2개 이상 존재할 수 있다
# 다중 상속의 단점은 상속 시키는 2번째 부모 클래스와 변수와 메소드가 충돌할 수 있다는 단점이 있다.

# 농구 
# player
# Center

class Player :
    name="Player"
    number= -10
    position=""
    energy = 10

    
    def shoot(self):
        print (self.name, self.number, 'Player 슛')
        
    def steal(self):
        print (self.name, self.number, 'Player 스틸')
    
class Center(Player) :
    def __init__(self, argName, argNumber)  :
        self.position = "Center"
        self.name = argName
        self.number = argNumber        
class Pf(Player) :
    def __init__(self, argName, argNumber)  :
        self.position = "Pf"
        self.name = argName
        self.number = argNumber

player_1 = Center('Hyeonmin', 23)
player_2 = Pf('Minwoo', 55)

player_1.shoot()
player_2.shoot()



class Sf(Player) : 
    pass

class Pg(Player) :
    pass

class Sg(Player) :
    pass


    