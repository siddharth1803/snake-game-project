from turtle import Screen
import time
from food import Food
from scoreboard import Score
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)

create_snake = Snake()
create_food = Food()
take_score = Score()

screen.listen()
screen.onkey(create_snake.up, "Up")
screen.onkey(create_snake.down, "Down")
screen.onkey(create_snake.left, "Left")
screen.onkey(create_snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    create_snake.move_snake()

    # detect collision with food
    if create_snake.head.distance(create_food) < 15:
        create_food.refresh()
        take_score.increase_score()
        create_snake.extend()
    # detection collision with walls
    if create_snake.head.xcor() > 280 or create_snake.head.xcor() < -280 or create_snake.head.ycor() > 280 \
            or create_snake.head.ycor() < -280:
        game_is_on = False
        take_score.game_over()
    # detect collision with body
    for segment in create_snake.segments[1:]:
        if create_snake.head.distance(segment) < 10:
            game_is_on = False
            take_score.game_over()

screen.exitonclick()
