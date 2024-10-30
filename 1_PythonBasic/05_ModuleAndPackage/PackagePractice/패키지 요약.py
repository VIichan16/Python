"""
패키지란?
: 관련 있는 모듈을 하나의 폴더로 구성해 놓은 것

내가 만든 모듈들을 main에서 불러 오는 법
1. import 패키지.모듈 --> 특정 모듈만 불러올 때 사용
ex)
불러오기 -> import unit.character
사용하기 -> unit.character.test()


2. from 패키지 import 모듈 --> 특정 모듈만 불러올 때 사용 1번이랑 불러오는건 똑같지만 모듈의 함수를 사용할 때 코드가 조금더 간결해짐
ex)
불러오기 -> from unit import character
사용하기 -> character.test()


3. from 패키지 import * --> 패키지 안에 있는 모든 모듈을 불러 올 때 사용
* 을 이용해 모듈의 전부를 불러 올 때는 __init__ 파일로 이동해 from . import 사용할 모듈 작성 해줄 것.
__init__파일에 작성 해줘야 하는 것 : from . import character, item, monster --> 현재 위치로 부터 character, item, monster 모듈을 불러온다.
ex)
불러 오기 -> from unit import *
사용 하기 -> character.test()


4. import 패키지
4번 방법도 3번이랑 똑같이 __init__ 파일 수정 필요.
ex)
불러 오기 -> import unit
사용 하기
unit.monster.test()
unit.character.test()
unit.item.test()


"""
