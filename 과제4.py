""" 리스트 과제 1 """
score_list = []

score_list.append(int(input("국어 점수는 : ")))
score_list.append(int(input("수학 점수는 : ")))
score_list.append(int(input("영어 점수는 : ")))
score_list.append(int(input("과학 점수는 : ")))
score_list.append(int(input("사회 점수는 : ")))

reverse_list = score_list[:]
reverse_list.sort(reverse=True)
score_avg = sum(score_list)/len(score_list)

print("입력 자료 : %s\n정렬 자료 : %s\n평균 점수 : %.1f" %(score_list, reverse_list, score_avg))


""" 리스트 과제 2 """
import turtle

t = turtle.Turtle()
color_list = [
    "red",
    "green",
    "blue",
]

length = 50
t.right(180)

t.fillcolor(color_list[0])
t.begin_fill()
t.circle(length, steps=3)
t.end_fill()

t.penup()
t.goto( ((((3 ** 0.5)/2)*length)*2)*1, 0 )
t.pendown()

t.fillcolor(color_list[1])
t.begin_fill()
t.circle(length, steps=3)
t.end_fill()

t.penup()
t.goto( ((((3 ** 0.5)/2)*length)*2)*2, 0 )
t.pendown()

t.fillcolor(color_list[2])
t.begin_fill()
t.circle(length, steps=3)
t.end_fill()
