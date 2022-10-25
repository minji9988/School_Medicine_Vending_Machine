######## Main 코드#########

# 프로그램 종료 메세지
from Close_Message import Close_Message

# 프로그램 시작 메세지 출력
from Welcom_Message import Welcome_Message
Welcome_Message()


#  Name_List: 학생의 학번과 이름을 저장한 변수
Name_List = {'22206425' : '토끼', '20206243' : '나비', 
        '20212444' : '캥거루', '202454544' : '부엉이' }


# Medicine_List: 학생이 선택한 약이 저장되는 변수
Medicine_List = {'22206425' : [], 
'20206243' : [], '20212444' : [], '202454544' : [] }

# 예) 토끼학생이 타이레놀과 부루펜을 선택했다면
# 토끼의 학번인 22206425에 있는 [] 빈 리스트에 ["타이레놀", "부루펜"] 형식으로 저장됨


# Student_Numeber: 학생 학번을 입력받는 변수
Student_Number = input("\t\t      본인 확인을 위해 '학번'을 입력해주세요. \n\n\t\t\t\t  99번. 종료하기 \n\n\n\n\n") 


# Student_DB: 동물학교 학생인지 확인하는 함수
def Student_DB():
        global Student_Number
        while True :                
                # 1) 학생이 프로그램을 종료하려는 경우
                if Student_Number == '99':
                      Close_Message()

                # 2) 학생이 학번을 올바르게 입력한 경우
                elif Student_Number in Name_List:
                        Student_Name = Name_List[Student_Number]

                        # 2-1) 학생이 오늘 하루 약을 2개 이하 구매한 학생인 경우 
                        if Student_Number in Name_List and len(Medicine_List[Student_Number]) < 3 :
                                print(f"안녕하세요, {Student_Name}님")
                                break
                        
                        #2-2) 학생이 오늘 하루 약을 3개 구매한 학생이라면 프로그램이 종료된다.
                        # 약물남용 및 타 학우들을 위해 하루에 1인당 3개의 약만 구매할 수 있도록 제한했다.
                        elif Student_Number in Name_List and len(Medicine_List[Student_Number]) == 3 :
                                num = input("하루에 구매할 수 있는 약은 최대 3개 입니다.\n다음에 다시 이용해주시기 바랍니다.\n99번: 종료하기 ") #num=종료 변수
                                if num == '99':
                                    print("프로그램이 종료되었습니다.")
                                Close_Message()


                # 3) 학생이 학번을 잘못 입력한 경우
                else:
                        print("\n입력하신 학번을 찾지 못했습니다.\n")
                        Student_Number = input("본인 확인을 위해 학번을 다시 입력해주세요. \n\n 99번. 종료하기\n\n")
                                


Student_DB()


# 약 자판기 사용시 주의사항 출력
from Notice import Notice
Notice()


# 각각의 약 수량을 20개로 설정

tylenol = []
ezn = []
brufen = []
Panpyrin = []
pancol = []
bearse = []

for i in range(1, 21):
    tylenol.append(1)
    if len(tylenol) == 20:
        pass
    ezn.append(1)
    if len(ezn) == 20:
        pass
    brufen.append(1)
    if len(brufen) == 20:       
        pass
    Panpyrin.append(1)
    if len(Panpyrin) == 20:       
        pass
    pancol.append(1)
    if len(pancol) == 20:       
        pass
    bearse.append(1)
    if len(bearse) == 20:       
        pass


# 자판기에서 판매중인 약 리스트 호출
from Medicine_List import Vending_Machine_Medicine_List
Vending_Machine_Medicine_List()



# 약 수량 감소 기능 

# 약 변수 지정
# 변수 지정 이유: 리스트에 추가할 수 있는 건 변수뿐이기 때문
a= '타이레놀'
b= '이지엔6'
c= '부루펜'
d= '판피린'
e= '판콜'
f= '베아제'


# 아래의 buy_additional() 함수는 학생이 약을 선택하면 약 리스트에서 수량이 줄어들도록 하는 함수다.
# 예) 타이레놀이 총 20개 있는데 학생이 타이레놀을 선택했다면
# 타이레놀 수량이 19개로 줄어드는 것이다.


def buy_additional1():
        print("하루 최대 구매하실 수 있는 약은 3개입니다.\n8번: 결제창으로 넘어가기\t99번: 종료하기")
        for buypill in range(2) :
            buypill=input("\n구매하실 약의 '번호'를 입력하고, 'Enter' 키를 눌러주세요.\n8번. 추가로 구매할 약 없음\n\n")
            if buypill == '1':
                del tylenol[0] #타이레놀 리스트에서 하나 삭제
                Medicine_List[Student_Number].append(a) #리스트에 이름 추가
            elif buypill == '2':
                del ezn[0] #이지엔6 리스트에서 하나 삭제
                Medicine_List[Student_Number].append(b) #리스트에 이름 추가
            elif buypill == '3':
                del brufen[0] #부루펜 리스트에서 하나 삭제
                Medicine_List[Student_Number].append(c) #리스트에 이름 추가
            elif buypill == '4':
                del Panpyrin[0] #판피린 리스트에서 하나 삭제
                Medicine_List[Student_Number].append(d) #리스트에 이름 추가
            elif buypill == '5':
                del pancol[0] #판콜 리스트에서 하나 삭제
                Medicine_List[Student_Number].append(e) #리스트에 이름 추가
            elif buypill == '6':
                del bearse[0] #베아제 리스트에서 하나 삭제
                Medicine_List[Student_Number].append(f) #리스트에 이름 추가
            elif buypill == '99':
                Close_Message()
            else:
                break

