# Simple Pong

import turtle

# Window setup
wn = turtle.Screen()
wn.title("Pong by Banut Dragos")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

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
# Speed control
ball.dx = 0.2
ball.dy = 0.2

# Pen (for score)
pen = turtle.Turtle()
pen.penup()
pen.color('white')
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 | Player B: 0", align="center", font=("Courier", 20, "normal"))



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

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a +=1
        pen.clear()
        pen.write(f"Player A: {score_a} | Player B: {score_b}", align="center", font=("Courier", 20, "normal"))

    elif ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b +=1
        pen.clear()
        pen.write(f"Player A: {score_a} | Player B: {score_b}", align="center", font=("Courier", 20, "normal"))

    # Paddle and ball collision
    if ball.xcor() > 330 and ball.xcor() < 333 and ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() - 60:
        ball.setx(330)
        ball.dx *= -1
    if ball.xcor() < -330 and ball.xcor() > -333 and ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() - 60:
        ball.setx(-330)
        ball.dx *= -1
