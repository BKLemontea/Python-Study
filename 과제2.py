""" 2-2번 과제 """
print("-------------------\n[2-2번 과제]\n")
numberList = []

text = input("정수 = ")
size = len(text)
text = int(text)

for a in range(size):
    numberList.append(text%10)
    text //= 10

print("입력한 정수 :", numberList)
print("입력한 정수의 합 :", sum(numberList), "\n-------------------\n")


""" 공통 과제 """
import turtle

t = turtle.Turtle()

print("-------------------\n[공통 과제]\n")
length = int(input("정수의 길이 : "))
shapes = 4
angle = 360 / shapes

radius = length / 2

t.circle(radius)

t.penup()
t.forward(radius)
t.pendown()

for i in range(shapes):   
    t.left(angle)
    t.forward(length)
print("-------------------\n")
