#######윤민녕 코드#######

# 약 자판기에서 판매중인
# 약 리스트와 수량을 나타내는 코드

def Vending_Machine_Medicine_List() :

    
    tylenol = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    ezn = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
    brufen = [41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]
    Panpyrin = [61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]
    pancol = [81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    bearse = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120]



    class pill:

        def __init__(self, number, name, quantity, price, efficacy):
            self.number = number
            self.name = name
            self.quantity = quantity
            self.price = price
            self.efficacy = efficacy

            print(self.number, self.name, self.quantity, self.price, self.efficacy)

    import time
    time.sleep(1)

    while True:
        print("\n"+"="*80)
        print("\n"+'숫자  이름      수량  가격(원)  효능 \n')
        print("="*80+"\n")

        pill('1.', '   타이레놀 ', len(tylenol), '   3000', '    발열 및 두통 완화\n')
        pill('2.', '   이지엔6  ', len(ezn), '   2500', '    생리통 완화\n')
        pill('3.', '   부루펜   ', len(brufen), '   6000', '    염증성 발열 완화\n')
        pill('4.', '   판피린   ', len(Panpyrin), '   1500', '    재채기 및 콧물 증상 완화\n')
        pill('5.', '   판콜     ', len(pancol), '   2600', '    감기제증상 완화\n')
        pill('6.', '   베아제   ', len(bearse), '   1700', '    소화불량 완화\n')

        break    
