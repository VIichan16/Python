# 1. 파이썬 객체를 pickle로 저장하기
import pickle

data = {
    "목표1" : "매일 팔굽혀 펴기 100회",
    "목표2" : "매일 코딩 공부 1시간"
}

file = open("data.pickle", "wb")
pickle.dump(data, file) # --> file 변수에 data 객체가 저장된다.
file.close()


# 2. pickle 파일 파이썬으로 가져오기
file = open("data.pickle", "rb")
data = pickle.load(file)
print(data)
file.close()

# 3. with 구문 사용
with open("data.txt","r", encoding="utf-8") as file:
    data = file.read()
    print(data)

