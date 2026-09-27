from turtle import *

speed("fastest")

max_sides = 20
width = 1000

for sides in range(3, max_sides):
    for _j in range(0, sides):
        forward(width/sides)
        right(360/sides)
    left(90)

mainloop()