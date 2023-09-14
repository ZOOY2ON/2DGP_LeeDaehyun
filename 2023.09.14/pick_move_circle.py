import turtle

def draw_circle (x, y, r):
    turtle.penup()
    turtle.goto(x,y)
    turtle.stamp()
    turtle.goto(x+r,y)
    turtle.pendown()
    turtle.circle(r)

turtle.shape("turtle")
turtle.left(90)
draw_circle(0, 0, 50)
draw_circle(200, 200, 100)
draw_circle(100, -100, 50)
