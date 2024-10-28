import 모듈03_모듈생성
#원래 모듈명이나 변수명들은 영어로 작성해주는게 좋다.

#변수 사용
print(모듈03_모듈생성.version)

#함수 사용
모듈03_모듈생성.printAuthor()

#클래스 사용
pay_info = 모듈03_모듈생성.Pay("A120305", 20000, "2021-06-13")
print(pay_info.get_pay_info())


print(모듈03_모듈생성.__name__) #pay module 실행 출력

