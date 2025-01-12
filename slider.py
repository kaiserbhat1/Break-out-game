from turtle import Turtle
class Slider(Turtle):
    def __init__(self):
        super().__init__()
        self.__x=0
        self.penup()
        self.goto(0,-250)
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=3.2,stretch_wid=0.5)
    def move_left(self):
        if self.__x >= -200:
            if self.__x ==190:
                self.__x-=30
            else:
                self.__x-=20
        self.goto(self.__x, -250)

    def move_right(self):
        if self.__x <= 200:
            if self.__x == 200:
                self.__x+=10
            else:
                self.__x += 20
        self.goto(self.__x, -250)
    def reset_slider(self):
        self.__x = 0
        self.goto(0,-250)