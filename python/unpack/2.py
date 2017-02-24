from sys import argv

script, user_name = argv
prompt='>> '

print("안녕 %s 나는 %s 스크립트야" % (user_name, script))
print("몆자기 질문을 할께")
print("%s 나를 좋아해?" % user_name)
likes=input(prompt)

print("%s 어디에살아?" % user_name)
lives=input(prompt)

print("무슨 종류의 컴퓨터를 가지고있어?")
computer=input(prompt)

print("""
종아 나를 좋아하냐는 질문에는 '%s'
'%s'에 살고 어딘지는 모르지만
'%s'컴퓨터를 가지고있어""" % (likes, lives, computer))
