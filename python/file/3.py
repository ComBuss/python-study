from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("%s에서 %s로 복사합니다" % (from_file, to_file))


indata=open(from_file).read()

print("입력 파일은 %d바이트 입리다" % len(indata))

print("출력 파일이 존재하나요? %r" % exists(to_file))
input("?")

out_file=open(to_file,'w')
out_file.write(indata)

print("모두 완료되었습니다")

out_file.close()
