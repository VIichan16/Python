#문자열 포매팅이 없다면?
# 성남님 수강기간이 7일 남았습니다.
name = "성남"
duration= 7

message = name + "님 수강기간이 " + str(duration) +"일 남았습니다."
print(message)


#문자열 포매팅 사용
message_format = f"{name}님 수강기간이 {duration}일 남았습니다."
print(message_format)


#format메서드 사용방법
# : "{인덱스}.format(데이터)
a = "Hello {0}".format("startcoding")
b = "Hello {0} {1} {2}".format("apple","pineapple","pen")
c = "Hello {} {} {}".format("apple","pineapple","pen") #인덱스 생략
print(a)
print(b)


#f-string 사용방법
# : f"{변수}"

name = "apple"
name2 = "pineapple"
name3 = "pen"

d = f"Hello {name} {name2} {name3}"
print(d)