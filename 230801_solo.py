import random

class _Player :
    name = ""
    hp = 100
    attack = 15
    defence = 10
    
class _info : # 기본 몬스터 부모 클래스 # 스폰 함수
    def SpawnMsg(self): # 소환 안내 메세지
        print(self.name,"이(가) 소환되었습니다.")
        print(self.name,"의 체력은",self.hp,"이며,","공격력은",self.attack,"방어력은",self.defence, "입니다.")
    
class _Slime(_info): # 슬라임 클래스 생성
    def __init__(self,argHp,argAttack,argDefence):        
        self.name="슬라임"
        self.hp = argHp
        self.attack = argAttack
        self.defence = argDefence
        
class _Orc(_info): # 오크 클래스 생성
    def __init__(self,argHp,argAttack,argDefence):        
        self.name="오크"
        self.hp = argHp
        self.attack = argAttack
        self.defence = argDefence
        3
class _Dragon(_info): # 드래곤 클래스 생성
    def __init__(self,argHp,argAttack,argDefence):        
        self.name="드래곤"
        self.hp = argHp
        self.attack = argAttack
        self.defence = argDefence           

Slime = _Slime(50,10,1)
Orc = _Orc(100,20,10)
Dragon = _Dragon(200,30,15)



Player =_Player()

class spawn(_info,_Player): # 몬스터 소환 클래스
    
    PlayerHp = _Player.hp
    
    def __init__(self,argCount=1):
        count = argCount
        
        for i in range(1, count+1):
                spawndice = random.randrange(1,4)
                
                if spawndice == 1:
                    Slime.SpawnMsg()
                    MonsterHp = Slime.hp
                    while True:
                        PlayerHp = PlayerHp - (Slime.attack-Player.defence)
                        print ("슬라임의 공격, 플레이어 HP : ",PlayerHp)
    
                        MonsterHp = MonsterHp - (Player.attack-Slime.defence)
                        print("플레이어의 공격, 슬라임 HP : ",MonsterHp)
    
                        if PlayerHp < 0 or MonsterHp < 0:
                            print("전투 종료 ","플레이어 HP :",PlayerHp,"슬라임 HP :",MonsterHp)
                            break
                        
                if spawndice == 2:
                    Orc.SpawnMsg()
                    MonsterHp = Orc.hp
                    while True:
                        PlayerHp = PlayerHp - (Orc.attack-Player.defence)
                        print ("오크의 공격, 플레이어 HP : ",PlayerHp)
    
                        MonsterHp = MonsterHp - (Player.attack-Orc.defence)
                        print("플레이어의 공격, 오크 HP : ",MonsterHp)
    
                        if PlayerHp < 0 or MonsterHp < 0:
                            print("전투 종료 ","플레이어 HP :",PlayerHp,"오크 HP :",MonsterHp)
                            break
                        
                if spawndice == 3:
                    Dragon.SpawnMsg()   
                    MonsterHp = Dragon.hp
                    while True:
                        PlayerHp = PlayerHp - (Dragon.attack-Player.defence)
                        print ("드래곤의 공격, 플레이어 HP : ",PlayerHp)
    
                        MonsterHp = MonsterHp - (Player.attack-Dragon.defence)
                        print("플레이어의 공격, 드래곤 HP : ",MonsterHp)
    
                        if PlayerHp < 0 or MonsterHp < 0:
                            print("전투 종료 ","플레이어 HP :",PlayerHp,"드래곤 HP :",MonsterHp)
                            break
                        
                elif spawndice > 3:
                    print('ERROR')
                    break
                           
Fight = spawn(3) # 몬스터 전투 (횟수)


# 왜 안되는건지 나도 모름