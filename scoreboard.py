from turtle import Turtle

FONT = ("Arial Black", 12, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=280)
        self.high_score = 0
        self.score = 0
        self.update_score()
        self.open_high_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score = {self.score} High Score ={self.high_score}", move=False, align="center", font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.score = 0
        self.update_score()

    def open_high_score(self):
        with open("high_score.txt", "r") as file:
            self.high_score = int(file.read())

    def save_high_score(self):
        with open("high_score.txt", "w") as file:
            file.write(str(self.high_score))
