#main.py

from turtle import Screen, Turtle
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


    lives = 3
    blocks = 18

    score = Turtle()
    score.goto(220,-280)
    score.color('white')
    score.hideturtle()
    score.write(f"Lives: {lives} | Block remaining: {blocks}", False, align='center', font=('Courier', 18, 'normal'))

    game_over = True

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

        score.clear()
        score.write(f"Lives: {lives} | Block remaining: {blocks}", False, align='center', font=('Courier', 18, 'normal'))

        screen.onkeypress(paddle_1.move_right, "Right")
        screen.onkeypress(paddle_1.move_left, "Left")


        if paddle_1.distance(ball) < 50 and ball.ycor() <= -230:
            if ball.heading() == 225:
                ball.setheading(135)
            else:
                ball.setheading(45)

        if ball.ycor() <= -280:
            ball.goto(0,0)
            lives -= 1
            
            if lives == 0:
                game = Turtle()
                game.color('white')
                game.goto(0,0)
                game.write("GAME OVER", False, align='center', font=('Courier', 60, 'normal'))
                game_over = True




        for sq in squares:
            if sq.distance(ball) < 50:
                blocks -= 1
                if ball.heading() == 45:
                    ball.setheading(315)
                else:
                    ball.setheading(225)
                sq.goto(-400,-400)
                # sq.reset()

        if blocks == 0:
            win = Turtle()
            win.color('white')
            win.goto(0,0)
            win.write("YOU WIN", False, align='center', font=('Courier', 60, 'normal'))
            game_over = True

    screen.exitonclick()




if __name__ == "__main__":
    run()