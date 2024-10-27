"""
상속이란?
: 클래스들에 중복된 코드를 제거하고 유지보수를 편하게 하기 위해서 사용.

"""

#부모 클래스 생성
class Monster:
    def __init__(self, name,health, attack):
        self.name = name
        self.health = health
        self.attack = attack
    def move(self):
        print(f"[{self.name}] 지상에서 이동하기")

#상속 받을 자식 클래스 생성
class Wolf(Monster):
    pass

class Shark(Monster):
    def move(self): #메서드 오버라이딩
        print(f"[{self.name}] 헤엄치기")

class Dragon(Monster):
    def move(self): #메서드 오버라이딩
        print(f"[{self.name}] 날기")

wolf = Wolf("늑대" , 1500,200)
wolf.move() # wolf는 Monster의 move를 사용

shark = Shark("메갈로돈" , 2000, 300)
shark.move() # shark는 Shark클래스에서 재정의 된 move를 사용

dragon = Dragon("투슬리스" , 8000,800)
dragon.move() # dragon는 Dragon클래스에서 재정의 된 move를 사용
