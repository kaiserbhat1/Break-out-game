from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white","red")
        self.setpos(-240, 320)
        self.__points = 0
        self.write(f"Score: {self.__points}",align="left",font=('monaco',14,'bold'))
    def add_point(self):
        self.__points += 1
        self.__update_scr()
    def __update_scr(self):
        self.clear()
        self.write(f"Score: {self.__points}",align="left",font=('monaco',14,'bold'))
    def reset_score(self):
        self.__points = 0
        self.__update_scr()


