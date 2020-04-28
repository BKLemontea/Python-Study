""" 과제 1 """
fst_input = int(input("a 입력 : "))
sec_input = int(input("b 입력 : "))

if fst_input == sec_input:
    print("a와 b는 같다")
elif fst_input > sec_input:
    result = fst_input - sec_input
    print("a가 b보다 " + str(result) + " 만큼 더 크다")
else:
    result = sec_input - fst_input
    print("b가 a보다 " + str(result) + " 만큼 더 크다")


""" 과제 2 """
import random
user = input("[가위, 바위, 보] 중에 입력해주십시오 : ")
if user == "가위" or user == "바위" or user == "보":  
    computer = random.choice(["가위", "바위", "보"])
    print("컴퓨터 입력 : " + computer)
    if user == computer:
        print("결과 : 무승부")
    elif (user == "가위" and computer == "보") or (user == "바위" and computer == "가위") or (user == "보" and computer == "바위"):
        print("결과 : 승리")
    else:
        print("결과 : 패배")
    
else:
    print("[가위, 바위, 보] 중에 입력해주십시오")


""" 과제 3 """
import turtle
from math import degrees, atan

t = turtle.Turtle()

var_list = []
var_list.append(int(input("변1 : ")))
var_list.append(int(input("변2 : ")))
var_list.append(int(input("변3 : ")))
var_list.sort()

if var_list[2] == (((var_list[0]**2) + (var_list[1]**2)) ** 0.5):
    var_list[0] *= 10
    var_list[1] *= 10
    var_list[2] *= 10
    
    A = degrees(atan(var_list[1]/var_list[0]))
    B = 90 - A

    t.forward(var_list[0])
    t.left(90)
    t.forward(var_list[1])
    t.left(90 + A)
    t.forward(var_list[2])
    t.left(90 + B)
else:
    t.write("직각삼각형이 아님:")
