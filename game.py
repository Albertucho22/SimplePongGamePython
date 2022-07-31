import turtle as t

# Window screen
window = t.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(800, 600)

# Left paddle
leftPaddle = t.Turtle()
leftPaddle.speed(0)
leftPaddle.shape("square")
leftPaddle.color("white")
leftPaddle.shapesize(5, 1)
leftPaddle.penup()
leftPaddle.goto(-250, 0)

# Right paddle
rightPaddle = t.Turtle()
rightPaddle.speed(0)
rightPaddle.shape("square")
rightPaddle.color("white")
rightPaddle.shapesize(5, 1)
rightPaddle.penup()
rightPaddle.goto(250, 0)

# Ball
ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(0, 0)
ball.dx = 5
ball.dy = -5

# Initialize score
playerAScore = 0
playerBScore = 0

# Display score
score = t.Turtle()
score.speed(0)
score.color("blue")
score.penup()
score.goto(0, 250)
score.write("Left_player : {}    Right_player: {}".format(playerAScore, playerBScore), align="center", font=("Courier", 24, "normal"))

score.hideturtle()

# Move paddles
def paddleAUp():
    y = leftPaddle.ycor()
    y += 20
    leftPaddle.sety(y)

def paddleADown():
    y = leftPaddle.ycor()
    y -= 20
    leftPaddle.sety(y)

def paddleBUp():
    y = rightPaddle.ycor()
    y += 20
    rightPaddle.sety(y)

def paddleBDown():
    y = rightPaddle.ycor()
    y -= 20
    rightPaddle.sety(y)

# Keyboard bindings
window.listen()
window.onkeypress(paddleBUp, "Up")
window.onkeypress(paddleBDown, "Down")
window.onkeypress(paddleAUp, "w")
window.onkeypress(paddleADown, "s")

# Check borders
def upCollision():
    if(ball.ycor() > 300):
        ball.sety(300)
        ball.dy *= -1

def downCollision():
    if(ball.ycor() < -300):
        ball.sety(-300)
        ball.dy *= -1

# Players score
def checkScore(playerAScore, playerBScore):
    if(ball.xcor() > 400):
        ball.goto(0, 0)
        ball.dy *= -1
        playerAScore += 1
        score.clear()
        score.write("Left_player : {}    Right_player: {}".format(playerAScore, playerBScore), align="center", font=("Courier", 24, "normal"))
    
    if(ball.xcor() < -400):
        ball.goto(0, 0)
        ball.dy *= -1
        playerBScore += 1
        score.clear()
        score.write("Left_player : {}    Right_player: {}".format(playerAScore, playerBScore), align="center", font=("Courier", 24, "normal"))
    return playerAScore, playerBScore

# Paddle collision
def paddleCollision():
    if (ball.xcor() > 250 and ball.xcor() < 260) and (ball.ycor() < rightPaddle.ycor()+60 and ball.ycor() > rightPaddle.ycor()-60):
        ball.setx(250)
        ball.dx *= -1

    if (ball.xcor() < -250 and ball.xcor() > -260) and (ball.ycor() < leftPaddle.ycor()+60 and ball.ycor() > leftPaddle.ycor()-60):
        ball.setx(-250)
        ball.dx *= -1

# Main logic
while True:
    window.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    upCollision()
    downCollision()

    playerAScore, playerBScore = checkScore(playerAScore, playerBScore)
    paddleCollision()