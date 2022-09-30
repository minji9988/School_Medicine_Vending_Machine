
# 1. 학생 데이터 저장

# 학생들의 학번을 key로 두고
# key를 통해 학생의 이름과 학생이 구매한 약 리스트를
# 저장할 수 있는 변수 선언 

Student_Name_List = {'202068062' : '강수현', '202068040' : '백홍기', 
'202068044' : '윤민녕', '202025003' : '조민지' }

Student_Medicine_Purchase_List = {'202068062' : ['약1', '약2', '약3'], 
'202068040' : ['약1', '약2', '약3'], '202068044' : [''], '202025003' : [''] }

# 강수현 = Student_Name_List.get('202068062')
# 백홍기 = Student_Name_List.get('202068040')
# 윤민녕 = Student_Name_List.get('202068044')
# 조민지 = Student_Name_List.get('202025003')

# 강수현 = []
# 백홍기 = []
# 윤민녕 = []
# 조민지 = []



# 2. 학생 본인확인

# 저장된 학생 정보를 통해 전주대 학생인지 확인하는 구문

Check_Student_Information = input("본인 확인을 위해 학번을 입력해주세요. \n\n 99번: 프로그램 종료 \n\n")
if Check_Student_Information == '99':
    print("\n\n 프로그램이 종료됐습니다.")

elif Check_Student_Information in Student_Name_List and len(Student_Medicine_Purchase_List[Check_Student_Information]) < 3 :
    print(Student_Name_List[Check_Student_Information],"님 반갑습니다.")

elif Check_Student_Information in Student_Name_List and len(Student_Medicine_Purchase_List[Check_Student_Information]) == 3 :    
    print("하루에 구매할 수 있는 약은 최대 3개 입니다. 다음에 다시 이용해주시기 바랍니다.")
else:
    print("입력하신 학번을 찾을 수 없습니다.")
    input("학번을 다시 입력해 주세요: ")


# - 각 학생들의 약 리스트
# - 하루에 학생들이 약을 구매할 수 있는
# 개수가 최대 3개, 중복구매 불가 코드 구현

# - 각각의 학생들이 약을 최대 3개 이상 구매 못하게 하고,
# 같은 약을 중복해서 구매하지 못하도록 하는 코드 구현해야 한다.




