"""
Program by Alexis Rossfelder
This program is available under the terms of the GNU General Public License v3.0

https://www.gnu.org/licenses/gpl-3.0.en.html

Ce fichier contient les fonctions nécessaires à la contruction des éléments naturels 
"""

from random import randint
from turtle import (back, begin_fill, circle, end_fill, fillcolor, forward,
                    goto, left, pencolor, pendown, pensize, penup, right,
                    setheading, speed, mainloop)
import time

from basic_shapes import SIZE, randomBlue, rectangle


def sun():
    goto(SIZE * -600, SIZE * 300)
    fillcolor('yellow')
    begin_fill()
    circle(50)
    end_fill()

def tree(init_size=22, end_threshold=8):
    pencolor("#966F33")
    pendown()
    setheading(90)
    pensize(3)
    draw_branch(init_size, end_threshold)
    fillcolor("#966F33")
    penup()
    	

def draw_branch(len, end_threshold):
    #time.sleep(0.1)
    if (len > end_threshold):
        pensize(len/4)
        pencolor("#966F33")
        forward(len)
        right(25) 
        draw_branch(len - randint(1,5), end_threshold)
        left(50)
        draw_branch(len - randint(1,5), end_threshold)
        right(25)
        back(len)
    else:
        fillcolor('#42692F')
        begin_fill()
        penup()
        circle(15)
        pendown()
        end_fill()

def draw_background(infinity = 1_000):
    penup()
    goto(-infinity, SIZE * -103)
    fillcolor('#cdf9ff')
    begin_fill()
    rectangle(infinity*2, infinity)
    end_fill()

    goto(-infinity, SIZE * -120)
    fillcolor((0.5 ,0.5 ,0.5))
    begin_fill()
    rectangle(infinity*2, 17)
    end_fill()

    goto(-infinity, SIZE * -240)
    fillcolor('#d8caae')
    begin_fill()
    rectangle(infinity*2, 120)
    end_fill()

    goto(-infinity, -infinity - 240)
    fillcolor('#628ca6')
    begin_fill()
    rectangle(infinity*2, infinity)
    end_fill()
    goto(0, 0)

def starfish(posX, posY):
    penup()
    goto(posX, posY)
    fillcolor('#ea5924') # Benjamin Moore Festive Orange
    begin_fill()
    for _ in range(5):
        forward(SIZE * 10)
        right(144)
    end_fill()



def wave(posX, posY, amp = 10):
    penup()
    goto(posX, posY)
    setheading(0)
    pencolor(randomBlue())
    pendown()
    right(amp * 2)
    pensize(2)

    for _ in range(amp):
        forward(4)
        left(4)
    for _ in range(amp):
        forward(4)
        right(4)
    penup()

    
# Lance la génération principale depuis n'importe quel fichier
if __name__ == '__main__':
    speed(1)
    tree()
    mainloop()
