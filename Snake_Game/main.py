from score_board import Scoreboard
from turtle import Screen, Turtle
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.09)
    snake.move()

    #Detect collision
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect wall collision
    if snake.snake_head.xcor() > 290 or snake.snake_head.xcor() < -290 or snake.snake_head.ycor() > 290 or snake.snake_head.ycor() < -290:
        is_game_on = False
        scoreboard.game_over()

    #Detect self collision
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()


screen.exitonclick()
