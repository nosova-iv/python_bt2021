import turtle

turtle.speed(0)

def polygone (n, lenght):
    for _ in range(n):
        turtle.forward(lenght)
        turtle.left(360//n)


turtle.penup()
turtle.forward(7)
for i in range(3, 12):
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()
    turtle.left(90 + 180/i)
    polygone(i, 15 + 10*i)
    turtle.right(90 + 180/i)



turtle.mainloop()


