import os.path
import csv

from post import Post
#파일경로
file_path = "../MiniProject/data.csv"

#post 객체를 저장할 리스트
post_list = []


#data.csv 파일이 있다면
if os.path.exists(file_path): #os.path.exists(file_path) --> 위에서 지정해준 경로에 파일이 있다면 true 반환
    # 게시글 로딩
    print("게시글 로딩중...")
    f = open(file_path, "r", encoding="utf-8")
    reader = csv.reader(f)
    for data in reader:
        #Post 인스턴스 생성하기
        post = Post(int(data[0]),data[1],data[2],int(data[3]))
        post_list.append(post)
else: #파일이 경로에 없는 경우
    #파일 생성하기
    f = open(file_path, "w", encoding="utf-8", newline="")
    f.close()

#게시글 쓰기 함수
def write_post():
    """게시글 쓰기 함수"""
    print("\n\n- 게시글 쓰기 -")
    title = input("제목을 입력해주세요.\n >>>")
    content = input("내용을 입력해주세요.\n >>>")
    #글번호
    id = post_list[-1].get_id() + 1 #리스트 마지막 요소를 가져오고 싶을 땐 -1
    post = Post(id,title,content,0)
    post_list.append(post)
    print("# 게시글이 등록되었습니다.")

# Todo 구현 중 나중에 구현이 되면 삭제 할 것!
#게시글 목록보기
def list_post():
    """게시글 목록 함수"""
    print("\n\n - 게시글 목록 -")
    for post in post_list:
        print(f"번호 : {post.get_id()}")
        print(f"제목 : {post.get_title()}")
        print(f"조회수 : {post.get_view_count()}")
        print("")

    while True:
        print("Q) 글 번호를 선택해 주세요. (메뉴로 돌아가려면 -1을 입력해주세요.)")
        id = int(input(">>>"))


# 메뉴 출력하기
while True:
    print("\n\n- FASTCAMPUS BLOG -")
    print("- 메뉴를 선택해 주세요 -")
    print("- 1. 게시글 쓰기 -")
    print("- 2. 게시글 목록 -")
    print("- 3. 프로그램 종료 -")

    try:
        choice = int(input(">>>"))
    except ValueError:
        print("숫자를 입력해주세요.")
    else:
        if choice == 1:
            write_post()
        elif choice == 2:
            list_post()
        elif choice == 3:
            print("프로그램 종료")
            break


