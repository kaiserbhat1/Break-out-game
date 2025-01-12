from turtle import Turtle
TOTAL_LIVES = 3
class Live(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.live_left = TOTAL_LIVES
        self.hideturtle()
        self.color("red")
        self.setpos(90, 320)
        self.write("Lives: " + "❤" *self.live_left,align="left",font=('monaco',14,'bold'))

    def remove_life(self):
        self.live_left -=1
        self.__update_scr()
    def __update_scr(self):
        self.clear()
        self.write("Lives: " + "❤" * self.live_left, align="left", font=('monaco', 14, 'bold'))
    def reset_lives(self):
        self.live_left = 3
        self.__update_scr()