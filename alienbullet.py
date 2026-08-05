import random
from turtle import Turtle

alien_bullets = []

class AlienBullet(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.hideturtle()
        self.shape("square")

        self.shapesize(0.2, 0.8)
        self.color("red")

        self.penup()

        self.goto(x, y)
        self.setheading(270)  # down
        self.showturtle()

    def move(self):
      new_y = self.ycor() - 5
      self.sety(new_y)
