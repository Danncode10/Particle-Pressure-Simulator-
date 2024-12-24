from turtle import Turtle


class Barrier(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=40)
        self.penup()
        self.goto(0, 280)

    def move_up(self):
        if self.ycor() < 280:
            self.sety(self.ycor() + 3)

    def move_down(self):
        if self.ycor() > -280:
            self.sety(self.ycor() - 3)
