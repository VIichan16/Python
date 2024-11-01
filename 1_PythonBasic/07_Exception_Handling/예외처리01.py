#실습1
from typing import final

# 원화를 입력, 환율 입력 -> 달러 값

won = input("원화금액을 입력 하세요. >>> ")
dollar = input("환율을 입력하세요. >>>")

"""
try: # 예외가 발생 할 수 있는 코드
    print(int(won) / int(dollar))
except: # 예외가 발생했을 때 실행되는 코드
    print("예외가 발생했습니다.")
"""

# try - except 문으로 감싸 주게 되면 예외가 발생 하더라도 프로그램이 종료가 되지 않음

try: # 예외가 발생 할 수 있는 코드
    print(int(won) / int(dollar))
except ValueError as e: # won , dollar 의 값은 int인 정수값 이지만 입력 값이 다른 자료형이 들어 왔을 때 발생하는 에러
    #as e 는 에러의 별칭을 정해줄 수 있음.
    print("에러가 발생했습니다.", e) # 프린트 문 마지막에 에러 메세지가 출력 된다.
except ZeroDivisionError as e: # 어떠한 수를 0으로 나눌 때 발생하는 오류입니다.
    print("나누기 0 은 불가 합니다." , e)
else:
    print("예외가 발생하지 않았을 때 실행되는 코드")
finally: # 리소스 반환을 꼭 해줘야 하는 부분에 많이 사용됨
    print("예외가 발생하던지, 하지 않던지 무조건 실행 되는 코드")