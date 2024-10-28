#결제 정보, 관리 모듈
#변수
version = 2.0


#함수
def printAuthor():
    print("스타트코딩")



#클래스
class Pay:
    def __init__(self, id, price, time): # id: 식별아이디 , price : 결제가격 , time : 결제 시간
        self.id = id
        self.price = price
        self.time = time
    def get_pay_info(self):
        return f"{self.id} {self.price} {self.time}"

#해당 파일을 직접 실행했을 때만 실행된다.
if __name__ == "__main__":
    print("pay module 실행")

print(__name__) #__main__ 출력