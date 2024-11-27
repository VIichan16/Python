#map 함수란?
# : 반복 가능한 (iterable) 객체의 각 요소에 대해 지정된 함수를 적용하여 결과를 반환


#map 함수 사용방법
# : map(함수 , 순서가 있는 자료형) -->순서가 있는 자료형 =  리스트, 튜플, 딕셔너리
map(int, ["3","4","5","6"])



#map 함수가 작동하는 과정
# 순서가 있는 자료형 ["3","4","5","6"]이 지정 함수를 한번씩 다 거치게 한다.
# 문자 자료형이 숫자형으로 변환 되고 map object가 생성된다.
# map_object(3,4,5,6)
# 이렇게 변환 된 객체를 다시 리스트로 변경하려면
# list(map_object(3,4,5,6))
# 이런식으로 리스트 함수를 사용해 변경해준다.


#리스트 모든 요소의 공백 제거
#for 문 사용
items= [" 로지텍마우스 ", " 앱솔키보드 "]
for i in range (len(items)):
    items[i] = items[i].strip()

#map 사용
def strip_all(x):
    return x.strip()

items= [" 로지텍마우스 ", " 앱솔키보드 "]
items = list(map(strip_all, items))

print(f"map = {items}")

#람다 + map 사용
items= [" 로지텍마우스 ", " 앱솔키보드 "]
items = list(map(lambda x : x.strip(), items))
print("람다 + map = ", items)


#filter 함수란?
# : 반복 가능한(iterable) 객체의 각 요소에 대해 지정된 조건을 검사하고, 그 조건을 만족하는 요소들만 걸러내는 함수.

#filter 함수 사용 방법
# filter(함수, 순서가 있는 자료형)

#예제
def func(x):
    return x < 0
filter(func , [-3,-2,0,5,7])
#조건식에 맞는 반환값들만 뽑아서 필터 객체 생성


#리스트에서 길이가 3이하인 문자들만 필터링
#for문 사용
animals = ["cat", "tiger", "dog", "bird","monkey"]
result = []
for i in animals:
    if len(i) <= 3:
        result.append(i)

print(result)

#filter 사용
animals = ["cat", "tiger", "dog", "bird","monkey"]
def word_check(x):
    return len(x) <= 3

result = list(filter(word_check, animals))
print(result)

#filter + rambda 사용
animals = ["cat", "tiger", "dog", "bird","monkey"]
result = list(filter(lambda x : len(x) <= 3, animals))
print(result)