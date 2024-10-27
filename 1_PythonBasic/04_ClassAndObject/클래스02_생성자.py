"""
생성자란?
: 생성자(constructor)는 객체가 생성될 때 항상 가장 먼저 호출되는 함수로,
객체 속성에 값을 할당하거나 객체 생성 시 수행해야 하는 작업을 수행한다.
클래스 정의에서 가장 중요한 함수로 Python에서는 __init__ 함수에 해당한다.

객체 속성이 필요하지 않다면 __init__ 함수에 self 외의 매개변수는 정의하지 않아도 된다.
"""


#클래스 생성
class Monster:
    def __init__(self, health, attack, speed): # __init__ 함수는 인스턴스가 생성 될 때 실행
        self.health = health
        self.attack = attack
        self.speed = speed
    def decrease_health(self , num):
        self.health -= num
    def get_health(self):
        return self.health



# 고블린 인스턴스 생성
goblin = Monster(800,120,300) # __init__ 함수 실행

# 호출
goblin.decrease_health(100)
print(goblin.get_health())

# 늑대 인스턴스 생성
wolf = Monster(1500,200,350)

#호출
wolf.decrease_health(1000)
print(wolf.get_health())
