#4-1확인문제풀이

#5
numbers=[1, 2, 3, 4, 5, 6, 7, 8]
output=[[],[],[]]
for number in numbers:
    output[(number+2)%3].append(number) #리스트에 요소 추가하기/ 리스트명.append(요소)

print(output)