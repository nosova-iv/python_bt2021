import turtle
turtle.shape("circle")
turtle.goto(300, 0)
turtle.goto(-300, 0)
turtle.speed(2)
Vx = 3
a = 1
Vy = 17
y = 0
x = -300

for i in range(500):
    Vy -= a*1.5
    if y + Vy < 0:
        y = Vy
        Vy = -Vy
    turtle.goto(x + Vx, y + Vy)
    x = turtle.xcor()
    y = turtle.ycor()
