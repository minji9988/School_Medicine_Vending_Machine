#######윤민녕 코드#######

# 약 자판기 사용 전에 주의해야 할 부분 출력 코드

import time
from Close_Message import Close_Message

time.sleep(1)

def Notice():
    print("""\n\n
 
            .__   __.   ______   .___________. __    ______  _______ 
            |  \ |  |  /  __  \  |           ||  |  /      ||   ____|
            |   \|  | |  |  |  | `---|  |----`|  | |  ,----'|  |__   
            |  . `  | |  |  |  |     |  |     |  | |  |     |   __|  
            |  |\   | |  `--'  |     |  |     |  | |  `----.|  |____ 
            |__| \__|  \______/      |__|     |__|  \______||_______|
                                                            
    
    """)
    print("="*80+"\n")

    print('1. 약물오남용 방지와 타 학우분들을 위해\n   1인당 하루에 3개 이하의 약만 구매해주시기 바랍니다.\n')
    print('2. 해당 자판기는 전주대 학생에 한해서 서비스를 제공하고 있습니다.\n   전주대 학생이 아닌 경우, 자판기 이용이 불가합니다.\n')
    print('3. 구매하신 약의 주의사항을 확인 하시고 사용해주세요.\n')

    print("="*80+"\n")

    print('1번. 시작하기\n99번. 종료하기\n')

    number = int(input('선택해주세요 : '))

    while(True):
        if number == 1:
            break

        elif number == 99:
            Close_Message()
            
        else :
            number = int(input("번호를 정확히 입력해 주세요. : "))
