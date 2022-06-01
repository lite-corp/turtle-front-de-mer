"""
Program by Alexis Rossfelder
This program is available under the terms of the GNU General Public License v3.0

https://www.gnu.org/licenses/gpl-3.0.en.html


Ce fichier contient des fonctions essentielles ne pouvant être rattachées à un élément en particulier
"""

from random import randint
from turtle import forward, left, setheading, speed
from typing import Tuple

SIZE = 1
speed(0)
def randcolor() -> Tuple[float, float, float]:
    return (
        0.5 + (randint(0, 128) / 256),
        0.5 + (randint(0, 128) / 256),
        0.5 + (randint(0, 128) / 256)            
    )

def randomBlue() -> Tuple[float, float, float]:
    c = randint(0,128) / 256
    return (0.5 + c, 0.5 +c, 1.0)

def rectangle(width: float, height: float):
    setheading(0)
    for _ in range(2):
        forward(SIZE * width)
        left(90)
        forward(SIZE * height)
        left(90)


# Lance la génération principale depuis n'importe quel fichier
if __name__ == '__main__':
    import main
    main.build_scene()
