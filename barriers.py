from turtle import Turtle

barriers_list = []

START_X = -250
START_Y = 50

ROWS = 4
COLUMN = 15

class Barriers:
    def __init__(self):
        self.make_barrier()

    def make_barrier(self):
        for row in range(ROWS):
            for col in range(COLUMN):

                barrier = Turtle()
                barrier.shape("turtle")
                barrier.shapesize(stretch_wid=0.8,stretch_len=0.8)
                barrier.penup()

                x = START_X + col * 30
                y = START_Y - row * 30

                barrier.goto(x, y)

                barriers_list.append(barrier)
