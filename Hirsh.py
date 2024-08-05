import turtle as t
tim = t.Turtle()

import random
t.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color

tim.penup()
tim.hideturtle()
tim.speed("fastest")
tim.setheading(220)
tim.forward(300)
tim.setheading(0)

number_of_dots = 100
for dot_count in range(1, number_of_dots +1):
    tim.dot(20, random_color())
    tim.forward(50)

    if dot_count %10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

















screen = t.Screen()
screen.exitonclick()