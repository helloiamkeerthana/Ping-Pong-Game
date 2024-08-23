import turtle
import os

# Set up the screen
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("light blue")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A (AI-controlled)
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B (Player-controlled)
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = 0.15

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Functions for Paddle B (Player-controlled)
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:  # Prevent paddle from going off screen
        y += 30
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -240:  # Prevent paddle from going off screen
        y -= 30
    paddle_b.sety(y)

# Keyboard bindings for Paddle B
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Ball and top/bottom border collision
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Ball and left/right border collision (score update)
    if ball.xcor() > 390:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -390:
         score_b += 1
         pen.clear()
         pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
         ball.goto(0, 0)
         ball.dx *= -1

    # AI for Paddle A
    if paddle_a.ycor() < ball.ycor() and abs(paddle_a.ycor() - ball.ycor()) > 10:
        paddle_a.sety(paddle_a.ycor() + 20)
    elif paddle_a.ycor() > ball.ycor() and abs(paddle_a.ycor() - ball.ycor()) > 10:
        paddle_a.sety(paddle_a.ycor() - 20)

    # Paddle and ball collision detection
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")
    
    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")