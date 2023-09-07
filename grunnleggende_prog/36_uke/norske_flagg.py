import turtle 

t = turtle.Turtle()

#Rød rektangel

def rektangel():
    turtle.Screen().bgcolor("black")
    t.speed(5)
    t.fillcolor("red")
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

#Hvit kors Vertikal
t.up()
t.left(180)
t.forward(380)

t.fillcolor("white")
t.begin_fill()

for side in range(0,2):
    t.right(90)
    t.forward(300)
    t.right(90)
    t.forward(100)

t.end_fill()

#Hvit kors Horizontal

t.forward(120)
t.right(90)
t.forward(100)
t.right(90)

t.begin_fill()

t.forward(500)
t.left(90)
t.forward(100)
t.left(90)
t.forward(500)
t.left(90)
t.forward(100)
t.right(180)
t.forward(30)

t.end_fill()

#Blått kors Horizontal

t.fillcolor("blue")
t.begin_fill()

t.right(90)
t.forward(500)
t.left(90)
t.forward(40)
t.left(90)
t.forward(500)
t.left(90)
t.forward(40)

t.end_fill()

#Blått kors Vertikalt

t.right(180)
t.forward(170)
t.right(90)
t.forward(150)
t.right(90)

t.begin_fill()

t.forward(300)
t.left(90)
t.forward(40)
t.left(90)
t.forward(300)
t.left(90)

t.end_fill()

#Gjemme peker
t.fillcolor("black")
t.right(90)
t.forward(100)

#Kryss ut applikasjon.
turtle.exitonclick()