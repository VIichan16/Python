"""
로또에 당첨 되서 퇴사를 하고 싶었던 김로또는 로또 예상번호 추출 프로그램을
파이썬으로 작성하려고 한다. 다음 조건에 따라 김로또의 프로그램을 완성해보자
1. 로또 번호 6개를 생성한다.
2. 로또 번호는 1~45까지의 랜덤한 번호다.
3. 6개의 숫자 모두 달라야 한다.
4.getRandomNumber() 함수를 사용해서 구현한다. (random 모듈의 sample함수는 사용하지 않는다)

"""
import random
def getRandomNumber(): # 1~45 중 랜덤 숫자를 반환해주는 함수
    number = random.randint(1, 45)
    return number


lotto_num = [] #로또 번호를 저장할 리스트
count = 0

while True:
    if count > 5: #로또 번호가 6개가 다 뽑히면 반복문 종료
        break

    random_number = getRandomNumber()
    if random_number not in lotto_num: #lotto_num 리스트안에 해당 값이 들어있지 않으면 true 들어있으면 fales
        lotto_num.append(random_number)
        count += 1


        


lotto_num.sort()

for num in lotto_num:
    print(num , end=" ") # end=" " 함수가 종료 된 이후 출력할 문자.

