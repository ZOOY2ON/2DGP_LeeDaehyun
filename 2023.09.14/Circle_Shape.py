import turtle

shape = input("Enter Shape")

if shape == 'circle' :
    turtle.reset()
    turtle.circle(50)
elif shape == 'triangle' :
    turtle.reset()
    turtle.forward(50); turtle.left(120)
    turtle.forward(50); turtle.left(50)
    turtle.forward(50)
elif shape == 'square' :
    turtle.reset()
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
else:
    print('Unknown shape')
