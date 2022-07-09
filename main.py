from turtle import Screen
from paddle import Paddle
from ball import Ball
from squares import Square


def run():
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("BreakOut Game")
    screen.tracer(0)
    screen.listen()


    paddle_1 = Paddle()
    paddle_1.goto(0, -250)

    ball = Ball()

    squares = []

    space = 120
    height = 55
    
    for j in range(3):
        for i in range(6):
            square = Square()
            square.goto(-320 + space * i,260 - height * j)
            squares.append(square)



    game_over = False

    while not game_over:
        screen.update()
        ball.move()

        screen.onkeypress(paddle_1.move_right, "Right")
        screen.onkeypress(paddle_1.move_left, "Left")


        if paddle_1.distance(ball) < 50 and ball.ycor() <= -230:
            # ball.move_speed -= 0.01
            if ball.heading() == 225:
                ball.setheading(135)
            else:
                ball.setheading(45)

        for sq in squares:
            if sq.distance(ball) < 50:
                # ball.move_speed -= 0.01
                sq.reset()

    screen.exitonclick()




if __name__ == "__main__":
    run()