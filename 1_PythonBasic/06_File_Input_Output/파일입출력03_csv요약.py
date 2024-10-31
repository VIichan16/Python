"""
csv 파일이란?
: comma-separated values의 약자로 데이터가 콤마로 구분된 텍스트 파일 형식

ex)
student.csv
이름, 반, 번호
재석,1,20
홍철,3,8
형돈,5,32

사용법
1. csv 파일 쓰기
ex)
import csv

data = [
    ["이름","반","번호"],
    ["재석",1,2],
    ["홍철",3,8],
    ["형돈",5,32]
]

file = open("student.csv", "w")
writer = csv.writer(file)
for d in data:
    writer.writerow(d)
file.close()


2. csv 파일 읽기
import csv
file = open("student.csv", "r")
reader = csv.reader(file)
for d in reader:
    print(d)
file.close()




"""