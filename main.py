import turtle
turtle.pendown()
turtle.left(90)


def square(x, y, length, line_color, filling_color):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color(line_color, filling_color)
    turtle.begin_fill()
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.end_fill()


turtle.done()

