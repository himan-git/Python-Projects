# Using event listener to create Etch-A-Stech.

from turtle import Turtle, Screen
from logo_art import logo

print(logo)
tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(20)


def move_backward():
    tim.backward(10)


def turn_right():
    tim.right(10)


def turn_left():
    tim.left(10)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_right, "d")
screen.onkey(turn_left, "a")
screen.onkey(clear_screen, "c")
screen.exitonclick()
