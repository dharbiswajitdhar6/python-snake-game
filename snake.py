from turtle import Turtle,Screen
import time
position=[(0,0),(-20,0),(-40,0)]
move_dist=20


class Snake:
    def __init__(self):
        self.snake=[]
        self.create_snake()
        self.score=0
        
    

    def create_snake(self):
        for pos in position:
            self.add_segment(pos)

    def add_segment(self,pos):
        sn=Turtle("square")
        sn.penup()
        sn.color("white")
        sn.goto(pos)
        self.snake.append(sn)
    def extend(self):
        self.add_segment(self.snake[-1].position())

    def move(self):
        for sn in range(len(self.snake)-1,0,-1):
            x=self.snake[sn-1].xcor()
            y=self.snake[sn-1].ycor()
            self.snake[sn].goto(x,y)
        self.snake[0].forward(move_dist)


    def up(self):
        if self.snake[0].heading()!=270:
            self.snake[0].setheading(90)
    
    def down(self):
        if self.snake[0].heading()!=90:
            self.snake[0].setheading(270)
    
    def left(self):
        if self.snake[0].heading()!=0:
            self.snake[0].setheading(180)

    def right(self):
        if self.snake[0].heading()!=180:
         self.snake[0].setheading(0)

    def reset(self):
        for i in self.snake:
            i.goto(1000,1000)
        self.snake.clear()
        
        self.create_snake()
        





