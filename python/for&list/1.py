the_count = [1,2,3,4,5]
fruits = ['사과','귤','배','살구']
change = [1,'십원','2','백원','3','오백원']

for number in the_count:
    print("이수는 %d" % number)

for fruit in fruits:
    print("과일 종류: %s" % fruit)

for i in change:
    print("받은 잔동 %s" % i)

elements = []

for i in range(0,6):
    print("list에 %d숫자를 더합니다" % i)
    elements.append(i)

for i in elements:
    print("원소는 %d" % i)
