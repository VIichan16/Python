#람다 함수란?
# : 이름을 지을 필요도 없을 간단한 형태의 함수
# 다른 함수의 인자(argument)로 넣을 수 있다.
# 코드가 간결해 지고 , 메모리가 절약된다.

#선언 방법
# lambda 매개변수 : 리턴 값
lambda a : a-1

#호출 방법
#1번.
(lambda a : a-1)(10)

#2번(변수안에 람다함수를 넣어서 사용.)
minus_one = lambda a : a-1
minus_one(10) #(함수처럼 호출하여 사용 가능)

print(minus_one(10))


#람다 함수 사용방법(if문 사용)
#기존 함수 정의 방법
def is_positive_number(a):
    if a > 0:
        return True
    else:
        return False

#람다 함수(if문) 정의 방법
#lambda 매개변수 : 리턴값 if 조건식 else 리턴값
lambda a : True if a > 0 else False

#호출 방법1
print((lambda a : True if a > 0 else False)(-2))

#호출 방법2
is_positive_number2 = lambda a : True if a > 0 else False
print(is_positive_number2(2))

