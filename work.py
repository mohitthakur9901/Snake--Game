from turtle import Turtle , Screen
from main import Snake
from food import Food
from score import Score
import time
screen=Screen()
screen.setup(height=600,width=600)
screen.bgcolor("black")
screen.title("SNAKE GAME ")
screen.tracer(0)
snake=Snake()
food=Food()
score=Score()
segment=[]
screen.listen()
screen.onkey(snake.down, "s")
onkey = screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        score.new_score()
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        is_game_on=False
        score.game_over()
    for segment in snake.segment[-1::]:
        if snake.head.distance(segment) < 5:
            is_game_on= False
            score.game_over()
    snake.move()
screen.exitonclick()