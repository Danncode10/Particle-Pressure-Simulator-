from turtle import Turtle, colormode
from time import sleep
from random import randint

class Particle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.set_random_color()
        self.shape("circle")
        self.angle = randint(0, 360)
        self.goto_random_location()

    def set_random_color(self):
        colormode(255)
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        self.color(r,g,b)

    def goto_random_location(self):
        rand_x = randint(-380, 380)
        rand_y = randint(-280, 230) #Not 280 kase nandun ung barrier
        self.goto(rand_x, rand_y)
        self.showturtle()

    def detect_collision(self, barrier_coordinate):
        self.contact_y_wall(barrier_coordinate)
        self.contact_x_wall()

    def move(self):
        sleep(0.001)
        self.setheading(self.angle)
        self.forward(10)

    def contact_y_wall(self, barrier_coordinate):
        # barrier or wall contact, up and down walls
        if self.ycor() >= barrier_coordinate :
            self.bounce_y()
            self.sety(self.ycor() - 5) # -----------------> para hindi nag vibrate after touch sa barrier. (Bug fixed)
        elif self.ycor() <= -280:
            self.bounce_y()

    def contact_x_wall(self):
        # If ball touches the left or right wall, reverse x direction
        if self.xcor() >= 380 or self.xcor() <= -380:
            self.bounce_x()

    def bounce_y(self):
        self.angle = -self.angle

    def bounce_x(self):
        # Reflect the angle horizontally
        self.angle = 180 - self.angle  # reverse horizontal direction

