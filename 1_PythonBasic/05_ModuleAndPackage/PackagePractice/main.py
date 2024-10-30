#내가 만든 모듈 메인에서 불러오는 방법
# 1. import 패키지.모듈
import unit.character
unit.character.test()

# 2. from 패키지 import 모듈
from unit import item
item.test()

# 3. from 패키지 import *
from unit import *      #unit패키지 안에 있는 모듈을 전부 불러오는 것
character.test() # * 을 이용해 모듈의 전부를 불러 올 때는 __init__ 파일로 이동해 from . import 사용할 모듈 작성해줄것.
item.test()
monster.test()

# 4. import 패키지
import unit # 이것도 3번 방법과 똑같이 __init__파일 수정 필요
unit.monster.test()
unit.character.test()
unit.item.test()