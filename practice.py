#if조건문에 else구믄을 추가해서 짝수와 홀수 구분

#입력을 받습니다.
number=input("정수입력> ")
number=int(number)

#if조건문을 사용합니다.
if number%2 == 0:
    print("짝수입니다.") #조건이 참일 때, 즉 짝수조건
else:
    print("홀수입니다.") #조건이 거짓일 때, 즉 홀수조건