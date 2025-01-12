#importing the necessary modules and libraries
import time
import ctypes
from turtle import Screen
from bricks import Bricks
from slider import Slider
from scoreboard import Score
from lives import Live
from ball import Ball


# initialing the objects
sc = Screen()
sc.title("Break Out")
sc.bgcolor("black")
sc.setup(500,700)
sc.tracer(False)


brk = Bricks()
slider = Slider()
score = Score()
live = Live()
ball = Ball()

# event listener
sc.onkeypress(key="Left", fun=slider.move_left)
sc.onkeypress(key="Right", fun=slider.move_right)
sc.listen()

def game():
    while live.live_left >0:
        sc.update()
        time.sleep(ball.ball_speed)

        ball.free_fall()
        # checking if the ball has touched any brick
        for each_brk in brk.brick_wall:
            if ball.distance(each_brk) < 22:
                each_brk.hideturtle()
                ball.bounce_x()
                ball.bounce_y()
                ball.bounce_x()
                # removing the brick
                brk.brick_wall.remove(each_brk)
                # add a point to score
                score.add_point()
                # increasing the speed of the ball
                ball.speed_up()

        # checking if ball touched the walls and bounce accordingly
        if ball.ycor() > 325 or ball.ycor() <-325:
            ball.bounce_y()
        if ball.ycor() <= -330:
            live.remove_life()
            ball.reset_ball()
        if ball.xcor() <= -250:
            live.remove_life()
            ball.reset_ball()
        if ball.distance(slider) < 25 :
            ball.bounce_y()
        if ball.xcor() <-230 or ball.xcor() > 230:
            ball.bounce_x()

    # display message box
    rs = ctypes.windll.user32.MessageBoxW(0, "Do you want to play again!", "Game Over!", 1)
    if rs == 1:
        # resets all the parameters
        live.reset_lives()
        ball.reset_speed()
        brk.reset_wall()
        score.reset_score()
        slider.reset_slider()
        game()
# main
game()

