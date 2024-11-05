"""
1. 문자열 교체(replace)
사용 방법
"문자열".replace("변경 하고 싶은 문자" , "변경 할 문자)
ex)
"오늘 날씨는 흐림 입니다.".replace("흐림", "맑음")


2. 문자열 찾기(find)
사용 방법
"문자열".find("인덱스를 알고 싶은 문자열")
ex)
"Hello world".find("world)


3. 문자열 분리(split)
사용 방법
"문자열".split()
ex)
"나이키신발 265 X1212 78000".split("구분자") --> 구분자 입력 안할 시 공백을 기준으로 함

문자열 분리는 문자열 지정한 부분자를 기준으로 문자열을 리스트로 반환해줌


4. 문자열 공백 제거(strip)
사용 방법
"문자열".lstrip() -> 왼쪽 공백 제거
"문자열".rstrip() -> 오른쪽 공백 제거
"문자열".strip() -> 양쪽 공백 제거

ex)
"     Yeah".lstrip()
"Yeah     ".rstrip()
"     Yeah     ".strip()


"""


# 1. 문자열 교체(replace)
old ="오늘 날씨는 흐림 입니다."
print(old)
new =old.replace("흐림","맑음")
print(new)
# : 오늘 날씨는 맑음 입니다.


# 2. 문자열 찾기(find)
a = "Hello world".find("world")
print(a)
# : 6


# 3. 문자열 분리(split)
# : 1
b = "나이키신발 265 X1212 78000".split()
print(b)
# : ['나이키신발', '265', 'X1212', '78000']
c = "나이키신발:265:X1212:78000".split(":")
print(c)
# : ['나이키신발', '265', 'X1212', '78000']


# 4. 문자열 공백 제거(strip)
d = "     Yeah".lstrip()
print(d)
# : Yeah
e = "Yeah     ".rstrip()
print(e)
# : Yeah
f = "     Yeah     ".strip()
print(f)
# : Yeah
