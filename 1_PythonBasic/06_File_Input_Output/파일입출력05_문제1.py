"""
보유한 주식이 목표가에 도달했을 때의 종목별 수익금과 수익률을 출력해주는 프로그램을 작성해보자.
mystock.csv 파일로 부터 종목, 매입가, 수량, 목표가 정보를 가져온다.


종목, 매입가, 수량, 목표가
삼성전자,85000,10,90000
NAVER, 380000,5,400000

"""



import csv

def show_profit(data):
    name = data[0] #종목
    purchase_price = int(data[1]) #매입가
    amout = int(data[2]) # 수량
    target_price = int(data[3]) # 목표가
    
    profit = (target_price - purchase_price) * amout #수익금
    profit_ratio = (target_price/purchase_price -1) * 100 # 수익률

    print(f"{name} {profit} {profit_ratio:.2f}%")



# CSV 파일을 열기
file = open("..\\06_File_Input_Output\\mystock.csv ", 'r', encoding='utf-8')

# CSV 파일 내용을 리스트로 변환하여 reader 변수에 저장
reader = list(csv.reader(file))  # 리스트 형변환

# reader의 첫 번째 줄을 제외하고 각 데이터에 대해 show_profit 함수 호출
for data in reader[1:]:
    show_profit(data)

# 파일 닫기
file.close()