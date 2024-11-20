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
def listPost():
    print("\n\n- 게시물 목록 -")
    id_list = []
    for post in post_list:
        print(f"게시물번호: {post.id}")
        print(f"제목: {post.title}")
        print(f"작성자: {post.author}")
        print(f"조회수: {post.view_count}\n")
        print("")
        id_list.append(post.id)

    while True:
        print("Q) 글 번호를 선택해 주세요. (메뉴로 돌아가려면 -1을 입력해주세요.)")
        id = int(input(">>>"))
        if id in id_list:
            detail_post(id)
            break


#글 상세 페이지
def detail_post(id):
    """게시글 상세 보기 함수"""
    print("\n\n - 게시글 상세 -")

    for post in post_list:
        if post.get_id() == id:
            # 조회수 1 증가
            post.add_view_count()
            print("번호 : ", post.get_id())
            print("제목 : ", post.get_title())
            print("본문 : ", post.get_content())
            print("작성자 : ", post.get_author())
            print("조회수 : ", post.get_view_count())
            target_post = post

    while True:
        print("Q) 수정: 1 삭제:2 (메뉴로 돌아가려면 -1을 입력)")
        try:
            choice = int(input(">>>"))
            if choice == 1:
                #수정 함수
                break
            elif choice == 2:
                #삭제함수
                break
            elif choice == -1:
                break
            else:
                print("잘못 입력하였습니다.")
        except ValueError:
            print("숫자를 입력해 주세요.")

#Todo 업데이트 구현






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
            listPost()
        if choice == 3:
            break




