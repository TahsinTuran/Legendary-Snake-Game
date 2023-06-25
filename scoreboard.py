from turtle import Turtle
FONT = ("Arial", 15, "normal")
ALLIGNMENT = "center"




class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.updatescore()
    def updatescore(self):
        self.write(f"Score = {self.score}", align=ALLIGNMENT, font=FONT)
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!! Your Final Score: {self.score}", align=ALLIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.updatescore()
    def bigscore(self):
        self.score += 5
        self.clear()
        self.updatescore()
