class Post:
    """
        게시물 클래스
        param id : 글번호
        param title : 글제목
        param content : 글내용
        param view_count : 조회수
    """
    def __init__(self, id, title, content,view_count):
        self.id = id
        self.title = title
        self.content = content
        self.param_view_count =view_count

    def set_post(self, id, title, content, view_count): #게시물 수정
        self.id = id
        self.title = title
        self.content = content
        self.param_view_count = view_count

    def add_view_count(self):
        self.param_view_count += 1

    def get_id(self): #id 속성을 반환
        return self.id
    def get_title(self): #title 속성을 반환
        return self.title
    def get_content(self): #content 속성을 반환
        return self.content
    def get_view_count(self):#view_count 속성을 반환
        return self.param_view_count




if __name__ == "__main__": # 내가 만든 메서드가 잘 작동 하는지 테스트 해주는 공간
    post = Post(1,"테스트", "테스트입니다", 0)
    #post.set_post(1,"테스트2", "테스트입니다2", 0)
    post.add_view_count()


    print(f"{post.get_id()} {post.get_title()} {post.get_content()} {post.get_view_count()}")

