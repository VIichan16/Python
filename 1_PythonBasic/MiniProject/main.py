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
    f = open(file_path, "r", encoding="utf-8") #경로를 지정해준 파일을 열어 f 변수에 객체 형태로 저장
    reader = csv.reader(f) #csv 모듈을 사용하여 'f' 파일 객체를 읽기 위한 CSV 리더 객체(reader)를 생성합니다. -> 이 객체는 csv로 저장된 객체를 한줄씩 읽을 수 있게 해줌

    for data in reader: # csv 파일 객체를 저장한 reader 객체에서 한줄 씩 읽어 data 변수에 저장
        #Post 인스턴스 생성하기
        post = Post(int(data[0]),data[1],data[2],int(data[3]))  #'data' 리스트에서 각 요소를 사용하여 Post 객체를 생성합니다.
        post_list.append(post) #Post객체를 post_list에 추가
else: #파일이 경로에 없는 경우
    #파일 생성하기
    f = open(file_path, "w", encoding="utf-8", newline="")
    f.close()

#게시글 쓰기 함수
def write_post():
    """게시글 쓰기 함수"""
    print("\n\n- 게시글 쓰기 -")
    title = input("제목을 입력해주세요.\n >>>") #사용자가 입력한 제목을 title 변수에 저장
    content = input("내용을 입력해주세요.\n >>>") #사용자가 입력한 내용을 content 변수에 저장
    #글번호
    id = post_list[-1].get_id() + 1 #post_list의 마지막 요소(post_list[-1])에서 'get_id()' 메서드를 호출하여 마지막 게시글의 ID를 가져오고, 그 값에 1을 더하여 새로운 게시글의 ID를 생성합니다.
    post = Post(id,title,content,0) #새 개시글 객체를 생성
    post_list.append(post) #사용자가 작성한 내용들을 post_list에 저장
    print("# 게시글이 등록되었습니다.")


#게시글 목록보기
def list_post():
    """게시글 목록 함수"""
    print("\n\n - 게시글 목록 -")
    id_list = []
    for post in post_list:
        print(f"번호 : {post.get_id()}")
        print(f"제목 : {post.get_title()}")
        print(f"조회수 : {post.get_view_count()}")
        print("")
        id_list.append(post.get_id())

    while True:
        print("Q) 글 번호를 선택해 주세요. (메뉴로 돌아가려면 -1을 입력해주세요.)")
        try:
            id = int(input(">>>"))
            if id in id_list:
                detail_post(id)
                break
            elif id == -1:
                break
            else:
                print("없는 글 번호 입니다.")
        except ValueError:
            print("숫자를 입력해 주세요.")

# 글 상세 페이지
def detail_post(id):
    """게시글 상세 보기 함수"""
    print("\n\n - 게시글 상세 -")

    for post in post_list:
        if post.get_id() == id:
            # 조회수 1 증가
            post.add_view_count()
            print("번호 : " , post.get_id())
            print("제목 : " , post.get_title())
            print("본문 : " , post.get_content())
            print("조회수 : " , post.get_view_count())
            target_post = post

    while True:
        print("Q) 수정: 1 삭제:2 (메뉴로 돌아가려면 -1을 입력)")
        try:
            choice=int(input(">>>"))
            if choice==1:
                update_post(target_post)

                break
            elif choice ==2:
                delete_post(target_post)
                break
            elif choice == -1:
                break
            else:
                print("잘못 입력하였습니다.")
        except ValueError:
            print("숫자를 입력해 주세요.")

#게시물 수정 함수
def update_post(target_post):
    """게시물 수정"""
    print("\n\n- 게시물 수정")
    title = input("제목을 입력하세요.\n")
    content = input("본문을 입력해 주세요.\n")
    target_post.set_post(target_post.id , title, content, target_post.get_view_count())
    print("게시물이 수정되었습니다.")

#게시물 삭제 함수
def delete_post(target_post):
    """게시물 삭제"""
    post_list.remove(target_post)
    print("게시물이 삭제되었습니다.")

#게시글 저장 함수
def save():
    """게시물 저장"""
    f = open(file_path, "w", encoding="utf-8", newline="")
    writer = csv.writer(f)
    for post in post_list:
        row = [post.get_id(), post.get_title(), post.get_content(), post.get_view_count()]
        writer.writerow(row)
    f.close()
    print("# 저장이 완료 되었습니다.")
    print("# 프로그램 종료")


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
            save()
            break


