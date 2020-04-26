""" 문자열 과제 1 """
def check_word(word):
    um = ord('a')- ord('A')
    if ord(word) < ord('a'):
        return chr(ord(word) + um)
    return word

first_name = input("이름 첫째자는 : ")
middle_name = input("이름 둘째자는 : ")
last_name = input("이름 셋째자는 : ")

size = len(first_name + middle_name + last_name)

middle_name = check_word(middle_name[0])
last_name = check_word(last_name[0])
temp = ""
for i in range(len(first_name)):
    temp += check_word(first_name[i])
first_name = temp
    
name = middle_name + last_name + first_name

text = ""
for i in range(size):
    text += '*'
print(text + "(" + str(size) + ")")
print(name)

""" 문자열 과제 2 """
import turtle
t = turtle.Turtle()

angle = 360/6
length = 20

for i in range(6):
    t.forward(length)
    t.left(angle)

t.penup()
t.goto(0, length/2)
t.color("red")
t.pendown()
t.write("Stop")
