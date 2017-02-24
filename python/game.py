ten_things = "Apples Oranges Crows Telephone Light Suger"

print("잠깐 아직 10개가 들어있지 않으나 한번 고쳐봅시다")

stuff = ten_things.split(' ')
more_stuff=["Day","Night","Song","Frisbee","Corn","Banana","Girl","Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("추가:",next_one)
    stuff.append(next_one)
    print("이제 %d 항목이있습니다" % len(stuff))

print("이제 한번 볼까요?",stuff)
