from turtle import Turtle,Screen
screen  = Screen()

class Bullet(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.shapesize(stretch_wid=0.2, stretch_len=0.8)
        self.setheading(90)
        self.penup()
        self.hideturtle()
        self.state = "ready"  # ready / fire

    def fire(self, x, y):
        if self.state == "ready":
            self.state = "fire"
            self.goto(x, y + 20)
            self.showturtle()

    def move(self):
        if self.state == "fire":
            self.sety(self.ycor() + 20)

            if self.ycor() > 300:
                self.hideturtle()
                self.state = "ready"

    def reset_game(self):
        self.hideturtle()
        self.state = "ready"
        self.goto(0, -250)