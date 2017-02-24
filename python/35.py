from sys import exit

def gold_room():
    print("황금으로 가득찬 방입니다 얼마나 가져갈까요?")

    next = input(">")
    if "0" in next or "1" in next:
        how_much = int(next)

    else:
        dead("인강이여 숫자 쓰는법부터 배우세요")

    if how_much < 50:
        print("좋아 욕심 부리지 않군요 당신이 이겻습니다")
        exit(0)

    else:
        dead("욕심쟁이 얼간이 같으니!")


def bear_room():
    print("여기에는 곰이 한마리있습니다")
    print("곰은 꿀을 잔뜩 들고 있습니다")
    print("뚱뚱한 곰은 다른 쪽 문앞에 있습니다")
    print("어떻게 곰을 움직이겟습니까?")
    bear_moved = False

    while True:
        next = input(">")

        if next == "꿀 뺏기":
            dead("곰이 당신을 쳐다보더니 목이 떨어져라 따귀를 날립니다")
        elif next == "곰 놀리기" and not bear_moved:
            print("문이 열렷습니다 이제 나갈수잇습니다")
            bear_moved = True
        elif next == "곰 놀리기" and bear_moved:
            dead("곰이 머리 끝까지 열받아 당신의 다리를 씹어먹습니다")
        elif next == "문열기" and bear_moved:
            gold_room()
        else:
            print("무슨 말인지 모르겟어요")


def cthulhu_room():
    print("여기에는 대악마 크툴루를 봅니다")
    print("당신을 쳐다보고 당신은 미쳐갑니다")
    print("목숨을 위해 달아나려냐 네 머리를 먹어치우려냐?")

    next = input(">")

    if "달아나기" in next:
        start()
    elif "먹기" in next:
        dead("음 맛이 좋군요!")
    else:
        cthulhu_room()

def dead(why):
    print(why,"잘 햇어요")
    exit(0)

def start():
    print("어두운방에 잇습니다")
    print("오른쪽과 왼쪽에는 문이 있습니다")
    print("어느 쪽을 고를까요?")

    next = input(">")

    if next == "왼쪽":
        bear_room()
    elif next == "오른쪽":
        cthulhu_room()
    else:
        dead("문주위 에서 맴돌기만하다 죽엇습니다")

start()