def buy_additional2():
        print("하루 최대 구매하실 수 있는 약은 3개입니다.\n8번: 결제창으로 넘어가기\t99번: 종료하기")
        for buypill in range(1) :
            buypill=input("\n구매하실 약의 '번호'를 입력하고, 'Enter' 키를 눌러주세요.\n8번. 추가로 구매할 약 없음\n\n")
            if buypill == '1':
                del tylenol[0] #타이레놀 리스트에서 하나 삭제
                Medicine_List[Student_Number].append(a) #리스트에 이름 추가
            elif buypill == '2':
                del ezn[0] #이지엔6 리스트에서 하나 삭제
                Medicine_List[Student_Number].append(b) #리스트에 이름 추가
            elif buypill == '3':
                del brufen[0] #부루펜 리스트에서 하나 삭제
                Medicine_List[Student_Number].append(c) #리스트에 이름 추가
            elif buypill == '4':
                del Panpyrin[0] #판피린 리스트에서 하나 삭제
                Medicine_List[Student_Number].append(d) #리스트에 이름 추가
            elif buypill == '5':
                del pancol[0] #판콜 리스트에서 하나 삭제
                Medicine_List[Student_Number].append(e) #리스트에 이름 추가
            elif buypill == '6':
                del bearse[0] #베아제 리스트에서 하나 삭제
                Medicine_List[Student_Number].append(f) #리스트에 이름 추가
            elif buypill == '99':
                Close_Message()
            else:
                break

def buy_additional3():
        for buypill in range(3) :
            buypill=input("\n구매하실 약의 '번호'를 입력하고, 'Enter' 키를 눌러주세요.\n8번. 추가로 구매할 약 없음\n\n")
            if buypill == '1':
                del tylenol[0] #타이레놀 리스트에서 하나 삭제
                Medicine_List[Student_Number].append(a) #리스트에 이름 추가
            elif buypill == '2':
                del ezn[0] #이지엔6 리스트에서 하나 삭제
                Medicine_List[Student_Number].append(b) #리스트에 이름 추가
            elif buypill == '3':
                del brufen[0] #부루펜 리스트에서 하나 삭제
                Medicine_List[Student_Number].append(c) #리스트에 이름 추가
            elif buypill == '4':
                del Panpyrin[0] #판피린 리스트에서 하나 삭제
                Medicine_List[Student_Number].append(d) #리스트에 이름 추가
            elif buypill == '5':
                del pancol[0] #판콜 리스트에서 하나 삭제
                Medicine_List[Student_Number].append(e) #리스트에 이름 추가
            elif buypill == '6':
                del bearse[0] #베아제 리스트에서 하나 삭제
                Medicine_List[Student_Number].append(f) #리스트에 이름 추가
            elif buypill == '99':
                Close_Message()
            else:
                break
            

# buy_additional1,  buy_additional2, buy_additional3이 있는 이유
# 학생이 약을 1개 선택하고 바로 8번 버튼(결제하기)를 눌러서
# 결제창으로 바로 넘어가게 하기 위해선 buy_additional 함수가 3개가 필요했다.
# 학생이 약을 1개 선택했을 경우, 2개 선택했을 경우, 3개 선택했을 경우에 맞춰서
# 함수를 만들어줘야 8번 버튼(결제창 넘어가기)을 눌렀을 때 바로 결제창으로 넘어간다.
# 이렇게 함수를 3개 만들지 않게 된다면 학생이 약을 1개 선택하고
# 8번을 눌러서 결제창으로 넘어가고자 할 때 8번을 2번 눌러야 결제창으로 이동하는 번거로움이 따른다.      


#학생이 약을 1개 선택했을 때
if Student_Number in Name_List and len(Medicine_List[Student_Number]) == 1 :
        buy_additional1()
                                
# 학생이 약을 2개 선택했을 때 
elif Student_Number in Name_List and len(Medicine_List[Student_Number]) == 2 :
        buy_additional2()

# 학생이 약을 0개 선택했을 때 실행
elif Student_Number in Name_List and len(Medicine_List[Student_Number]) == 0 :
        buy_additional3()
                

