#계절을 구분하는 프로그램

"#날짜/시간과 관련된 기능을 가져옵니다."
import datetime

#현재 날짜/시간을 구합니다."
now = datetime.datetime.now()

if 3<= now.month <=5:
    print("이번달은 {}월로 봄입니다!".format(now.month))

if 6<= now.month <=8:
    print("이번달은 {}월로 여름입니다!".format(now.month))

if 9<= now.month <=11:
    print("이번달은 {}월로 가을입니다!".format(now.month))

if 12 == now.month or now.month <= 2:
    print("이번달은 {}월로 겨울입니다!".format(now.month))