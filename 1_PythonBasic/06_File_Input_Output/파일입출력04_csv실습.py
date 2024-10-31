# csv 실습 (쓰기)

import csv

data = [
    ["이름","반","번호"],
    ["재석",1,2],
    ["홍철",3,8],
    ["형돈",5,32]
]

file = open("student.csv", "w", newline="", encoding="utf-8-sig")
writer = csv.writer(file)
for d in data:
    writer.writerow(d)
file.close()


# csv 실습 (읽기)
file = open("student.csv", "r",encoding="utf-8-sig")
reader = csv.reader(file)
for d in reader:
    print(d)
file.close()
