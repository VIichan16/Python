#위치 매개 변수
# : 가장 기본적인 매개변수
# 함수를 호출할 때 순서대로 데이터(인자)를 넘겨줘야한다.
# 다른 매개변수와 함께 쓸 때는 항상 맨 앞에 써야 한다.

#함수 정의 (positional parameter)
def my_func(a,b):
    print(a,b)

#함수 호출
my_func(1,2)


#기본 매개 변수 (Default parameter)
# : 매개변수의 기본적인(Default)값
# 함수를 정의할 때 매개변수의 기본 값을 지정할 수 있다.

#함수 정의
# : 변수 뒤에다 기본값을 대입 해주면 된다.
def post_info(title, content="내용 없음."):
    print("제목 : " , title)
    print("내용 : " , content)
    print("\n")

#함수 호출
post_info("Funtion_practice")



#키워드 매개 변수(keyword parameter)
# : 함수 호출 시에 키워드를 붙여 호출 한다.
# 매개변수의 순서를 지키지 않아도 된다.

#함수 정의
def post_info2(title, content):
    print("제목 : ", title)
    print("내용 : ", content)
    
#함수 호출
post_info2(content="없어요.", title="여자친구 만드는 방법")



