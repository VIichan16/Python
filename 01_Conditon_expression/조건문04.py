"""
프로그램 사용자로부터 국어, 수학, 영어 성적이 입력된다. 세 과목의 평균점수가 80점 이상이면 합격이다.
그런데 점수에 따라 합격 or 불합격이 정해지는 프로그램에 오류가 발생했다. 80점 이상일 경우 불합격이 표시되도록
프로그램을 작성해보자.(단, 0점에서 100점 사이의 숫자를 입력하지 않으면 "잘못 입력하였습니다."를 출력하자.)


"""

kor = float(input("국어 성적을 입력하시오. : "))
mat = float(input("수학 성적을 입력하시오. : "))
eng = float(input("영어 성적을 입력하시오. : "))

total = kor + mat + eng
avg = total / 3

if kor < 0 or kor > 100 or mat < 0 or mat > 100 or eng > 100 or eng < 0:
    print("점수를 잘못 입력하였습니다.")
else:
    if avg >= 80:
        print("평균 점수 : " + str(avg))
        print("불합격")
    else:
        print("평균 점수 : " + str(avg))
        print("합격")

