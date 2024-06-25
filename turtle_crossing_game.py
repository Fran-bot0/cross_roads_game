### Turtle Crossing Game ###

from turtle import Turtle, Screen
from time import sleep
from random import randint, choice

TURTLE_MOVING_SPEED = 10
CARS_MOVING_SPEED = 10
INFREQUENCY = 2
CAR_SPEED_INCREASE = 5

screen = Screen()
screen.setup(width=600, height=600)
screen.title("TURTLE CROSSING")
screen.tracer(0)

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("green")
        self.goto(0, -280)
        self.setheading(90)

    def move_forward(self):
        self.setheading(90)
        self.forward(TURTLE_MOVING_SPEED)

    def move_right(self):
        self.setheading(0)
        self.forward(TURTLE_MOVING_SPEED)
        self.setheading(90)

    def move_left(self):
        self.setheading(180)
        self.forward(TURTLE_MOVING_SPEED)
        self.setheading(90)

    def move_backwards(self):
        self.setheading(90)
        self.backward(TURTLE_MOVING_SPEED)


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(choice(("black", "yellow", "red", "purple", "orange", "green", "blue")))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(180)
        self.goto(300, (20*randint(-14, 14)))

    def move(self):
        self.forward(CARS_MOVING_SPEED)



class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-230, 260)
        self.current_level = 0
        self.is_level()

    def is_level(self):
        self.clear()
        self.write(arg=f"Level: {self.current_level}", move=False, align="center", font=("Courier New", 16, "bold"))
        self.current_level += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", move=False, align="center", font=("Courier New", 28, "bold"))


player = Player()
level = Level()

screen.listen()
screen.onkey(fun=player.move_forward, key="Up")
screen.onkey(fun=player.move_right, key="Right")
screen.onkey(fun=player.move_left, key="Left")
screen.onkey(fun=player.move_backwards, key="Down")

cars = []
game_on = True
while game_on:
    screen.update()
    sleep(0.1)

    # Higher values of INFREQUENCY spawn less cars.
    if randint(0, INFREQUENCY) == 0:
        car = Car()
        cars.append(car)

    # Moving the cars and detecting collisions.
    for vehicle in cars:
        if (player.xcor() >= vehicle.xcor()-30 and player.xcor() <= vehicle.xcor()+20) and (player.ycor()+10 >= vehicle.ycor()-10 and player.ycor() <= vehicle.ycor()+10) and player.distance(vehicle.position()) <= 44:
            level.game_over()
            game_on = False
        vehicle.move()

    # If the player reaches the other side of the scree, continue to next level.
    if player.ycor() >= 280:
        player.goto(0, -280)
        CARS_MOVING_SPEED += CAR_SPEED_INCREASE
        level.is_level()

    # Make it impossible for the player to leave the bounds of the gaming screen.
    if player.ycor() <= -275:
        player.sety(-280)
    if player.xcor() <= -275:
        player.setx(-280)
    if player.xcor() >= 285:
        player.setx(280)


screen.exitonclick()
