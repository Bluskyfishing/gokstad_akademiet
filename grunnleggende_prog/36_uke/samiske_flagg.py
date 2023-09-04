import turtle 

t = turtle.Turtle()

#Rød rektangel

def rektangel():
    turtle.Screen().bgcolor("black")
    t.speed(20)
    t.fillcolor("blue")
    t.begin_fill()
    t.up()
    t.forward(200)
    t.down()

    for side in range(0,2):
        t.left(90)
        t.forward(300)
        t.left(90)
        t.forward(500)
    
    t.end_fill()

rektangel()

#Kryss ut applikasjon.
turtle.exitonclick()