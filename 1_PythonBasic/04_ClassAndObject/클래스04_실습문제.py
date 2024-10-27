"""
영철은 스타트게임즈 회사에 개발자로 취직을 하게 되었다. 지난주 회의 결과로
신작 MMORPG 게임의 아이템 구성안을 만들었다.

아이템 공통 : 이름, 가격, 무게, 판매하기, 버리기
장비 아이템 : 착용효과, 착용하기
소모품 아이템 : 사용효과, 사용하기
(단, 버리기는 버릴 수 있는 아이템만 가능하다.)


"""


class Item:
    def __init__(self, name, price, weight, isdropable): #생성자 생성
        self.name = name
        self.price = price
        self.weight = weight
        self.isdropable = isdropable

    #판매 함수
    def sale(self):
        while True:
            select = input(f"[{self.name}]를 판매하시겠습니까? (예, 아니오)")

            if select == "예":
                print(f"[{self.name}] 판매 가격은 [{self.price}]")
                break
            elif select == "아니오":
                print(f"[{self.name}]를 판매하지 않았습니다. 판매시스템을 종료합니다.")
                break
            else:
                print("잘못 입력하였습니다. 다시 입력하시오.")
    #버리기 함수
    def discard(self):
        if self.isdropable:
            print(f"[{self.name}을 버렸습니다.]")
        else:
            print(f"[{self.name}]을 버리는데 실패하였습니다.")




class WearableItem(Item):
    def __init__(self, name, price, weight, isdropable, effect):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect

    def wear(self):
        print(f"[{self.name}]을 착용하였습니다. {self.effect}")


class UsableItem(Item):
    def __init__(self, name, price, weight, isdropable, effect):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect
    def use(self):
        print(f"[{self.name}]을 사용하였습니다. {self.effect}")


def menu():
    while True:
        print(" ")
        print("===============메뉴 선택===============")
        print("1. 판매")
        print("2. 버리기")
        print("3. 인벤토리")
        print("4. 종료하기")
        print("======================================")
        print(" ")
        select = input("메뉴를 입력하시오. : ")


        if select == "1":
            sword.sale()
            break
        elif select == "2":
            sword.discard()
            break
        elif select == "3":
            while True:
                print("===============아이템 선택===============")
                print("사용하거나 착용할 아이템을 선택하시오. ")
                print("◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆")
                print ("1. 이가닌자의검")
                print ("2. 신비한 투명물약")
                print("◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆")
                selectInven = int(input(""))
                if selectInven == 1:
                    sword.wear()
                    break
                elif selectInven == 2:
                    potion.use()
                    break
        elif select == "4":
            print("메뉴를 종료합니다.")
            break
        else:
            print("잘못 입력하였습니다. 다시 입력하시오.")


#인스턴스 생성

sword = WearableItem("이가닌자의검", 30000, 3.5, True, "체력 5000증가 , 마력 5000증가")
potion = UsableItem("신비한 투명물약", 150000, 0.1, False, "투명효과 300초")

menu()


