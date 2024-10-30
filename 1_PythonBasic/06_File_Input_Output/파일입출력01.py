#1. 파일 쓰기 (덮어 쓰기)
file = open("data.txt", "w", encoding='utf-8') #파일을 생성 했을때 한글이 깨지게 된다면 encoding="원하는 인코딩 형식"을 작성해준다.
file.write("1. 스타트코딩과 함께 파이썬 공부")
file.close() #파일을 열어주었으면 꼭 닫아주기


#2. 파일 추가 (이어 쓰기)
file = open("data.txt", "a", encoding='utf-8') #파일을 생성
file.write("\n2. 비전공자도 정말 쉽게 배울 수 있습니다.")
file.close()

#3. 파일 읽기
file =  open("data.txt", "r", encoding='utf-8') #파일을 생성

#3.1 파일 전체 읽기
#data = file.read()
#print(data)
#file.close()

#3.2 파일 한 줄 읽기
while True:
    data = file.readline()
    print(data, end="")
    if data == "":
        break
file.close()


"""
파일의 한 줄 읽기는 readline으로 한 줄 씩 읽게 되면
파일의 끝이 언제인지 모르기 때문에 파일의 마지막을 알 수 있는 코드를
while문으로 작성을 해주어야한다.
"""