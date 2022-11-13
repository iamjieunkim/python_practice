#해당하는 값 모두 제거하기
#변수를 선언합니다.
list_test=[1, 2, 1, 2]
value = 2

#list_text 내부에 value값이 있다면 반복
while value in list_test:
    list_test.remove(value)

print(list_test)