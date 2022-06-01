#!/usr/bin/python3
"""
Program by Alexis Rossfelder
This program is available under the terms of the GNU General Public License v3.0

https://www.gnu.org/licenses/gpl-3.0.en.html


Ce programme permet de dessiner une rue face à la mer en utilisant turtle.py
"""

from random import randint, seed
import time
from turtle import (back, forward, hideturtle, left, mainloop, pencolor,
                    pendown, pensize, penup, right, setheading, tracer)

from basic_shapes import SIZE, randcolor
from building_parts import floor, roof
from landscape import draw_background, starfish, sun, tree, wave


def building(height: int):
    color = randcolor()
    floor(color, True)
    left(90)
    forward(SIZE * 60)
    setheading(0)
    back(SIZE * 140)
    for _ in range(height-1):
        floor(color, False)
        setheading(0)
        back(SIZE * 141)
        left(90)
        forward(SIZE * 60)
    roof()
    right(90)
    penup()
    forward(SIZE * height * 60)

def street(lenght=180):
    setheading(0)
    pencolor((0.5, 0.5, 0.5))
    pensize(5)
    pendown()
    if lenght == 180: back(SIZE * 40)
    if lenght == 180: forward(SIZE * 40)
    forward(SIZE * lenght)
    right(90)
    penup()
    forward(SIZE * 10)
    right(90)
    pendown()
    pensize(4)
    forward(SIZE * lenght)
    back(SIZE * lenght)
    penup()
    right(90)
    forward(SIZE * 10)
    right(90)
    pensize(1)
    pencolor('black')
    

def build_scene(number_of_buildings: int = 7, number_of_trees: int = 2, number_of_starfishes: int = 20, number_of_waves: int = 30, generation_seed = 0):
    """
    Ceci est la fonction principale, elle permet d'afficher la rue.

    Args:
        number_of_buildings:    Nombre de bâtiments.
        number_of_trees:        Nombre d'arbres avant et après les bâtiments.
        number_of_starfishes:   Nombre d'étoiles de mer sur la plage
        number_of_waves:        Nombre de vagues dans la mer
        generation_seed:        Graine pour le RNG

    Returns:
        Cette fonction de retourne rien.

    Nice seeds : 
    00001   : Rêve bleu
    63539   : Flat roof corporation
    43762   : Maison de Mme Hervieu
    94538   : Joyeux front de mer
    69686   : Seul contre tous
    35348   : Tall bois
    54321   : Smol bois

    """
    time.sleep(10)

    penup()
    if generation_seed: seed(generation_seed)

    draw_background()

    back(SIZE * (number_of_buildings * 180 + number_of_trees * 100 + 200) / 2)

    right(90)
    forward(SIZE * 105)
    street(60)
    for _ in range(number_of_trees):
        tree(22, 10)
        street(100)

    for _ in range(number_of_buildings):
        #tree()
        street()
    for _ in range(number_of_trees):
        tree(22, 10)
        street(100)
    penup()
    back(SIZE * (number_of_trees * 100 + number_of_buildings * 180 + 40))
    for _ in range(number_of_buildings):
        building(randint(1, 5))
        street()

    for _ in range(number_of_starfishes):
        starfish(
            randint(
                -SIZE * (number_of_buildings * 180 + number_of_trees * 100 + 200) / 2,
                SIZE * (number_of_buildings * 180 + number_of_trees * 100 + 200) / 2
                ), 
                randint(-230, -140))
    for _ in range(number_of_waves):
        wave(
            randint(
                -SIZE * (number_of_buildings * 180 + number_of_trees * 100 + 200) / 2,
                SIZE * (number_of_buildings * 180 + number_of_trees * 100 + 200) / 2
                ), 
                randint(-600, -250))
    
    sun()

    hideturtle()
    mainloop()

if __name__ == '__main__':
    print(__doc__)
        
    build_scene(7, 2, 20, 30, 94538)
