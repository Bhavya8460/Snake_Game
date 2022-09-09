from turtle import Turtle, Screen

tim = Turtle('turtle')
screen = Screen()
tim.setheading(90)
tim.forward(100)

tom = Turtle('turtle')
tom.forward(100)
tom.setheading(0)

dom = Turtle('turtle')
dom.backward(100)
dom.setheading(180)

sem = Turtle('turtle')
sem.setheading(270)
sem.forward(100)


screen.exitonclick()