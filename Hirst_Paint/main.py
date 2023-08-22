import turtle as t
import random
from logo_art import logo


print(logo)
t.colormode(255)
tim = t.Turtle()

color_list = [(74, 12, 74), (19, 16, 12), (255, 27, 30), (15, 17, 44), (16, 81, 110), (109, 213, 26), (97, 172, 206), (33, 159, 170), (41, 70, 53), (8, 21, 166), (100, 220, 200), (124, 187, 229), (7, 5, 255), (215, 130, 149), (251, 24, 155), (23, 27, 26), (124, 45, 45), (22, 58, 12), (14, 77, 22), (185, 41, 220), (88, 246, 249), (169, 4, 10), (132, 21, 6), (4, 28, 49), (23, 15, 87), (108, 106, 218), (23, 23, 67), (10, 45, 15), (19, 241, 18)]

tim.speed(0)
tim.setheading(225)
tim.penup()
tim.hideturtle()
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(16, random.choice(color_list))
    tim.forward(50)
    
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.seth(180)
        tim.forward(500)
        tim.setheading(0)


screen = t.Screen()
screen.exitonclick()
