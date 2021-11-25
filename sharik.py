import pygame as pg
from pygame.draw import *
from random import randint
import numpy as np

pg.init()

finished = False
screen_width = 1000
screen_height = 600
score = 0
FPS = 30
max_velocity = 5
min_death_time = 50
max_death_time = 180
min_radius = 15
max_radius = 85
screen = pg.display.set_mode((screen_width, screen_height))
clock = pg.time.Clock()
R = (255, 0, 0)
B = (0, 0, 255)
G = (0, 255, 0)
V = (199, 21, 133)
O = (255, 165, 0)
C = (0,0,0)
W = (255,255,255)
COLORS = [R, B, V, G, O, W, C]
ball_number = 13
ball_X = []
ball_Y = []
ball_R = []
ball_Color = []
ball_Vx = []
ball_Vy = []
ball_time = []
ball_death_time = []


def text(score):
    f1 = pg.font.SysFont('arial',65)
    text = f1.render(score, 1, R)
    screen.blit(text, (60,20))

for i in range(ball_number):
    ball_X.append(0)
    ball_Y.append(0)
    ball_Vx.append(0)
    ball_Vy.append(0)
    ball_R.append(0)
    ball_Color.append(0)
    ball_time.append(0)
    ball_death_time.append(0)

def new_ball(i):
    ball_X[i] = randint(int(screen_width * 0.1), int(screen_width * 0.9))
    ball_Y[i] = randint(int(screen_height * 0.1), int(screen_height * 0.9))
    ball_Vx[i] = randint(-max_velocity, max_velocity)
    ball_Vy[i] = randint(-max_velocity, max_velocity)
    ball_R[i] = randint(min_radius, max_radius)
    ball_Color[i] = COLORS[randint(0, 5)]
    ball_time[i] = 0
    ball_death_time[i] = randint(min_death_time, max_death_time)

for i in range(ball_number):
    new_ball(i)

while not finished:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            for i in range(ball_number):
                if (mouse_x - ball_X[i]) ** 2 + (mouse_y - ball_Y[i]) ** 2 <= ball_R[i] ** 2:
                    if i <= ball_number:
                        new_ball(i)
                    if i > ball_number:
                        new_ball(i)
                    if ball_R[i] <= max_radius and ball_R[i] >= max_radius * 0.5:
                        score += 1
                    if ball_R[i] < max_radius * 0.5 and ball_R[i] >= max_radius * 0.3:
                        score += 2
                    if ball_R[i] < max_radius * 0.3:
                        score += 4

    for i in range(ball_number):

        circle(screen, ball_Color[i], (ball_X[i], ball_Y[i]), ball_R[i])
        ball_time[i] += 1

        if ball_time[i] >= ball_death_time[i]:
            new_ball(i)

        if ball_X[i] > screen_width * 0.9:
            ball_Vx[i] = randint(-max_velocity, 0)
        if ball_X[i] < screen_width * 0.1:
            ball_Vx[i] = randint(0, max_velocity)
        if ball_Y[i] > screen_height * 0.9:
            ball_Vy[i] = randint(-max_velocity, 0)
        if ball_Y[i] < screen_height * 0.1:
            ball_Vy[i] = randint(0, max_velocity)

        ball_X[i] += ball_Vx[i]
        ball_Y[i] += ball_Vy[i]

    text(str(score))
    pg.display.update()
    screen.fill((100, 100, 100))

pg.quit()