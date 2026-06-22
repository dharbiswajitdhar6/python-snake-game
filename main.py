from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen=Screen()
screen.bgcolor("black")
screen.title("My Snake Game")
screen.setup(width=600,height=600)
screen.tracer(0)#turns OFF live streaming


snake =Snake()
food=Food()
score=Scoreboard()
screen.listen()
screen.onkeypress(snake.up,"Up")
screen.onkeypress(snake.down,"Down")
screen.onkeypress(snake.left,"Left")
screen.onkeypress(snake.right,"Right")

#onkey-trigger+release then it will work
#onkeypress-trigger it will work
game_is_on=True
while game_is_on:
    screen.update()#show next frame
    time.sleep(0.1)#frame delay
    snake.move()


    if snake.snake[0].distance(food)<15:
        food.refresh()
        snake.extend()
        score.increase_score()
    
    if (snake.snake[0].xcor()>290 or snake.snake[0].xcor()<-290 or snake.snake[0].ycor()>290 or snake.snake[0].ycor()<-290):
        score.reset()
        snake.reset()
        

    #Detect collison with tail
    for nag in snake.snake[1:]:
        if snake.snake[0].distance(nag) <10:
            score.reset()
            snake.reset()
            

screen.exitonclick()