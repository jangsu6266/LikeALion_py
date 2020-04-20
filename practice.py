x=1
while (x != 0):
    print("구구단 몇단을 계산할까요?")
    x= int(input())
    if x==0:
        break
    if not(1<=x<=9):
        print("잘못 입력했습니다. 1-9사이 숫자를 입력하세요.")
    else :
        print('구구단 ""단을 계산합니다.',str(x))
        for i in range(1,10):
            print(str(x)+"X"+str(i)+'='+str(x*i))
print("구구단을 종료합니다.")