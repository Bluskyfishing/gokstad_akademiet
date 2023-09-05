import turtle 

t = turtle.Turtle()

#Rød rektangel

def rektangel():
    turtle.Screen().bgcolor("black")
    t.speed(5)
    t.fillcolor("blue")
    t.begin_fill()
    t.up()
    t.forward(200)
    t.down()

    for side in range(0,2):
        t.left(90)
        t.forward(301)
        t.left(90)
        t.forward(501)
    t.right(180)
    t.end_fill()

rektangel()

t.forward(300)
t.right(90)

#Rød rektangel
t.fillcolor("red")
t.begin_fill()
t.up()
t.forward(300)
t.left(90)
t.forward(200)
t.left(90)
t.forward(300)
t.left(90)
t.forward(200)
t.left(90)
t.end_fill()

#Grønn stripe
t.fillcolor("green")
t.begin_fill()
t.up()
t.forward(300)
t.right(90)
t.forward(40)
t.right(90)
t.forward(300)
t.right(90)
t.forward(120)
t.right(180)
t.forward(80)
t.left(90)
t.end_fill()

#Gul stripe
t.fillcolor("yellow")
t.begin_fill()
t.up()
t.forward(300)
t.left(90)
t.forward(40)
t.left(90)
t.forward(300)
t.right(90)
t.forward(40)
t.end_fill()

#Justering av posisjon
t.left(180)
t.forward(50)
t.left(90)
t.forward(50)
t.right(90)
t.forward(25)

#Sirkel blå/rød halvdel
t.width(15)
t.pendown()
t.pencolor("red")
t.circle(100,180)
t.pencolor("blue")
t.circle(100,180)

#Gjemme peker
t.penup()
t.fillcolor("black")
t.pencolor("black")
t.right(90)
t.forward(100)

#Kryss ut applikasjon
turtle.exitonclick()