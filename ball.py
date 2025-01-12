import random
from turtle import Turtle
CORD = [(10, 10), (-10, 10)]
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        pos = random.choice(CORD)
        self.__xcod = pos[0]
        self.__ycod = pos[1]
        self.ball_speed = 0.1
        self.shapesize(stretch_len=0.4,stretch_wid=0.4)
        self.shape("circle")
        self.color("red")
        self.speed("slow")
    def free_fall(self):
        xcod = self.xcor() - self.__xcod
        ycod = self.ycor() - self.__ycod
        self.goto(xcod,ycod)
    def bounce_x(self):
        self.__xcod *= -1
    def bounce_y(self):
        self.__ycod *= -1
    def speed_up(self):
        if self.ball_speed > 0.0509:
            self.ball_speed -= 0.004
    def reset_ball(self):
        self.goto(0,0)
        pos = random.choice(CORD)
        self.__xcod = pos[0]
        self.__ycod = pos[1]
        self.free_fall()
    def reset_speed(self):
        self.ball_speed = 0.1

