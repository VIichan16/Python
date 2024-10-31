"""
파일 입출력을 사용하는 이유
: 파일로부터 데이터를 읽어와서 프로그램에 사용하기 위해 사용하거나
프로그램에서 만든 데이터를 파일형태로 저장하기 위해 사용.

파일 입출력의 과정
1. 파일 열기
2. 파일 작업 (읽기, 쓰기 등)
3. 파일 닫기


파일 열기 모드
1. w : 쓰기 모드(write)
2. a : 추가 모드(append)
3. r : 읽기 모드(read)

w(write)모드와 a(append)모드 차이점
w: 덮어쓰기
a: 이어쓰기


파일 쓰기 방법
파일객체 = open("파일이름","w")
파일객체.write(데이터)
파일객체.close
ex)
file = open("data.txt","w") --> data.txt파일을 객체형태로 가져온 뒤 file변수에 담는다. 여기서, w(write)모드는 파일이름과 동일한게 없으면 새로운 파일을 만들어 낸다.
file.write("1. 스타트코딩과 함께 파이썬 공부") --> ()안에있는 데이터를 data.txt에 작성
file.close() --> 파일 닫기


파일 추가 방법
파일객체 = open("파일이름","a")
파일객체.write(데이터)
파일객체.close
ex)
file = open("data.txt","a")
file.write("2. 비전공자도 정말 쉽게 배울 수 있습니다.")
file.close()


파일 읽기 방법
파일객체 = open("파일이름","r")
변수 = 파일객체.read()
파일객체.close

ex) 파일 전체 읽기
file =  open("data.txt", "r", encoding='utf-8')
data = file.read()
file.close()

#3.2 파일 한 줄 읽기
file =  open("data.txt", "r", encoding='utf-8')
while True:
    data = file.readline()
    print(data, end="")
    if data == "":
        break
file.close()



모든 입출력 코드에서 파일이 생성되는 경로를 변경하고 싶을 땐
파일 열기에서 open("경로/파일이름","파일모드") 이렇게 경로를 지정해준다.

파일을 생성 했을때 한글이 깨지게 된다면 encoding="원하는 인코딩 형식"을 작성해준다.
ex)
file = open("data.txt", "w", encoding='utf-8')


"""