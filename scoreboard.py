from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        with open("highscore.txt") as h_score:
            self.high_score=int(h_score.read())
        
        self.penup()
        self.color("white")
        self.goto(0,270)
        self.hideturtle()
        self.update_score()

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.write(f"Score :{self.score} High Score :{ self.high_score}",align="center",font=("Arial,24,normal"))
    
    def reset(self):
        if self.score>self.high_score:
            with open("highscore.txt",mode="w") as h_score:
                self.high_score=self.score
                h_score.write(f"{self.score}")
        self.score=0
        self.update_score()


    

        