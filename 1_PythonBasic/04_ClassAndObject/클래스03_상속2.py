#클래스03_상속 프로그램 업그레이드 버전
import random


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
    #생성자 오버라이딩
    def __init__(self, name,health, attack): #(3번)스킬을 멤버변수에 직접적으로 입력해주면 매개변수가 없어도 되기 때문에 skill매개변수를 없애준다.
        super().__init__(name,health,attack) #--> 부모 클래스의 __init__() 메소드를 자식 클래스의 __init__() 메소드에서 실행 한다고 생각 하면 된다 즉, 자식 클래스에도 부모 클래스의 인스턴스 속성과 동일한 속성이 생성되는 것.
        self.skills =("불뿜기" , "꼬리치기", "날개치기") # --> (2번) 멤버 변수에다가 바로 스킬 목록을 작성 한다.

    def move(self): #메서드 오버라이딩
        print(f"[{self.name}] 날기")
    def skill(self):
        print(f"[{self.name}]의 {self.skills[random.randint(0,2)]} 발동") #--> 스킬 목록이 튜플로 되어있기 때문에 랜덤 함수를 사용해 3개중 하나를 랜덤으로 반환



wolf = Wolf("늑대" , 1500,200)
wolf.move() # wolf는 Monster의 move를 사용

shark = Shark("메갈로돈" , 2000, 300)
shark.move() # shark는 Shark클래스에서 재정의 된 move를 사용

#dragon = Dragon("투슬리스" , 8000,800, ("불뿜기" , "꼬리치기", "날개치기")) --> (1번) 이런식으로 코드를 작성하면 동작이 되겠지만, 현재는 드래곤이 하나라 문제가 없지만 드래곤이 여러개가 나올때마다 입력을 해줘야 하기때문에 멤버 변수에다 입력해주어 코드를 간결하게 작성한다.
dragon = Dragon("투슬리스" , 8000,800)
dragon.move() # dragon는 Dragon클래스에서 재정의 된 move를 사용
dragon.skill()