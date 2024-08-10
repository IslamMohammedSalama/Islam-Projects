import turtle


score_1 = 0
score_2 = 0

wintow = turtle.Screen()
wintow.bgcolor("black")
wintow.title("PING PONG BY ISLAM")
wintow.setup(height=600, width=800)
wintow.tracer(0)


player_1 = turtle.Turtle()
player_1.speed(0)
player_1.shape("square")
player_1.shapesize(stretch_wid=5, stretch_len=1)
player_1.color("#00ff00")
player_1.penup()
player_1.goto(350, 0)


player_2 = turtle.Turtle()
player_2.speed(0)
player_2.shape("square")
player_2.shapesize(stretch_wid=5, stretch_len=1)
player_2.color("red")
player_2.penup()
player_2.goto(-350, 0)


ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25
ball.dy = 0.25


text = turtle.Turtle()
text.speed()
text.penup()
text.hideturtle()
text.color("white")
text.goto(0,260)
text.write("player 1 : {} player 2 : {}".format(score_1,score_2),align="Center",font=("arial ",30,"bold"))


def player_1_up():
    y = player_1.ycor()
    y += 10
    player_1.sety(y)

def player_1_down():
    y = player_1.ycor()
    y -= 10
    player_1.sety(y)

def player_2_up():
    y = player_2.ycor()
    y += 10
    player_2.sety(y)

def player_2_down():
    y = player_2.ycor()
    y -= 10
    player_2.sety(y)


wintow.listen()
wintow.onkeypress(player_1_up, "Up")
wintow.onkeypress(player_1_down, "Down")
wintow.onkeypress(player_2_up, "w")
wintow.onkeypress(player_2_down, "s")


while True:
    wintow.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if player_1.ycor() == 290 : 

        player_1.sety(290)

    elif player_1.ycor() == -290 :

        player_1.sety(-290)

    elif player_2.ycor() == 290 : 

        player_2.sety(290)

    elif player_2.ycor() == -290 :
        player_2.sety(-290)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1


    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1


    if ball.xcor() > 390:
        ball.color("#ff0000")
        ball.setx(390)
        ball.dx *= -1
        score_1 += 1
        text.clear()
        text.write("player 1 : {} player 2 : {}".format(score_1,score_2),align="Center",font=("Courier",30,"normal"))
    
    
    if ball.xcor() < -390:
        ball.color("#00ff00")
        ball.setx(-390)
        ball.dx *= -1
        score_2 += 1
        text.clear()
        text.write("player 1 : {} player 2 : {}".format(score_1,score_2),align="Center",font=("Courier",30,"normal"))
    
    
    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() > (player_1.ycor()-60) and ball.ycor() < (player_1.ycor()+60):
        ball.setx(-340)
        ball.dx *= -1

    # collision with player 2
    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() > (player_2.ycor()-60) and ball.ycor() < (player_2.ycor()+60):
        ball.setx(340)
        ball.dx *= -1
