from turtle import Screen, Turtle
from space import Space
from bullets import Bullet
from alienbullet import AlienBullet
from barriers import Barriers,barriers_list
import random
import time

# ---------------- SCREEN ----------------
screen = Screen()

screen.tracer(0)

# ---------------- OBJECTS ----------------
space = Space()
bullet = Bullet()

alien_list = []
alien_bullets = []

barriers = Barriers()


#___________Making Line_______________
def draw_bottom_line():
    line = Turtle()
    line.hideturtle()
    line.penup()
    line.pensize(3)
    line.color("black")
    line.goto(-250, -250)   # left side
    line.pendown()
    line.goto(250, -250)    # right side



# ---------------- GAME STATE ----------------
game_is_on = True
alien_direction = 1

# ---------------- ALIENS ----------------
def make_aliens():
    start_x = -200
    start_y = 360

    rows = 5
    cols = 12

    for row in range(rows):
        for col in range(cols):
            alien = Turtle()
            alien.shape("circle")
            alien.penup()

            x = start_x + col * 30
            y = start_y - row * 30

            alien.goto(x, y)
            alien_list.append(alien)


# ---------------- ALIEN MOVE ----------------
def move_aliens():
    global alien_direction

    move_down = False

    for alien in alien_list:
        alien.setx(alien.xcor() + alien_direction * 2)

        if alien.xcor() > 260 or alien.xcor() < -260:
            move_down = True

    if move_down:
        alien_direction *= -1
        for alien in alien_list:
            alien.sety(alien.ycor() - 20)

    if game_is_on:
        screen.ontimer(move_aliens, 200)


# ---------------- BOTTOM ALIENS ----------------
def get_bottom_aliens():
    bottom = []

    for alien in alien_list:
        same_col = [a for a in alien_list if a.xcor() == alien.xcor()]
        lowest = min(same_col, key=lambda a: a.ycor())
        bottom.append(lowest)

    return list(set(bottom))


# ---------------- ALIEN SHOOT ----------------
last_shot = 0

def alien_shoot():
    global last_shot

    if time.time() - last_shot > 2:
        bottom = get_bottom_aliens()

        if bottom:
            shooter = random.choice(bottom)
            alien_bullets.append(
                AlienBullet(shooter.xcor(), shooter.ycor())
            )

        last_shot = time.time()


# ---------------- GAME OVER ----------------
def game_over():
    text = Turtle()
    text.hideturtle()
    text.color("red")
    text.penup()
    text.goto(0, 0)
    text.write("GAME OVER", align="center", font=("Arial", 40, "bold"))


# ---------------- SETUP ----------------
make_aliens()
move_aliens()
draw_bottom_line()

screen.listen()
screen.onkey(space.go_left, "Left")
screen.onkey(space.go_right, "Right")
screen.onkey(lambda: bullet.fire(space.xcor(), space.ycor()), "space")


# ---------------- GAME LOOP ----------------
while game_is_on:
    screen.update()
    time.sleep(0.02)

    # ---------------- PLAYER BULLET ----------------
    bullet.move()

    # Alien touches Barrier
    for alien in alien_list:
        for barrier in barriers_list[:]:
            if alien.distance(barrier) < 20:
                barrier.hideturtle()
                barriers_list.remove(barrier)


    # bullet vs aliens
    for alien in alien_list[:]:
        if bullet.distance(alien) < 25:
            alien.hideturtle()
            alien_list.remove(alien)

            bullet.hideturtle()
            bullet.state = "ready"
            bullet.goto(0, -250)
            break

        # check if alien touches space
        if alien.distance(space)< 15:
            game_over()
            game_is_on = False

    # WIN CHECK
    if not alien_list:
        win = Turtle()
        win.hideturtle()
        win.color("green")
        win.penup()
        win.goto(0, 0)
        win.write("You win!", align="center", font=("Arial", 60, "bold"))
        game_is_on = False


    # ---------------- ALIEN BULLETS ----------------
    for b in alien_bullets[:]:
        b.move()

        # bullet vs barriers
        for barrier in barriers_list[:]:
            if b.distance(barrier) < 25:
                barrier.hideturtle()
                barriers_list.remove(barrier)

                b.hideturtle()
                alien_bullets.remove(b)
                break

        # bullet vs player
        if b.distance(space) < 10:
            game_over()
            game_is_on = False
            break

        # remove off screen
        if b.ycor() < -350:
            b.hideturtle()
            alien_bullets.remove(b)

        #check two bullets collision made situation.
        if bullet.distance(b) <10:
            b.hideturtle()
            alien_bullets.remove(b)

            bullet.hideturtle()
            bullet.state = "ready"
            bullet.goto(0, -250)




    # ---------------- ALIEN SHOOT ----------------
    alien_shoot()


screen.exitonclick()