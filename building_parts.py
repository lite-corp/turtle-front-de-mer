"""
Program by Alexis Rossfelder
This program is available under the terms of the GNU General Public License v3.0

https://www.gnu.org/licenses/gpl-3.0.en.html

Ce document contient les fonctions permettant la construction de parties de maisons
"""

from random import randint
from turtle import (backward, begin_fill, circle, end_fill, fillcolor, forward,
                    left, pendown, pensize, penup, right, setheading)
from typing import Tuple

from basic_shapes import SIZE, randcolor, rectangle


def floor(color: Tuple[float, float, float]=None, with_door:bool = False)-> None:

    if color : fillcolor(color)
    if color : begin_fill()

    door_i = randint(0, 2)
    pendown()
    rectangle(140, 60)
    penup()
    if color : end_fill()
    for i in range(3):
        if i == door_i and with_door:
            door()
        else:
            window(with_door)


def door()-> None:
    setheading(0)
    forward(SIZE * 8)
    pendown()
    
    left(90)
    fillcolor(randcolor())
    begin_fill()
    forward(SIZE * 30)
    if randint(0, 1):
        left(180)
        circle(SIZE * 15, -180)
        left(180)
    else:
        forward(SIZE * 20)
        
        right(90)
        forward(SIZE * 30)
        
        right(90)
        forward(SIZE * 20)
    forward(SIZE * 30)
    end_fill()
    
    left(90)
    penup()
    forward(SIZE * 8)

def window(avoid_large_windows = False)-> None:
    if randint(0, 1) or avoid_large_windows:
        penup()
        forward(SIZE * 10)
        left(90)
        forward(SIZE * 20)
        pendown()
        fillcolor('white')
        begin_fill()
        rectangle(30, 30)
        end_fill()
        penup()
        right(90)
        forward(SIZE * 20)
        left(90)
        forward(SIZE * 37)
    else:
        penup()
        forward(SIZE * 10)
        left(90)
        forward(SIZE * 5)
        fillcolor('white')
        begin_fill()
        pendown()
        rectangle(30, 50)
        right(90)
        forward(SIZE * 3)
        end_fill()
        pendown()
        for _ in range(10):
            rectangle(3, 20)
            forward(SIZE * 3)
        penup()
        right(90)
        forward(SIZE * 2)
        left(90)
        forward(SIZE * 7)

def roof()-> None:
    if randint(0, 1):
        setheading(0)
        pensize(5)
        backward(SIZE * 5)
        pendown()
        forward(SIZE * 150)
        penup()
        backward(SIZE * 145)
        pensize(1)
    else:
        setheading(0)
        pensize(2)
        backward(SIZE * 14)
        pendown()
        fillcolor((0.3, 0.3, 0.5))
        begin_fill()
        forward(SIZE * (14 + 140/2))
        left(90)
        penup()
        forward(SIZE * 30)
        end_fill()
        begin_fill()
        backward(SIZE * 30)
        pendown()
        right(90)
        forward(SIZE * (140/2 + 14))
        end_fill()
        penup()
        backward(SIZE * (140 + 14))

# Lance la génération principale depuis n'importe quel fichier
if __name__ == '__main__':
    import main
    main.build_scene()
