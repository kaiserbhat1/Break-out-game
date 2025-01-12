import random
from turtle import Turtle
class Bricks:
    def __init__(self):
        self.brick_wall = []
        self.xcod  = -220
        self.ycod = 300
        self.make_wall()
    def make_wall(self):
        for n in range(10):
            self.xcod=-220
            self.__make_bricks()
            self.ycod -= 20
    def __make_bricks(self):
        color=("yellow","pink","orange")
        for i in range(11):
            brick = Turtle("square")
            brick.penup()
            brick.speed("fastest")
            brick.hideturtle()
            brick.color("red",random.choice(color))
            brick.shapesize(stretch_len=2.09)
            brick.goto(self.xcod,self.ycod)
            brick.showturtle()
            self.brick_wall.append(brick)
            self.xcod+=43
    def reset_wall(self):
        for brk in self.brick_wall:
            brk.reset()
        self.brick_wall = []
        self.xcod = -220
        self.ycod = 300
        self.make_wall()