# Simple Pong

import turtle

# Window setup
wn = turtle.Screen()
wn.title("Pong by Banut Dragos")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A setup
paddle_a = turtle.Turtle()
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.speed(0)
paddle_a.penup()
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.goto(-350, 0)

# Paddle B setup
paddle_b = turtle.Turtle()
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.speed(0)
paddle_b.penup()
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.goto(350, 0)

# Ball setup
ball = turtle.Turtle()
ball.shape("square")
ball.color("white")
ball.speed(0)
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1



# Function
def paddle_a_up():
    paddle_a.sety(paddle_a.ycor() + 20)

def paddle_a_down():
    paddle_a.sety(paddle_a.ycor() - 20)

def paddle_b_up():
    paddle_b.sety(paddle_b.ycor() + 20)

def paddle_b_down():
    paddle_b.sety(paddle_b.ycor() - 20)


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(paddle_b_up, "Up")


# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1