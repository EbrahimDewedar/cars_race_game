from turtle import Turtle
MOVE_DISTANCE = 10
STARTING_POSITION = (0,-280)
FINISH_LINE_Y = 280
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
    def go_up(self):
        self.forward(MOVE_DISTANCE)
    def go_to_start(self):
        self.goto(STARTING_POSITION)
    def is_at_finish_line(self):
        if self.ycor() > 280:
            return True
        else:
            return False
