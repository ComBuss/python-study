def print_two(*args):
    arg1,arg2=args
    print("실행인자: %r, 실행인자: %r" % (arg1,arg2))

def print_two_again(arg1,arg2):
    print("실행인자: %r, 실행인자: %r" % (arg1,arg2))

def print_one(arg1):
    print("실행인자1: %r" % arg1)

def print_none():
    print("아무것도 받지않음")

print_two("zed", "shaw")
print_two_again("Zed", "Shaw")
print_one("First!!")
print_none()
