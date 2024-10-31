"""
pickle 모듈이란?
: 파일에 파이썬 객체를 저장 할 수 있는 모듈



pickle 모듈 객체 쓰기 방법
ex)
import pickle --> 내장 모듈
data = {
    "목표1" : "매일 팔굽혀 펴기 100회",
    "목표2" : "매일 코딩 공부 1시간"
}
file = open("data.pikle","wb") --> data.pikle 이 부분은 data.p or data.pic 이 처럼 원하는대로 변경 가능 , 파일 모드 "wb"는 write binary 라는 뜻
pickle.dump(data,file) --> file 변수에 data 라는 객체가 저장된다.
file.close()


pickle 모듈 객체 읽기 방법
ex)
import pickle --> 내장 모듈
file = open("data.pikle","rb") --> 파일 모드 "rb"는 read binary 라는 뜻
data = pickle.load(file)
print(data)
file.close()


with문 이란?
파이썬에서 open 함수를 사용해서 파일을 열면 파이썬이 알아서 닫아 주는 문법

with 구문 사용 x
file = open("data.txt" , "r")
data = file.read()
file.close()

with 구문 사용 o
with open("data.txt" , "r") as file:
    data = file.read()

"""