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
        self.score = 0
        self.update_score(self.score)

    def update_score(self, score):
        self.clear()
        self.write(
            arg=f"Score = {score}",
            move=False,
            align="center",
            font=FONT,
        )

    def game_over(self):
        self.clear()
        self.goto(x=0, y=0)
        self.write(
            arg="GAME OVER",
            move=False,
            align="center",
            font=FONT,
        )
