from turtle import Turtle
FONT = ("courier", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-200, 230)
        self.level = 0
        self.update_score()
    def update_score(self):
        self.clear()
        self.write(f"level : {self.level}", align = "center", font = FONT)
    def increase_score(self):
        self.level += 1
        self.update_score()
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align = "center", font = FONT)