""" 과제 1 """
height = 5
height = (2*height)-1
    
for count in range(1, (height+1), 2):
    text = ""
    start_point = int(height/2) - int(count/2)
    end_point = start_point + count
    for i in range(height):
        if i >= start_point and i < end_point:
            text += "*"
        else:
            text += " "
    print(text)
    

""" 과제 2 """
import turtle

t = turtle.Turtle()
length = 50
count = 5
degree = 360 / count

for c in range(count):
    t.left(degree)
    for a in range(count):
        t.forward(length)
        t.left(degree)
