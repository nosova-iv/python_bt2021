import turtle
turtle.shape('turtle')
print("Введите количество вершин звезды")
n = int(input())


def star(n):
    for i in range(n):
        turtle.forward(100)
        turtle.left(180 - (180/n))

star(n)
turtle.mainloop()

