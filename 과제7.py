""" 과제 1 """
import turtle
t = turtle.Turtle()
t.shape("turtle")

def cCircle(length=50):
    t.penup()
    t.goto(0,-length)
    t.pendown()
    t.circle(length)
    t.penup()
    t.goto(0,0)
    t.pendown()
    
cCircle()
cCircle(100)
cCircle(150)

""" 과제 2 """
def D2B(decimal):
    binary = ""
    while 1:
        binary = str(decimal%2) + binary
        decimal //= 2
        if decimal == 0:
            break
    return binary

def B2D(binary):
    demical = 0
    size = len(str(binary))
    for count in range(size): 
        if (binary % 10) == 1:
            demical += 2**count
        binary //= 10
    return demical

print(D2B(int(input("10 진수 : "))))
print(B2D(int(input("2 진수 : "))))
