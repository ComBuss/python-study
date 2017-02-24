from sys import argv

script, input_file = argv

def print_all(f):
    print (f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print (line_count, f.readline())

current_file = open(input_file)

print ("파일 전체를 출력해봅시다\n")

print_all(current_file)

print("테이프처럼 감아봅시다\n")

rewind(current_file)

print("세줄을 출력해봅시다")

current_line=1
print_a_line(current_line, current_file)

current_line +=1
print_a_line(current_line, current_file)

current_line +=1
print_a_line(current_line, current_file)
