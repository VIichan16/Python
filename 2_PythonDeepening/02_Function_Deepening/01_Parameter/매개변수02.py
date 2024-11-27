# 위치 가변 매개변수
# : 개수가 정해지지 않은 매개변수
# 매개변수 앞에 *가 붙는다. (튜플형)

#함수 정의
def print_fruits(*args):
    for arg in args:
        print(arg)
    print("\n")


#함수 호출
print_fruits("apple", "orange", "mango")


# 키워드 가변 매개변수
# : 개수가 정해지지 않은 매개변수
# 매개변수 앞에 **가 붙는다.(딕셔너리)

#함수 정의
def comment_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    print("\n")

#함수 호출
comment_info(apple="사과", mango = "망고" , orange = "오렌지")


#매개변수 작성 순서
# 위치 - 기본 - 위치 가변 - 키워드(기본) - 키워드 가변

"""
def post_info(*tags , title, content):
    print(f"제목 : {title}")
    print(f"내용 : {content}")
    print(f"태그 : {tags}")

#함수 호출
post_info("#파이썬", "#함수","파이썬 함수 정리", "다양한 매개변수 정리합니다.") --> 이렇게 작성하게 되면 *tags 매개변수가 인자를 전부 받기 때문에 title, content가 인자를 못 받았다고 오류가뜸.

"""
#위 상황의 해결 방법
# 1. 매개변수 순서 변경
def post_info(title, content,*tags):
    print(f"제목 : {title}")
    print(f"내용 : {content}")
    print(f"태그 : {tags}\n")

post_info("파이썬 함수 정리", "다양한 매개변수 정리합니다.""#파이썬", "파이썬","#함수")

# 2. 키워드 매개변수를 같이 사용.
def post_info2(*tags , title, content):
    print(f"제목 : {title}")
    print(f"내용 : {content}")
    print(f"태그 : {tags}\n")

post_info2("#파이썬", "#함수", title = "파이썬 함수 정리", content = "다양한 매개변수 정리합니다." )


