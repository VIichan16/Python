"""
예외 만들기
class 예외(Exception):
    def __init__(self): --> 객체가 생성 되었을때 바로 실행되는 코드
        super().__init__("에러 메세지")

"""

class PositiveNumberError(Exception):
    def __init__(self):
        super().__init__("양수는 입력 불가.")


try:
    num = int(input("음수를 입력해 주세요.>>>"))
    if num >= 0:
        raise PositiveNumberError
except PositiveNumberError as e:
    print("에러 발생!" , e)