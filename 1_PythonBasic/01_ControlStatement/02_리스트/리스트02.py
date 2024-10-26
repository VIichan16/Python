""""
턱걸이 평균 측정 프로그램을 만들어보자. 먼저, 턱걸이 횟수를 저장할
빈 리스트를 만든다. 그리고 일주일간의 턱걸이 횟수를 입력받아 리스트에 저장한다.
리스트에 저장된 데이터의 평균을 구해 출력한다.

"""

pullUp = []

x = int(input("1일차 턱걸이 횟수 >>> "))
pullUp.append(x)
x = int(input("2일차 턱걸이 횟수 >>> "))
pullUp.append(x)
x = int(input("3일차 턱걸이 횟수 >>> "))
pullUp.append(x)
x = int(input("4일차 턱걸이 횟수 >>> "))
pullUp.append(x)
x = int(input("5일차 턱걸이 횟수 >>> "))
pullUp.append(x)
x = int(input("6일차 턱걸이 횟수 >>> "))
pullUp.append(x)
x = int(input("7일차 턱걸이 횟수 >>> "))
pullUp.append(x)





result = 0

total = pullUp[0] + pullUp[1] +pullUp[2] +pullUp[3] +pullUp[4] +pullUp[5] +pullUp[6]

avg = total / 7

print("평균 :" + str(avg))

