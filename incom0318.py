def escape_well():
    A = int(input("달팽이가 낮에 올라가는 거리를 정하세요(A): "))
    B = int(input("달팽이가 밤에 미끄러지는 거리를 정하세요(B): "))
    depth = 30
    if A <= B:
        print("A는 B보다 커야합니다. 다시 입력하세요")
        return
    current_height = 0
    days = 0
    while True:
        days +=1
        current_height +=A
        print("Day",days ,"낮동안 달팽이가",current_height,"미터 만큼 올라갔습니다.")
        if current_height >= depth :
            print("달팽이는",days,"일 만에 탈출 했습니다." )
            break
        current_height -=B
        print("Day",days,"밤동안 달팽이가",current_height,"미터 만큼 미끄러졌습니다.")

escape_well()







def menu():
    while True:
        print("===메뉴===")
        print("1. 현재 시간 표시")
        print("2. 날씨 정보를 가져옵니다.")
        print("3. 프로그램을 종료합니다.")
        
        choice = input("번호를 입력하세요:")

        if choice == "1":
            print("현재 시간을 표시합니다.")
        elif choice == "2":
            print("날씨 정보를 가져옵니다.")
        elif choice == "3":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")
menu()



traffic_light="빨강"

def change_light():
    global traffic_light
    if traffic_light == "빨강":
        traffic_light = "초록"
    else:
        traffic_light="빨강"

def cross_street():
    global traffic_light
    while True:
        입력값=input("행동을 입력하세요(건너기):")
        if 입력값 == "건너기":
            if traffic_light == "초록":
                print("길을 건넙니다.")
                break
            else:
                print("기다리세요")
        else:
            print("올바른 입력이 아닙니다.'건너기'를 입력하세요")
def change__light():
    global traffic_light
    user_input=input("신호를 변경하시오.(신호변경):")
    if user_input == "신호변경":
        if traffic_light=="빨강":