import turtle
import random

t=turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
colors = ["red","orange","yellow","green","purple","blue"]

for i in range(100):
    t.color(random.choice(colors))
    t.forward(i*5)
    t. right(121)

turtle.done()