# choice 함수: 사용자가 선택한 약을 보여주는 함수
# 예) 만약 토끼가 부루펜과 타이레놀을 선택했다면
# 구매하실 약이 [부루펜, 타이레놀] 이 맞습니까? 라고 뜬다.
 
def choice():
    print('\n\n\n구매하실 약이 ', Medicine_List.get(Student_Number), '맞습니까?\n') #학번의 리스트안에 구매한 약 이름 출력 & 선택지 출력
    answer = input("1번. 맞습니다 \n99번. 종료하기\n\n") 
    
    while(True):
        if answer == '1' :
                print("\n결제창으로 넘어갑니다.")
                break
        elif answer == '99':
                Close_Message()
        else:
                answer = input("\n\n숫자를 잘못 입력하셨습니다.\n다시 입력해주세요.\n\n")
    
choice()





# 결제 기능 

# 학생이 선택한 약 가격을 모두 더한 후, 지불할 돈을 계산해서 보여주고
# 잔돈을 거슬러 주거나 부족한 돈을 추가로 지불할 수 있도록 구현


# 학생이 선택한 약 가격을 담는 변수
Total = 0


# 학생이 선택한 약 가격을 더하는 함수 
def Add_Medicine_Price ():
        global Total    
        if Medicine_List[Student_Number][i] == "타이레놀":
                Total += 3000
        elif Medicine_List[Student_Number][i] == "이지엔6":
                Total += 2500
        elif Medicine_List[Student_Number][i] == "부루펜":
                Total += 6000  
        elif Medicine_List[Student_Number][i] == "판피린":
                Total += 1500
        elif Medicine_List[Student_Number][i] == "판콜":
                Total += 2600
        elif Medicine_List[Student_Number][i] == "베아제":
                Total += 1700



# 1) 학생이 구매한 약이 3개일 경우 실행되는 계산식 
if len(Medicine_List[Student_Number]) == 3:

        for i in range(3):
                Add_Medicine_Price()


# 2) 학생이 구매한 약이 2개인 경우 실행되는 계산식
elif len(Medicine_List[Student_Number]) == 2:

        for i in range(2):
                Add_Medicine_Price()


# 3) 학생이 구매한 약이 1개인 경우 실행되는 계산식
else:
        for i in range(1):
                Add_Medicine_Price()


print('''\n\n\n          <결제창>    \n''')
print(f"\n지불하실 금액은 {Total}원입니다.")

# 학생이 지불한 금액을 저장하는 Money 변수 선언
Money = int(input("돈을 투입구에 넣어주세요. \n\n99번. 종료하기\n\n"))


# 학생이 돈을 지불하지 않고 프로그램을 종료하는 경우
if Money == 99:
        Close_Message()


# 지불해야 할 돈에 맞게 돈을 지불한 경우
elif Money == Total:
        print('''\n\n\n          -구매완료-    \n''')
        print("\n\n구매가 완료됐습니다. \n투입구에서 약을 받아가 주세요.")
        Close_Message()


# 지불해야 할 돈보다 더 많은 돈을 지불한 경우
elif Money > Total:

        # 거스름돈을 저장할 Change 변수 선언
        Change = Money - Total
        print('''\n\n\n          -구매완료-    \n''')
        print(f"구매가 완료됐습니다. \n투입구에서 약과 거스름돈 {Change}원을 받아가주세요.")
        Close_Message()


# 부족한 금액을 지불한 경우
else :
        # 얼마나 부족한 금액을 지불했는지 알려주는 lack_money 변수 선언
        # 예) 5000원을 지불해야하는데 학생이 1000원을 지불했다면 4000원을 덜 지불한 것이니
        # lack_money에는 4000원이 저장된다.
    lack_money = abs(Money - Total)
    print('''\n\n\n          -잔액부족-    \n''')
    print(f"\n투입하신 돈이 {lack_money}원 부족합니다.")

    while True:
        #학생이 추가로 지불한 돈을 저장하는 Pay_Extra 변수 선언
        Pay_Extra = int(input("돈을 추가로 투입해주세요. \n\n99번. 종료하기 \n\n"))


        if Pay_Extra == 99:
            Close_Message()

        elif Pay_Extra == lack_money:
            print('''\n\n\n          -구매완료-    \n''')
            print("\n구매가 완료됐습니다. \n투입구에서 약을 받아가 주세요.")
            Close_Message()

        elif Pay_Extra < lack_money:
            lack_money = abs(Pay_Extra - lack_money)
            print('''\n\n\n          -잔액부족-    \n''')
            print(f"\n투입하신 돈이 {lack_money}원 부족합니다.\n")
            continue


                # 지불해야 할 돈보다 더 많은 돈을 지불한 경우
        elif Pay_Extra > lack_money:

                        # 거스름돈 변수인 Change 선언
                        
            Change = lack_money - Pay_Extra
            print('''\n\n\n          -구매완료-    \n''')
            print(f"구매가 완료됐습니다. \n투입구에서 약과 거스름돈 {Change}을 받아가주세요.")
            Close_Message()

