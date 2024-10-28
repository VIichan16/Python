
#내장모듈
#: 파이썬 설치 시 자동으로 설치되는 모듈



#1 (모듈 이름이 길지 않을 때)
import math
print(math.pi)
print(math.ceil(2.7))


#2 (모듈 이름이 길 때)
#from 모듈이름 import 변수, 메서드
from math import pi, ceil
print(pi)
print(ceil(2.7))


#3 (메서드나 변수의 이름을 변경해서 사용하고 싶을 때)
#from 모듈이름 import 변수, 메서드 as 변경할 이름
from math import pi, ceil as kim
print(pi)
print(kim(2.7))