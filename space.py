from turtle import Turtle,Screen
screen  = Screen()

class Space(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("triangle")
        self.setheading(90)
        self.penup()
        self.backward(220)


    def go_right(self):
        self.penup()
        self.setx(self.xcor()+ 20)

    def go_left(self):
        self.penup()
        self.setx(self.xcor()-20)