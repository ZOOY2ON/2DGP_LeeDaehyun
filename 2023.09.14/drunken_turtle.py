import turtle
import random

turtle.shape('turtle')

while(True):
    a = random.randint(10, 360)
    b = random.randint( 100, 200)

    turtle.setheading(a)
    turtle.forward(b)
    turtle.stamp()
