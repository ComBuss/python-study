from sys import argv

script, filename = argv

print("%r 파일을 지우려합니다" % filename)
print("취소하려먼 CTRL-C(^C)를 누르세요")
print("진행하려면 리턴을 누르세요")

input("?")

print("파일 여는중...")
target = open(filename, 'w')

print("파일 내용을 지웁니다")
target.truncate()

print("이제 세줄에 들어갈 내용을 묻겟습니다")

line1=input("1줄:")
line2=input("2줄:")
line3=input("3줄:")

print("이내용을 파일에 씁니다")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("마지막으로 닫겟습니다")
target.close()
