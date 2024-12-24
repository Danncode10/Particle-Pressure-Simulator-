from turtle import Screen
from particle import Particle
from barrier import Barrier

def main():
    create_balls(number_of_balls)
    while True:
        screen.update()
        move_all_balls()

#Global
screen = Screen()
ball = []
barrier = None
barrier_wall = None
number_of_balls = 30

def create_barrier():
    global barrier, barrier_wall
    barrier = Barrier()
    barrier_wall = barrier.ycor() - 30
    barrier_controls()

def barrier_controls():
    screen.listen()
    screen.onkey(barrier.move_up, "Up")
    screen.onkey(barrier.move_down, "Down")

def screen_setup():
    screen.bgcolor("black")
    screen.setup(height=600, width=800)
    screen.title("Particle Simulator")
    screen.tracer(0)

def create_balls(amount):
    for new_ball in range(amount):
        new_ball = Particle()
        new_ball.detect_collision(barrier_wall) #dapat meron na agad detect collision sa barrier wall, after create
        ball.append(new_ball)

def move_all_balls():
    for i in range(len(ball)):
        ball[i].move()
        ball[i].detect_collision(barrier.ycor() - 30)

#Call
screen_setup()
create_barrier()
main()
screen.mainloop()

