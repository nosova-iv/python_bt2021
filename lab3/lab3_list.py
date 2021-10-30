import math
import turtle


diag_length = math.sqrt(50**2+50**2)
const_of_len_cifir=50
const_of_delta_x = 30

print('Введите комбинацию чисел')
input_c = input()

def number_zero(delta_x):
    turtle.pendown()
    turtle.forward(const_of_len_cifir)
    turtle.right(90)
    turtle.forward(2*const_of_len_cifir)
    turtle.right(90)
    turtle.forward(const_of_len_cifir)
    turtle.right(90)
    turtle.forward(2*const_of_len_cifir)
    turtle.right(90)
    turtle.penup()
    turtle.goto(delta_x, 0)
#one
def number_one(delta_x):
    turtle.shape('turtle')
    turtle.penup()
    turtle.right(90)
    turtle.forward(const_of_len_cifir)
    turtle.left(135)
    turtle.pendown()
    turtle.forward(diag_length)
    turtle.right(135)
    turtle.forward(100)
    turtle.penup()
    turtle.left(90)
    turtle.goto(delta_x,0)
    turtle.penup()
    turtle.goto(delta_x, 0)

#two
def number_two(delta_x):
    turtle.pendown()
    turtle.forward(const_of_len_cifir)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(45)
    turtle.forward(diag_length)
    turtle.left(135)
    turtle.forward(const_of_len_cifir)
    turtle.penup()
    turtle.goto(delta_x,0)

#three
def number_three(delta_x):
    turtle.pendown()
    turtle.forward(const_of_len_cifir)
    turtle.right(135)
    turtle.forward(diag_length)
    turtle.left(135)
    turtle.forward(const_of_len_cifir)
    turtle.right(135)
    turtle.forward(diag_length)
    turtle.left(135)
    turtle.penup()
    turtle.goto(delta_x,0)

def number_four(delta_x):
    turtle.pendown()
    turtle.right(90)
    turtle.forward(const_of_len_cifir)
    turtle.left(90)
    turtle.forward(const_of_len_cifir)
    turtle.left(90)
    turtle.forward(const_of_len_cifir)
    turtle.left(180)
    turtle.forward(2*const_of_len_cifir)
    turtle.left(90)
    turtle.penup()
    turtle.goto(delta_x, 0)

def number_five(delta_x):
   turtle.pendown()
   turtle.forward(const_of_len_cifir)
   turtle.left(180)
   turtle.forward(const_of_len_cifir)
   turtle.left(90)
   turtle.forward(const_of_len_cifir)
   turtle.left(90)
   turtle.forward(const_of_len_cifir)
   turtle.right(90)
   turtle.forward(const_of_len_cifir)
   turtle.right(90)
   turtle.forward(const_of_len_cifir)
   turtle.left(180)
   turtle.penup()
   turtle.goto(delta_x, 0)

def number_six(delta_x):
    turtle.pendown()
    turtle.forward(const_of_len_cifir)
    turtle.left(180)
    turtle.forward(const_of_len_cifir)
    turtle.left(90)
    turtle.forward(const_of_len_cifir)
    turtle.left(90)
    turtle.forward(const_of_len_cifir)
    turtle.right(90)
    turtle.forward(const_of_len_cifir)
    turtle.right(90)
    turtle.forward(const_of_len_cifir)
    turtle.right(90)
    turtle.forward(const_of_len_cifir)
    turtle.right(90)
    turtle.penup()
    turtle.goto(delta_x, 0)

def number_seven(delta_x):
    turtle.pendown()
    turtle.forward(const_of_len_cifir)
    turtle.right(135)
    turtle.forward(diag_length)
    turtle.left(45)
    turtle.forward(const_of_len_cifir)
    turtle.left(90)
    turtle.penup()
    turtle.goto(delta_x, 0)

def number_eight(delta_x):
    turtle.pendown()
    turtle.forward(const_of_len_cifir)
    turtle.right(90)
    turtle.forward(2*const_of_len_cifir)
    turtle.right(90)
    turtle.forward(const_of_len_cifir)
    turtle.right(90)
    turtle.forward(2*const_of_len_cifir)
    turtle.left(180)
    turtle.forward(const_of_len_cifir)
    turtle.left(90)
    turtle.forward(const_of_len_cifir)
    turtle.penup()
    turtle.goto(delta_x, 0)






list_of_numbers = []

try:
    for item in input_c:
        if int(item) == 0:
            list_of_numbers.append(number_zero)
        if int(item) == 1:
            list_of_numbers.append(number_one)
        if int(item) == 2:
            list_of_numbers.append(number_two)
        if int(item) == 3:
            list_of_numbers.append(number_three)
        if int(item) == 4:
            list_of_numbers.append(number_four)
        if int(item) == 5:
            list_of_numbers.append(number_five)
        if int(item) == 6:
            list_of_numbers.append(number_six)
        if int(item) == 7:
            list_of_numbers.append(number_seven)
        if int(item) == 8:
            list_of_numbers.append(number_eight)

except ValueError:
        print('Вы ввели некоректную строку')

alpha_x=0

for i in range(len(list_of_numbers)):
    alpha_x = alpha_x + const_of_delta_x + const_of_len_cifir
    list_of_numbers[i](alpha_x)


x = input()

