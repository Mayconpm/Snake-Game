import time
from turtle import Screen

from food import Food
from scoreboard import ScoreBoard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")


screen.update()
game_is_on = True
score_number = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake.move()

    if snake.head.distance(food) < 15:
        print("nom nom nom")
        score_number += 1
        snake.extend()
        score.update_score(score_number)
        food.refresh()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
