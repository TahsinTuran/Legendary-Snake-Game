from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
import random
s = Screen()
s.setup(600, 600)
s.bgcolor("black")
s.title("The Snake Game by Turan")
s.tracer(0)
snake = Snake()
s.listen()
food = Food()
scoreboard = ScoreBoard()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.right, "Right")
s.onkey(snake.left, "Left")

is_game_on = True
while is_game_on:
    s.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food) < 17:
        if food.shapesize() == (0.8, 0.8, 1):
            scoreboard.bigscore()
            snake.bigextend()
        else:
            scoreboard.increase_score()
            snake.extend()
        food.which()
            

    if snake.segments[0].xcor() > 299 or snake.segments[0].xcor() < -299 or snake.segments[0].ycor() > 299 or snake.segments[0].ycor() < -299:
        is_game_on = False
        scoreboard.game_over()
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()

s.exitonclick()
