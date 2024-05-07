import turtle , time , random 

def goup():

    if snake.direction != 'down':

        snake.direction = 'up'

def godown():

    if snake.direction != 'up':

        snake.direction = 'down'

def goright():

    if snake.direction != 'left':

        snake.direction = 'right'

def goleft():

    if snake.direction != 'right':

        snake.direction = 'left'

def go():

    if snake.direction == 'down' :

        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == 'up' :

        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == 'left' :

        x = snake.xcor()
        snake.setx(x - 20)

    if snake.direction == 'right' :

        x = snake.xcor()
        snake.setx(x + 20)

def g_o():

    pen2 = turtle.Turtle()
    pen2.write('GAME OVER !!!',align="Center",font=("arial ",50,"bold"))
    pen2.color('red')
    pen2.speed(0)
    pen2.hideturtle()
    pen2.penup()
    pen2.goto(0, 0)
    time.sleep(2.5)
    pen2.clear()

score = 0
higth_score = 0
speed = 0.1

root = turtle.Screen()
root.bgcolor("black")
root.title("SNACKE GAME BY ISLAM")
root.setup(height=800, width=800)
root.cv._rootwindow.resizable(False,False)

root.tracer(0)

snake = turtle.Turtle()
snake.speed(3)
snake.shape("square")
snake.shapesize(stretch_wid=1, stretch_len=1)
snake.color("white")
snake.penup()
snake.goto(0, 0)
snake.direction = 'stop'


color = random.choice(['red','blue','green','yellow'])
shape = random.choice(['circle','square','triangle','turtle'])
x = random.randint( -270, 270)
y = random.randint( -270, 270)
food = turtle.Turtle()
food.speed(0)
food.shape(shape)
food.shapesize(stretch_wid=1, stretch_len=1)
food.color(color)
food.penup()
food.goto(x, y)

pen = turtle.Turtle()
pen.color('white')
pen.speed(0)
pen.hideturtle()
pen.penup()
pen.goto(0, 350)
pen.write(f'Score : {score}     higth_score : {higth_score}',align="Center",font=("arial ",20,"bold"))

root.listen()

root.onkeypress(goup,'Up')
root.onkeypress(godown,'Down')
root.onkeypress(goright,'Right')
root.onkeypress(goleft,'Left')

sgma = []

while True :

    root.update()
    if (
        snake.xcor() > 360 or
        snake.xcor() < -360 or
        snake.ycor() > 360 or
        snake.ycor() < -360 
    ):
        
        # g_o()
        snake.goto(x=0,y=0)
        snake.direction = 'stop'
        for sgm in sgma :

            sgm.goto(x=1000,y=1000)

        sgma.clear()
        color = random.choice(['red','blue','green','yellow'])
        shape = random.choice(['circle','square','triangle','turtle'])
        food.shape(shape)
        food.color(color)
        score = 0
        speed = 0.1
        pen.clear()
        pen.write(f'Score : {score}     higth_score : {higth_score}',align="Center",font=("arial ",20,"bold"))

    if snake.distance(food) < 20 :

        x = random.randint( -270, 270)
        y = random.randint( -270, 270)
        food.goto(x,y)
        new_sgm = turtle.Turtle()
        new_sgm.speed(0)
        new_sgm.shape("square")
        new_sgm.shapesize(stretch_wid=1, stretch_len=1)
        new_sgm.color("orange")
        new_sgm.penup()
        sgma.append(new_sgm)
        speed -= 0.001
        if len(sgma) < 5 :

            score += 10
        elif len(sgma) < 5 :

            score += 20
        elif len(sgma) < 5 :

            score += 30

        else :

            score += 10

        if score > higth_score :

            higth_score = score 
            pen.clear()
            pen.write(f'Score : {score}     higth_score : {higth_score}',align="Center",font=("arial ",20,"bold"))
    
    for i in range(len(sgma)- 1 , 0 , -1) :

        x = sgma[i - 1 ].xcor()
        y = sgma[i - 1 ].ycor()
        sgma[i].goto(x, y)

    if len(sgma) > 0 :

        x= snake.xcor()
        y= snake.ycor()
        sgma[0].goto(x, y)
    go()
    for sgm in sgma :

        if snake.distance(sgm) < 20 :
            # g_o()
            snake.goto(x=0,y=0)
            snake.direction = 'stop'
            for sgm in sgma :

                sgm.goto(x=1000,y=1000)

            sgma.clear()
            color = random.choice(['red','blue','green','yellow'])
            shape = random.choice(['circle','square','triangle','turtle'])
            food.shape(shape)
            food.color(color)
            score = 0
            speed = 0.1
            pen.clear()
            pen.write(f'Score : {score}     higth_score : {higth_score}',align="Center",font=("arial ",20,"bold"))
    time.sleep(speed)