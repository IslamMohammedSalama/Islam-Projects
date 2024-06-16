import math
import random
import turtle
import pygame

pygame.mixer.init()

# Setup Screen
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.bgpic("bg.png")
wn.setup(width=700, height=560)
wn.tracer(2)

score = 0

# ============= Draw Shapes ==============
# Draw Borders
border = turtle.Turtle()
border.speed(0)  # Draw Animation (0: fastest)
border.penup()
border.setposition(-300, -230)
border.pendown()
border.pensize(5)
border.color("red")
for i in (700, 560, 700, 560):
    border.forward(i - 100)
    border.left(90)
border.hideturtle()

# Draw The Score
border.penup()
border.setposition(-75, 235)
border.color("white")
border.write(f"Score: {score}", align="left", font=("Courier", 22, "bold"))

# Create Player
player = turtle.Turtle()
player.speed(0)
player.penup()
player.shape("triangle")
player.color("white")

player_speed = 1


# Create List of Goals
goals = []
goals_count = 6
for i in range(goals_count):
    # Create One Goal
    goals.append(turtle.Turtle())
    goals[i].speed(0)
    goals[i].penup()
    goals[i].shape("circle")
    goals[i].color(random.choice(["yellow", "cyan" , "red", "purple", "blue","green", "orange", "white", "black"]))
    goals[i].setposition(random.randint(-300, 300), random.randint(-230, 230))

goal_speed = 2


# =========== Game Functions ===========
def turn_left():
    player.left(30)


def turn_right():
    player.right(30)


def increase_speed():
    global player_speed
    player_speed += 1


def decrease_speed():
    global player_speed
    if player_speed < 1:
        return
    player_speed -= 1


def isCollision(t1, t2):
    d = math.sqrt(
        math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2)
    )
    if d < 20:
        return True
    else:
        return False


# =========== Key Bindings =============
wn.listen()
wn.onkey(turn_left, "Left")
wn.onkey(turn_right, "Right")
wn.onkey(increase_speed, "Up")
wn.onkey(decrease_speed, "Down")


# ============= Game Loop ==============
while True:
    # Move Player
    player.forward(player_speed)

    # Player & Boundary Collision
    if player.xcor() > 300 or player.xcor() < -300:
        player.right(180)
    if player.ycor() > 230 or player.ycor() < -230:
        player.right(180)

    # Move Goal
    for goal in goals:
        goal.forward(goal_speed)

        # Goal & Boundary Collision
        if goal.xcor() > 300 or goal.xcor() < -300:
            goal.right(180)
        if goal.ycor() > 230 or goal.ycor() < -230:
            goal.right(180)

        # Player & Ball Collision Detection
        if isCollision(player, goal):
            goal.setposition(random.randint(-300, 300), random.randint(-230, 230))
            goal.right(random.randint(0, 360))
            # Update Score
            score += 1
            border.undo()
            border.write(f"Score: {score}", align="left", font=("Courier", 22, "bold"))
            # play Sound
            # winsound.PlaySound("collision.wav", winsound.SND_ASYNC)
            # pygame.mixer.Sound("collision.wav").play(
                
            # )

# Don't close the window automatically
wn.mainloop()
