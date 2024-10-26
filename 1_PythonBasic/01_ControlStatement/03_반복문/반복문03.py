"""
성민은 패스트 대학교에 Lily 라는 이름의 교환학생과 친해지게 되었다.
영어를 잘하지 못했던 성민은 Lily에게 한국어를 가르쳐 주기 위해 한국어 연습
프로그램을 만들게 되었다.

-Learning Korean-
1.연습할 한국어가 담긴 리스트를 만든다.
2.리스트에서 순서대로 단어를 가져와 화면에 출력한다.
3. 프로그램 사용자는 단어를 그대로 입력하고
4. 맞추면 다음 단어를 가져온다. 틀리면 프로그램 종료

"""


kor = ["사과", "수박", "복숭아", "딸기", "망고", "두리안", "샤인머스켓"]

print("-Learning Korean-")
score = 0

for i in kor:
    print(i)
    data = input("정답 입력: ")
    if data == i:
        score += 1
        if score == 7:
            print(" ")
            print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
            print("전체 문제 : ", len(kor))
            print("맞힌 문제 : ", score)
            print("아직 안푼 문제 : ", len(kor) - score)
            print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
            print(" ")
        continue
    elif data != i:
        print(" ")
        print("전체 문제 : ", len(kor))
        print("맞힌 문제 : ", score)
        print("아직 안푼 문제 : " , len(kor) - score)
        print(" ")
        break



