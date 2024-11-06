# 혼자 미니프로젝트 구현해보기 (작성자 추가)

import os.path
import csv


from post2 import Post
#파일 경로 지정
file_path = "../MiniProject_Test/data.csv"

post_list = []

if os.path.exists(file_path):
    print("게시물 로딩중...")
    file = open(file_path, "r", encoding="utf-8")
    reader = csv.reader(file)
    for data in reader:
        post = Post(int(data[0]), data[1], data[2], data[3], int(data[4]))
        post_list.append(post)
else:
    file = open(file_path, "w", encoding="utf-8", newline='')
    file.close()





#게시글 쓰기
def postWrite():
    print("\n\n- 게시글 쓰기 -")
    title = input("제목을 입력하세요.\n >>>")
    contents = input("내용을 입력하세요.\n >>>")
    author = input("작성자를 입력하세요. \n >>>")
    #글번호
    id = post_list[-1].get_id() + 1
    post = Post(id, title, contents, author, 0)
    post_list.append(post)
    print("게시물 등록 완료")

#Todo 구현중
def readPost():
    print(post_list)



while True:
    print("\n\n- FASTCAMPUS BLOG -")
    print("- 메뉴를 선택해 주세요 -")
    print("- 1. 게시글 쓰기 -")
    print("- 2. 게시글 목록 -")
    print("- 3. 프로그램 종료 -")

    try:
        choice = int(input("메뉴를 선택하세요."))

    except ValueError:
        print("숫자를 입력하세요.")
    else:
        if choice == 1:
            postWrite()
        if choice == 2:
            readPost()




